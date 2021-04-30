#! /usr/bin/env python3
# coding: utf-8

import datetime

class Tournament:
    '''Class management tournament'''

    def __init__(self, name, place, nb_rounds, time_control, description):
        self.name = name
        self.place = place
        self.nb_rounds = nb_rounds
        self.time_control = time_control
        self.description = description

    @property
    def date(self):
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y")

    @property
    def get_rounds(self):
        #appel vers la BDD pour afficher la liste des instances de round du tournoi
        pass

    @property
    def get_players(self):
        #appel vers la BDD pour afficher la iste des indices correspondant aux instances du joueur
        pass