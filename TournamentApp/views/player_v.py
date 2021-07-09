#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.utils.clear import Clear


class LoadPlayerView:
    """Display all player in DB"""

    def __init__(self, menu, tournament):
        self.menu = menu
        self.tournament = tournament

    def _display_menu(self):
        Clear().screen()
        print(f"IL Y A {len(self.tournament.players)} JOUEURS DANS CE TOURNOI : ")
        for player in self.tournament.players:
            print(f"PRÉNOM : {player.first_name},"
                  f" NOM DE FAMILLE : {player.last_name},"
                  f" DATE DE NAISSANCE : {player.birth_date},"
                  f" CLASSEMENT GÉNÉRAL : {player.ranking}].")
        print('\nVeuillez choisir le joueur en entrant le chiffre correspondant.\n')
        for key, entry in self.menu.items():
            print(f'{key} : {entry.option}')
        print()

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input('>> ')
            if choice in self.menu:
                return self.menu[choice]
    
    def not_in_db(self):
        print("\nIl n'y a pas de joueurs dans la base de données, ")
        print('vous allez être redirigé vers la création de nouveaux joueurs.')


class AddOrCreatePlayerView:
    """Display the menu to add or create a player"""
    def __init__(self, menu, tournament):
        self.menu = menu
        self.tournament = tournament

    def _display_menu(self):
        Clear().screen()
        print(f"IL Y A {len(self.tournament.players)} JOUEURS DANS CE TOURNOI")
        for player in self.tournament.players:
            print(f"NOM DE FAMILLE : {player.last_name},"
                  f" PRÉNOM : {player.first_name},"
                  f" DATE DE NAISSANCE : {player.birth_date},"
                  f" CLASSEMENT GÉNÉRAL : {player.ranking}.")
        print('\nVeuillez choisir une option en entrant le chiffre correspondant.\n')
        for key, entry in self.menu.items():
            print(f'{key} : {entry.option}')
        print()

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input('>> ')
            if choice in self.menu:
                return self.menu[choice]
