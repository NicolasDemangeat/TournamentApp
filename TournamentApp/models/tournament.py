#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.round import Round
from TournamentApp.models.match import Match
import datetime

class Tournament:
    '''Class management tournament'''

    def __init__(self, name, place, nb_rounds, time_control, description):
        self.name = name
        self.place = place
        self.nb_rounds = nb_rounds
        self.time_control = time_control
        self.description = description
        self.date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.players = []
        self.rounds = []

    @property
    def get_rounds(self):
        #appel vers la BDD pour afficher la liste des instances de round du tournoi
        pass

    @property
    def get_players(self):
        #appel vers la BDD pour afficher la iste des indices correspondant aux instances du joueur
        pass

    def add_players(self, player):
        self.players.append(player)

    def add_rounds(self, round):
        self.rounds.append(round)

    def set_first_round(self):
        players_sorted_by_rank = sorted(self.players, key=lambda x: x.ranking)
        first_half = players_sorted_by_rank[:len(players_sorted_by_rank)//2]
        second_half = players_sorted_by_rank[len(players_sorted_by_rank)//2:]
        round1 = Round()

        for i in range(len(first_half)):
            round1.add_match(Match(player_1=first_half[i], score_p1=first_half[i].score, player_2=second_half[i], score_p2=second_half[i].score))
        
        self.rounds.append(round1)