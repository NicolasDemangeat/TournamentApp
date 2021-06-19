#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.round import Round
from TournamentApp.models.match import Match
import datetime
import itertools

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
    def get_nb_rounds(self):
        return self.nb_rounds

    def add_score(self, choices, round_num):
        choices_values = [value for value in choices.values()]
        tuples_values = [[choices_values[i], choices_values[i+1]] for i in range(0, len(choices_values), 2)]

        for player, choice in choices.items():
            player.points += choice

        for values, match in zip(tuples_values, self.rounds[round_num].matchs):
            match.set_score_p1(values[0])
            match.set_score_p2(values[1])

    def add_players(self, player):
        self.players.append(player)

    def add_rounds(self, round):
        self.rounds.append(round)

    def set_first_round(self):
        '''Methode to create the first round'''
        self.all_possible_pairs = set(itertools.combinations(self.players, 2))
        self.match_already_done = set()

        players_sorted_by_rank = sorted(self.players, key=lambda x: x.ranking)
        first_half = players_sorted_by_rank[:len(players_sorted_by_rank)//2]
        second_half = players_sorted_by_rank[len(players_sorted_by_rank)//2:]
        round1 = Round()        

        for i, el in enumerate(first_half):
            round1.add_match(Match(el, el.points, second_half[i], second_half[i].points))
            self.match_already_done.add((el, second_half[i]))

        self.add_rounds(round1)

    def set_next_round(self):
        '''Methode to create the n next rounds'''
        
        rest_paires = self.all_possible_pairs - self.match_already_done
        players_sorted_by_points = sorted(self.players, key=lambda x: (x.points, x.ranking), reverse=True)
        round_n = Round()        

        for i in range(0, len(players_sorted_by_points), 2):
            temp = (players_sorted_by_points[i], players_sorted_by_points[i+1])
            round_n.add_match(Match(players_sorted_by_points[i], 
            players_sorted_by_points[i].points, 
            players_sorted_by_points[i+1], 
            players_sorted_by_points[i+1].points))
            self.match_already_done.add(temp)

        self.add_rounds(round_n)



