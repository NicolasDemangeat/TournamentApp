#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.utils.clear import Clear
import os


class RapportMenuView:
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
    def display_player_alpha(self, table):
        print('Liste de tous les acteurs par ordre alphabétique : \n')

        sorted_players = sorted(table, key=lambda k: k['last_name'])

        for player in sorted_players:
            print(f"NOM DE FAMILLE : {player['last_name']},"
                  f" PRÉNOM : {player['first_name']},"
                  f" DATE DE NAISSANCE : {player['birth_date']},"
                  f" SEXE : {player['gender']},"
                  f" CLASSEMENT GÉNÉRAL : {player['ranking']}.")

        os.system("pause")

    def display_player_ranking(self, table):
        print('Liste de tous les acteurs par classement : \n')

        sorted_players = sorted(table, key=lambda k: int(k['ranking']))

        for player in sorted_players:
            print(f"NOM DE FAMILLE : {player['last_name']},"
                  f" PRÉNOM : {player['first_name']},"
                  f" DATE DE NAISSANCE : {player['birth_date']},"
                  f" SEXE : {player['gender']},"
                  f" CLASSEMENT GÉNÉRAL : {player['ranking']}.")

        os.system("pause")

class RapportTournamentMenuView:
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
    def display_all_tournaments(self, table):
        print('Liste de tous les tournois enregistrés.\n')

        for tournament in table:
            print(f"NOM DU TOURNOI : {tournament['name']}, "
                  f"LIEUX : {tournament['place']}, "
                  f"DATE : {tournament['date']}, "
                  f"NOMBRES DE ROUNDS : {tournament['nb_rounds']}, "
                  f"TYPE DE CONTROLE DU TEMPS : {tournament['time_control']}, "
                  f"DESCRIPTION : {tournament['description']}.")

        os.system("pause")

    def display_all_rounds(self, tournament):
        print('Liste de tous les rounds du tournoi : ')

        for round in tournament:
            print(f"NOM DU ROUND : {round['name']}, "
                  f"DATE DE DEBUT : {round['start_date']}, "
                  f"DATE DE FIN : {round['end_date']}, "
                  f"NOMBRES DE MATCHS : {len(round['matchs'])}.")

        os.system("pause")

    def display_all_matchs(self, tournament):
        print('Liste de tous les matchs du tournoi : ')

        for round in tournament:
            for i, match in enumerate(round['matchs']):
                print(f'{round["name"]} - MATCH {i+1} : {match["match"]}')

        os.system("pause")