#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.managementbdd import ManagementBdd
from tinydb import TinyDB


class Player(ManagementBdd):
    '''Class management Player'''

    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking