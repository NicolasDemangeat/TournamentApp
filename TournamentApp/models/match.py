#! /usr/bin/env python3
# coding: utf-8

class Match:
    '''Class management Match'''

    def __init__(self, player_1, points_p1, player_2, points_p2):
        self.points_p1 = points_p1
        self.points_p2 = points_p2
        self.player_1 = player_1
        self.player_2 = player_2

    @property
    def get_match(self):
        return f'[{self.player_1.first_name}] contre [{self.player_2.first_name}]'

    @property
    def get_players(self):
        return [self.player_1, self.player_2]

    @property
    def get_score(self):
        return [self.points_p1, self.points_p2]

    def set_score_p1(self, choice):
        self.points_p1 = choice

    def set_score_p2(self, choice):
        self.points_p2 = choice
