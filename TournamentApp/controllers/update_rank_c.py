#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.managementbdd import ManagementDataBase
from TournamentApp.utils.clear import Clear
from TournamentApp.utils.constraint import Constraint
from TournamentApp.views.rank_v import UpdateRankingView
from TournamentApp.controllers import menu_c


class UpdateRankController:
    """This controler is called when user want to change player rank"""
    def __init__(self):
        self.view = UpdateRankingView()
        self.db = ManagementDataBase()
        self.constraint = Constraint()

    def __call__(self):
        Clear().screen()
        player_exist = False
        while player_exist is False:
            while True:
                self.first_name = self.view.get_player_firstname()
                check_first_name = [self.constraint.not_empty(self.first_name)]
                if False not in check_first_name:
                    break

            while True:
                self.last_name = self.view.get_player_lastname()
                check_last_name = [self.constraint.not_empty(self.last_name)]
                if False not in check_last_name:
                    break

            while True:
                self.birth_date = self.view.gat_player_birth_date()
                check_birth_date = [self.constraint.is_date(self.birth_date)]
                if False not in check_birth_date:
                    break

            player_exist = self.db.find_player(self.first_name, self.last_name, self.birth_date)

            if player_exist is False:
                self.view.dont_exist()

        while True:
            self.rank = self.view.new_rank()
            check_new_rank = [self.constraint.is_integer(self.rank)]
            if False not in check_new_rank:
                self.rank = int(self.rank)
                break

        self.db.rank_update(self.first_name, self.last_name, self.birth_date, self.rank)

        while True:
            self.yes_or_no = self.view.end_update()
            check_yes_or_no = [self.constraint.not_empty(self.yes_or_no)]
            if False not in check_yes_or_no and self.yes_or_no.lower() in ['o', 'n']:
                if self.yes_or_no.lower() == 'o':
                    return UpdateRankController()
                elif self.yes_or_no.lower() == 'n':
                    return menu_c.HomeMenuController()
                break
