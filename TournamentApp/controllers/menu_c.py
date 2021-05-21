#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.utils.menus import Menu
from TournamentApp.views.home import HomeMenuView

class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add('auto', 'Créer un tournoi', NewTournamentController())
        self.menu.add('auto', 'Générer des rapports', RapportMenuController())
        self.menu.add('Q', 'Quitter', EndAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler

class NewTournamentController:
    pass

class RapportMenuController:
    pass

class EndAppController:
    pass