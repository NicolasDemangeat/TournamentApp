#! /usr/bin/env python3
# coding: utf-8


from TournamentApp.utils.constraint import Constraint
from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.models.round import Round
from TournamentApp.controllers import menu_c
from TournamentApp.utils.clear import Clear
from TournamentApp.models.player import Player
from TournamentApp.models.tournament import Tournament
from TournamentApp.views.tournament_v import TournamentView


class NewTournamentController:
    """
    Called when user want to create a new tournament.
    Ask user's choices, check all choices, and create a new tournament.
    """

    def __init__(self):
        self.view = TournamentView()
        self.data_base = ManagementDataBase()
        self.constraint = Constraint()

    def __call__(self):
        # creation of the tournament instance and save in DB
        Clear().screen()
        choices = self.view.tournament_sequence()
        choices_check_empty = [self.constraint.not_empty(choice) for choice in choices]
        choices_check_integer = [self.constraint.is_integer(choices[2])]

        while False in choices_check_empty or False in choices_check_integer:
            if False in choices_check_empty and False in choices_check_integer:
                self.view.empty_value()
                self.view.not_integer()
            elif False in choices_check_empty:
                self.view.empty_value()
            elif False in choices_check_integer:
                self.view.not_integer()
            choices = self.view.tournament_sequence()
            choices_check_empty = [self.constraint.not_empty(choice) for choice in choices]
            choices_check_integer = [self.constraint.is_integer(choices[2])]

        self.tournament = Tournament(*choices)
        self.data_base.save_tournament(self.tournament)

        return menu_c.AddOrCreatePlayerMenu(self.tournament)


class NewPlayersController:
    """Create new player, add in DB and in tournament"""

    def __init__(self, tournament=None):
        self.tournament = tournament
        self.view = TournamentView()
        self.data_base = ManagementDataBase()
        self.constraint = Constraint()

    def __call__(self):
        Clear().screen()
        player_choices = self.view.players_sequence()
        empty_check = [self.constraint.not_empty(choice) for choice in player_choices]
        integer_check = [self.constraint.is_integer(player_choices[4])]
        positiv_check = [self.constraint.is_positiv(player_choices[4])]
        date_check = [self.constraint.is_date(player_choices[2])]

        while (False in empty_check or False in integer_check
                or False in positiv_check or False in date_check):
            if (False in empty_check and False in integer_check
                    and False in positiv_check and False in date_check):
                self.view.empty_value()
                self.view.not_integer()
                self.view.not_positiv()
                self.view.not_date()
            elif False in empty_check and False in integer_check:
                self.view.empty_value()
                self.view.not_integer()
            elif False in empty_check and False in positiv_check:
                self.view.empty_value()
                self.view.not_positiv()
            elif False in empty_check and False in date_check:
                self.view.empty_value()
                self.view.not_date()
            elif False in integer_check and False in positiv_check:
                self.view.not_integer()
                self.view.not_positiv()
            elif False in integer_check and False in date_check:
                self.view.not_integer()
                self.view.not_date()
            elif False in date_check and False in positiv_check:
                self.view.not_date()
                self.view.not_positiv()
            elif False in integer_check:
                self.view.not_integer()
            elif False in empty_check:
                self.view.empty_value()
            elif False in positiv_check:
                self.view.not_positiv()
            elif False in date_check:
                self.view.not_date()

            player_choices = self.view.players_sequence()
            empty_check = [self.constraint.not_empty(choice) for choice in player_choices]
            integer_check = [self.constraint.is_integer(player_choices[4])]
            positiv_check = [self.constraint.is_positiv(player_choices[4])]
            date_check = [self.constraint.is_date(player_choices[2])]

        player = Player(*player_choices)
        self.data_base.save_players(player)
        if self.tournament:
            self.tournament.add_players(player)
            self.data_base.save_tournament(self.tournament)
            self.view.player_added()
            continu = self.view.player_continue()
            if continu:
                return menu_c.AddOrCreatePlayerMenu(self.tournament)
            else:
                return NewRoundController(self.tournament)
        else:
            self.view.player_added()
            input('Appuyez sur une touche pour continuer...')
            return menu_c.HomeMenuController()


class LoadPlayerController:
    """Add the chosen player to the curent tournament"""

    def __init__(self, player, tournament):
        self.tournament = tournament
        self.db = ManagementDataBase()
        self.player = player
        self.view = TournamentView()

    def __call__(self):
        new_player = self.db.load_player(self.player)
        self.tournament.add_players(new_player)
        self.view.display_add_player(new_player)

        continu = self.view.player_continue()
        if continu:
            return menu_c.AddOrCreatePlayerMenu(self.tournament)
        else:
            return NewRoundController(self.tournament)


class NewRoundController:
    """Creat all rounds for a tournament"""

    def __init__(self, tournament):
        self.tournament = tournament
        self.view = TournamentView()
        self.data_base = ManagementDataBase()

    def __call__(self):
        Clear().screen()
        # creation of rounds
        start = int(self.tournament.round_played)
        end = int(self.tournament.get_nb_rounds)

        for i in range(start, end):
            nb_round_remaining = int(self.tournament.get_nb_rounds) - int(self.tournament.round_played)
            self.view.display_round_remaining(nb_round_remaining)
            if i == 0:
                self.tournament.set_first_round()
            else:
                self.tournament.set_next_round()
            choices = self.view.set_players_score(self.tournament, i)
            self.tournament.add_score(choices, i)
            self.tournament.rounds[i].set_end_date()
            self.tournament.set_round_played()
            self.data_base.save_tournament(self.tournament)
            Clear().screen()

        # end of tournament
        self.tournament.set_end_date()
        self.data_base.save_tournament(self.tournament)
        self.view.winner_announcement(self.tournament)
        Round.reset_round_number()

        return menu_c.EndTournamentMenuController()
