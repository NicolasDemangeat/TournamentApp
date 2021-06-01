#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.player import Player
from TournamentApp.models.tournament import Tournament
from TournamentApp.views.tournament_v import TournamentView


class NewTournamentController:
    def __init__(self):
        self.view = TournamentView()

    def __call__(self):
        liste_choices = self.view.tournament_sequence()

        self.tournoi = Tournament(*liste_choices)

        continuer = True
        while continuer:
            liste_players = self.view.players_sequence()
            self.tournoi.add_players(Player(*liste_players))            
            continuer = self.view.player_continue()

        self.view.matchs_selection()
        self.tournoi.set_first_round()
        for el in self.tournoi.rounds[0].matchs:
            el.get_match

        