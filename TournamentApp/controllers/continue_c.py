#! /usr/bin/env python3
# coding: utf-8

from tinydb import where

from TournamentApp.controllers.tournament_c import NewRoundController
from TournamentApp.controllers import menu_c
from TournamentApp.views.tournament_v import TournamentView
from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.views.rapport_v import RapportTournamentMenuView
from TournamentApp.utils.menus import Menu


class ContinueTournamentMenu:
    """Display tournaments with no end date"""

    def __init__(self):
        self.menu = Menu()
        self.view = RapportTournamentMenuView(self.menu)
        self.data_base = ManagementDataBase()

    def __call__(self):
        for tournament in self.data_base.tournaments_table.search(where('end_date') == str("None")):
            self.menu.add(
                'auto',
                f'NOM DU TOURNOI : {tournament["name"]:15}| '
                f'LIEUX : {tournament["place"]:15}| '
                f'DATE : {tournament["date"]:11}',
                ContinueTournamentController(tournament))

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class ContinueTournamentController:
    """This controller help user to continue a tournament"""

    def __init__(self, tournament):
        self.tournament = tournament
        self.db = ManagementDataBase()
        self.view = TournamentView()

    def __call__(self):
        new_tournament = self.db.load_tournament(self.tournament)

        if new_tournament.round_played == 0:
            self.view.go_to_player_creation()
            input('Appuyez sur une touche pour continuer...')
            return menu_c.AddOrCreatePlayerMenu(new_tournament)
        else:
            self.view.go_to_round_creation()
            input('Appuyez sur une touche pour continuer...')
            return NewRoundController(new_tournament)
