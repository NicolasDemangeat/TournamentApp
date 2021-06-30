#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.controllers.update_rank_c import UpdateRankControler
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
from TournamentApp.controllers.tournament_c import NewTournamentController
from TournamentApp.utils.menus import Menu
from TournamentApp.views.home import HomeMenuView


class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        Clear().screen()
        self.menu.add('auto', 'Créer un tournoi', NewTournamentController())
        self.menu.add('auto', 'Générer des rapports', RapportMenuController())
        self.menu.add('auto', "Modifier le classement d'un joueur", UpdateRankControler())
        self.menu.add('auto', 'Quitter', EndAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class RapportMenuController:
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
    def __call__(self):
        return None


class EndTournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = EndTournamentView(self.menu)

    def __call__(self):
        self.menu.add('auto', 'Retour au menu principal', HomeMenuController())
        self.menu.add('auto', "Modifier le classement d'un joueur", UpdateRankControler())
        self.menu.add('auto', 'Quitter l\'application', EndAppController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler
