#! /usr/bin/env python3
# coding: utf-8

class Match:
    '''Class management Match'''

    def __init__(self, player_1, score_p1, player_2, score_p2):
        self.match = ([player_1, score_p1], [player_2, score_p2])