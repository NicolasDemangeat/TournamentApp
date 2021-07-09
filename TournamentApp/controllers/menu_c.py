#! /usr/bin/env python3
# coding: utf-8

from tinydb import where
import os

from TournamentApp.views.player_v import AddOrCreatePlayerView, LoadPlayerView
from TournamentApp.controllers.continue_c import ContinueTournamentMenu
from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.controllers.update_rank_c import UpdateRankController
from TournamentApp.utils.clear import Clear
from TournamentApp.views.end_tournament_v import EndTournamentView
from TournamentApp.controllers.rapport_c import (
    AllActorAlpha,
    AllActorRank,
    AllPalyersAlphaMenu,
    AllPalyersRankMenu,
    AllTournaments,
    AllRoundTournamentMenu,
    AllMatchsTournamentMenu
    )
from TournamentApp.views.rapport_v import RapportMenuView
from TournamentApp.controllers.tournament_c import LoadPlayerController, NewPlayersController, NewTournamentController
from TournamentApp.utils.menus import Menu
from TournamentApp.views.home import HomeMenuView


class HomeMenuController:
    """Main menu controller, display the menu."""
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.db = ManagementDataBase()

    def __call__(self):
        Clear().screen()
        if self.db.tournaments_table.contains(where('end_date') == str("None")):
            self.menu.add('auto', 'Reprendre un tournoi en cours', ContinueTournamentMenu())
            self.menu.add('auto', 'Créer des joueurs', NewPlayersController())
            self.menu.add('auto', 'Générer des rapports', RapportMenuController())
            self.menu.add('auto', "Modifier le classement d'un joueur", UpdateRankController())
            self.menu.add('auto', 'Quitter', EndAppController())
        else:
            self.menu.add('auto', 'Créer un tournoi', NewTournamentController())
            self.menu.add('auto', 'Créer des joueurs', NewPlayersController())
            self.menu.add('auto', 'Générer des rapports', RapportMenuController())
            self.menu.add('auto', "Modifier le classement d'un joueur", UpdateRankController())
            self.menu.add('auto', 'Quitter', EndAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class RapportMenuController:
    """Display the rapport main menu"""
    def __init__(self):
        self.menu = Menu()
        self.view = RapportMenuView(self.menu)

    def __call__(self):
        Clear().screen()
        self.menu.add('auto', 'Liste de tous les acteurs par ordre alphabétique', AllActorAlpha())
        self.menu.add('auto', 'Liste de tous les acteurs par classement', AllActorRank())
        self.menu.add('auto', 'Liste de tous les joueurs d\'un tournoi par ordre alphabétique', AllPalyersAlphaMenu())
        self.menu.add('auto', 'Liste de tous les joueurs d\'un tournoi par classement', AllPalyersRankMenu())
        self.menu.add('auto', 'Liste de tous les tournois', AllTournaments())
        self.menu.add('auto', 'Liste de tous les tours d\'un tournoi', AllRoundTournamentMenu())
        self.menu.add('auto', 'Liste de tous les matchs d\'un tournoi', AllMatchsTournamentMenu())
        self.menu.add('auto', 'Retour au menu principal', HomeMenuController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class EndAppController:
    """Close the app"""
    def __call__(self):
        return None


class EndTournamentMenuController:
    """Called when a tournament is finish, display a menu."""
    def __init__(self):
        self.menu = Menu()
        self.view = EndTournamentView(self.menu)

    def __call__(self):
        self.menu.add('auto', 'Retour au menu principal', HomeMenuController())
        self.menu.add('auto', "Modifier le classement d'un joueur", UpdateRankController())
        self.menu.add('auto', 'Quitter l\'application', EndAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class LoadPlayerMenu:
    """Display a menu that contains all players in DB"""

    def __init__(self, tournament):
        self.menu = Menu()
        self.data_base = ManagementDataBase()
        self.tournament = tournament
        self.view = LoadPlayerView(self.menu, self.tournament)

    def __call__(self):
        Clear().screen()
        if len(self.data_base.players_table) < 1:
            self.view.not_in_db()
            os.system("Pause")
            return NewPlayersController(self.tournament)
        for player in self.data_base.players_table:
            self.menu.add(
                'auto',
                f'PRENOM : {player["first_name"].center(15)}, '
                f'NOM : {player["last_name"].center(15)}, '
                f'DATE DE NAISSANCE: {player["birth_date"].center(12)}, '
                f'CLASSEMENT : {player["ranking"].center(2)}',
                LoadPlayerController(player, self.tournament))

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class AddOrCreatePlayerMenu:
    """Display a menu for help user to choose between add or creat a player"""

    def __init__(self, tournament):
        self.menu = Menu()
        self.tournament = tournament
        self.view = AddOrCreatePlayerView(self.menu, self.tournament)

    def __call__(self):
        Clear().screen()
        self.menu.add('auto', 'Choisir un joueur depuis la base de données', LoadPlayerMenu(self.tournament))
        self.menu.add('auto', "Créer un nouveau joueur", NewPlayersController(self.tournament))

        user_choice = self.view.get_user_choice()

        return user_choice.handler
