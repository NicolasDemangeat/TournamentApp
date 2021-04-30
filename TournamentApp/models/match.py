#! /usr/bin/env python3
# coding: utf-8

class Match:
    '''Class management Match'''

    def __init__(self, player_1, score_p1, player_2, score_p2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_p1 = score_p1
        self.score_p2 = score_p2
        self.match = ([self.player_1, self.score_p1], [self.player_2, score_p2])