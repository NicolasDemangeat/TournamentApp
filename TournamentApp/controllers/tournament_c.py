#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.utils.constraint import Constraint
from tinydb import where

from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.models.round import Round
from TournamentApp.controllers import menu_c
from TournamentApp.utils.clear import Clear
from TournamentApp.models.player import Player
from TournamentApp.models.tournament import Tournament
from TournamentApp.views.tournament_v import TournamentView

class NewTournamentController:
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
        Clear().screen()

        # creation of players and save in DB
        continuer = True
        while continuer:
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

            player = Player(*player_choices)
            self.tournament.add_players(player)
            self.data_base.save_players(player)
            self.data_base.save_tournament(self.tournament)
            continuer = self.view.player_continue()
            Clear().screen()

        # creation of rounds
        for i in range(int(self.tournament.get_nb_rounds)):
            if i == 0:
                self.tournament.set_first_round()
            else:
                self.tournament.set_next_round()
            choices = self.view.set_players_score(self.tournament, i)
            self.tournament.add_score(choices, i)
            self.tournament.rounds[i].set_end_date()
            self.data_base.save_tournament(self.tournament)
            Clear().screen()

        # end of tournament
        self.data_base.save_tournament(self.tournament)
        self.view.winner_announcement(self.tournament)
        Round.reset_round_number()

        return menu_c.EndTournamentMenuController()
