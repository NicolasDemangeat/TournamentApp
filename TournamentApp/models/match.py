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
        print(f'{self.player_1.first_name} - {self.player_2.first_name}')