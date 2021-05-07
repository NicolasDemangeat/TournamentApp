#! /usr/bin/env python3
# coding: utf-8

class Player:
    '''Class management Player'''

    def __init__(self, first_name, last_name, birth_date, gender, ranking, points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.points = points