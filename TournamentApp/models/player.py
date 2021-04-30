#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB

class Player:
    '''Class management Player'''

    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def save_into_db(self):
        '''Serialize player infos and save into DB'''
        serialized_player = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'ranking': self.ranking
        }

        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(serialized_player)

    def read_db(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        liste_player = players_table.all()
        return liste_player