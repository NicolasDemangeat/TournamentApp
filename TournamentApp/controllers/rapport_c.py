#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.utils.menus import Menu
from TournamentApp.utils.clear import Clear
from TournamentApp.controllers import menu_c
from tinydb import TinyDB
from TournamentApp.views.rapport_v import RapportPlayerView, RapportTournamentMenuView, RapportTournamentView

class AllActorAlpha:
    def __init__(self):
        self.view = RapportPlayerView()
        self.db = TinyDB('db_echec.json')
        self.players_table = self.db.table('players')

    def __call__(self):
        Clear().screen()
        sorted_players = sorted(self.players_table, key=lambda k: k['last_name'])
        self.view.display_player_alpha(sorted_players)

        return menu_c.RapportMenuController()

class AllActorRank:
    def __init__(self):
        self.view = RapportPlayerView()
        self.db = TinyDB('db_echec.json')
        self.players_table = self.db.table('players')

    def __call__(self):
        Clear().screen()
        sorted_players = sorted(self.players_table, key=lambda k: int(k['ranking']))
        self.view.display_player_ranking(sorted_players)

        return menu_c.RapportMenuController()

class AllPalyersAlphaMenu:
    def __init__(self):
        self.menu = Menu()
        self.view = RapportTournamentMenuView(self.menu)
        self.data_base = ManagementDataBase()

    def __call__(self):
        for tournament in self.data_base.tournaments_table:
            self.menu.add(
                'auto', 
                f'NOM DU TOURNOI : {tournament["name"]}, '
                f'LIEUX : {tournament["place"]}, '
                f'DATE : {tournament["date"]}.', 
                AllPlayersAlpha(tournament))
        
        user_choice = self.view.get_user_choice()

        return user_choice.handler

class AllPlayersAlpha:
    def __init__(self, tournament):
        self.tournament = tournament
        self.view = RapportPlayerView()

    def __call__(self):
        self.view.display_player_alpha(self.tournament['players_tournament'])

        return menu_c.RapportMenuController()

class AllPalyersRankMenu:
    def __init__(self):
        self.menu = Menu()
        self.view = RapportTournamentMenuView(self.menu)
        self.data_base = ManagementDataBase()

    def __call__(self):
        for tournament in self.data_base.tournaments_table:
            self.menu.add(
                'auto', 
                f'NOM DU TOURNOI : {tournament["name"]}, '
                f'LIEUX : {tournament["place"]}, '
                f'DATE : {tournament["date"]}.', 
                AllPlayersRank(tournament))
        
        user_choice = self.view.get_user_choice()

        return user_choice.handler

class AllPlayersRank:
    def __init__(self, tournament):
        self.tournament = tournament
        self.view = RapportPlayerView()

    def __call__(self):
        self.view.display_player_ranking(self.tournament['players_tournament'])

        return menu_c.RapportMenuController()

class AllTournaments:
    def __init__(self):
        self.view = RapportTournamentView()
        self.db = TinyDB('db_echec.json')
        self.tournaments_table = self.db.table('tournaments')

    def __call__(self):
        Clear().screen()
        self.view.display_all_tournaments(self.tournaments_table)

        return menu_c.RapportMenuController()

class AllRoundTournamentMenu:
    def __init__(self):
        self.menu = Menu()
        self.view = RapportTournamentMenuView(self.menu)
        self.data_base = ManagementDataBase()

    def __call__(self):
        for tournament in self.data_base.tournaments_table:
            self.menu.add(
                'auto', 
                f'NOM DU TOURNOI : {tournament["name"]}, '
                f'LIEUX : {tournament["place"]}, '
                f'DATE : {tournament["date"]}.', 
                AllRoundTournament(tournament))
        
        user_choice = self.view.get_user_choice()

        return user_choice.handler

class AllRoundTournament:
    def __init__(self, tournament):
        self.tournament = tournament
        self.view = RapportTournamentView()

    def __call__(self):
        Clear().screen()
        self.view.display_all_rounds(self.tournament['all_round'])

        return menu_c.RapportMenuController()

class AllMatchsTournamentMenu:
    def __init__(self):
        self.menu = Menu()
        self.view = RapportTournamentMenuView(self.menu)
        self.data_base = ManagementDataBase()

    def __call__(self):
        for tournament in self.data_base.tournaments_table:
            self.menu.add(
                'auto', 
                f'NOM DU TOURNOI : {tournament["name"]}, '
                f'LIEUX : {tournament["place"]}, '
                f'DATE : {tournament["date"]}.', 
                AllMatchsTournament(tournament))
        
        user_choice = self.view.get_user_choice()

        return user_choice.handler

class AllMatchsTournament:
    def __init__(self, tournament):
        self.tournament = tournament
        self.view = RapportTournamentView()

    def __call__(self):
        Clear().screen()
        self.view.display_all_matchs(self.tournament['all_round'])

        return menu_c.RapportMenuController()