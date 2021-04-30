#! /usr/bin/env python3
# coding: utf-8


from .tournament import Tournament
import datetime

class Round(Tournament):
    '''Class management round'''

    round_number = 1

    def __init__(self):
        self.name = f'Round {type(self).round_number}'
        self.start_date = datetime.datetime.now().strftime("Date: %d/%m/%Y \nHeure: %H:%M:%S")
        self.end_date = None
        self.matchs = []
        type(self).round_number += 1

    @classmethod
    def reset_round_number(cls):
        cls.round_number = 1

    def set_end_date(self):
        '''Set the date and time when round is finish'''
        self.end_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")