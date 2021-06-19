#! /usr/bin/env python3
# coding: utf-8

from tinydb import where

from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.models.round import Round
from TournamentApp.controllers import menu_c
from TournamentApp.utils.clear import Clear
from TournamentApp.models.player import Player
from TournamentApp.models.tournament import Tournament
from TournamentApp.views.tournament_v import TournamentView

class NewTournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.data_base = ManagementDataBase()

    def __call__(self):
        Clear().screen()
        choices = self.view.tournament_sequence()
        self.tournament = Tournament(*choices)
        self.data_base.save_tournament(self.tournament)
        Clear().screen()

        continuer = True
        while continuer:
            liste_players = self.view.players_sequence()
            
            player = Player(*liste_players)
            self.tournament.add_players(player)
            self.data_base.save_players(player)
            self.data_base.save_tournament(self.tournament)
            continuer = self.view.player_continue()
            Clear().screen()

        for i in range(int(self.tournament.get_nb_rounds)):
            if i == 0:
                self.tournament.set_first_round()
            else:
                self.tournament.set_next_round()
            choices = self.view.set_players_score(self.tournament, i)
            self.tournament.add_score(choices, i)
            self.tournament.rounds[i].set_end_date()
            self.data_base.save_tournament(self.tournament)
            Clear().screen()

        self.data_base.save_tournament(self.tournament)
        self.view.winner_announcement(self.tournament)
        Round.reset_round_number()

        return menu_c.EndTournamentMenuController()
