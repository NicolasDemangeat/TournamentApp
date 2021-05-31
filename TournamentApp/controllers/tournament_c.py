#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.player import Player
from TournamentApp.models.tournament import Tournament
from TournamentApp.views.tournament_v import TournamentView


class NewTournamentController:
    def __init__(self):
        self.view = TournamentView()

    def __call__(self):
        liste_tournament_sequence = self.view.tournament_sequence()
        liste_input = [input, input, input, input, input]
        liste_choice = []

        for sentence, choice in zip(liste_tournament_sequence, liste_input):
            print(sentence)
            liste_choice.append(choice('>> '))

        tournoi = Tournament(*liste_choice)

        liste_players_sequence = self.view.players_sequence()
        liste_choice = []
        continuer = True
        while continuer:
            for sentence, choice in zip(liste_players_sequence, liste_input):
                print(sentence)
                liste_choice.append(choice('>> '))
            
            tournoi.players.append(Player(*liste_choice))
            liste_choice = []
            continuer = self.view.player_continue()