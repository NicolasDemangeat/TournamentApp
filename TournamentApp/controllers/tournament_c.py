#! /usr/bin/env python3
# coding: utf-8
from TournamentApp.controllers import menu_c
from TournamentApp.utils.clear import Clear
from TournamentApp.models.player import Player
from TournamentApp.models.tournament import Tournament
from TournamentApp.views.tournament_v import TournamentView

class NewTournamentController:
    def __init__(self):
        self.view = TournamentView()

    def __call__(self):
        Clear().screen()
        choices = self.view.tournament_sequence()

        self.tournoi = Tournament(*choices)

        Clear().screen()

        continuer = True
        while continuer:
            liste_players = self.view.players_sequence()
            self.tournoi.add_players(Player(*liste_players))
            continuer = self.view.player_continue()
            Clear().screen()

        for i in range(int(self.tournoi.get_nb_rounds)):
            if i == 0:
                self.tournoi.set_first_round()
            else:
                self.tournoi.set_next_round()
            self.view.matchs_selection(self.tournoi, i)
            choices = self.view.set_players_score(self.tournoi)
            self.tournoi.add_score(choices)
            Clear().screen()        

        self.view.winner_announcement(self.tournoi)

        return menu_c.EndTournamentMenuController()
