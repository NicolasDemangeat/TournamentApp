#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.utils.clear import Clear
import os


class RapportMenuView:
    """This view display the rapport main menu"""

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print('\nVeuillez choisir une option en entrant le chiffre correspondant.')
        for key, entry in self.menu.items():
            print(f'{key} : {entry.option}')
        print()

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input('>> ')
            if choice in self.menu:
                return self.menu[choice]


class RapportPlayerView:
    """This view contains all methods to display players, sort by alphabetical order or rank"""

    def display_player_alpha(self, table):
        print('Liste de tous les acteurs par ordre alphabétique : \n')

        for player in table:
            print(f"NOM DE FAMILLE : {player['last_name'].center(15)},"
                  f" PRÉNOM : {player['first_name'].center(15)},"
                  f" DATE DE NAISSANCE : {player['birth_date'].center(12)},"
                  f" SEXE : {player['gender'].center(2)},"
                  f" CLASSEMENT GÉNÉRAL : {player['ranking'].center(2)}.")

        os.system("pause")

    def display_player_ranking(self, table):
        print('Liste de tous les acteurs par classement : \n')

        for player in table:
            print(f"NOM DE FAMILLE : {player['last_name'].center(15)},"
                  f" PRÉNOM : {player['first_name'].center(15)},"
                  f" DATE DE NAISSANCE : {player['birth_date'].center(12)},"
                  f" SEXE : {player['gender'].center(2)},"
                  f" CLASSEMENT GÉNÉRAL : {player['ranking'].center(2)}.")

        os.system("pause")


class RapportTournamentMenuView:
    """Display a menu of all the tournaments in DB"""

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        Clear().screen()
        print('\nVeuillez choisir le tournoi en entrant le chiffre correspondant.')
        for key, entry in self.menu.items():
            print(f'{key} : {entry.option}')
        print()

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input('>> ')
            if choice in self.menu:
                return self.menu[choice]


class RapportTournamentView:
    """Contains all methods to display tournament infos"""

    def display_all_tournaments(self, table):
        print('Liste de tous les tournois enregistrés.\n')

        for tournament in table:
            print(f"NOM DU TOURNOI : {tournament['name'].center(15)}, "
                  f"LIEUX : {tournament['place'].center(15)}, "
                  f"DATE : {tournament['date'].center(12)}, "
                  f"NOMBRES DE ROUNDS : {tournament['nb_rounds'].center(3)}, "
                  f"TYPE DE CONTROLE DU TEMPS : {tournament['time_control'].center(10)}, "
                  f"DESCRIPTION : {tournament['description'].center(25)}.")

        os.system("pause")

    def display_all_rounds(self, tournament):
        print('Liste de tous les rounds du tournoi : ')

        for round in tournament:
            print(f"NOM DU ROUND : {round['name'].center(9)}, "
                  f"DATE DE DEBUT : {round['start_date'].center(12)}, "
                  f"DATE DE FIN : {round['end_date'].center(12)}, "
                  f"NOMBRES DE MATCHS : {str(len(round['matchs'])).center(3)}.")

        os.system("pause")

    def display_all_matchs(self, tournament):
        print('Liste de tous les matchs du tournoi : \n')

        for round in tournament:
            print()
            for i, match in enumerate(round['matchs']):
                print(f'{round["name"]} - MATCH {i+1} : {match["match"]}')

        os.system("pause")
