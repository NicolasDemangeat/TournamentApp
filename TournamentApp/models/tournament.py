#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.round import Round
from TournamentApp.models.match import Match
import datetime
from itertools import repeat


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
        return int(self.nb_rounds)

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
        '''Method to create the first round'''
        self.match_already_done = set()
        players_sorted_by_rank = sorted(self.players, key=lambda x: x.ranking)
        first_half = players_sorted_by_rank[:len(players_sorted_by_rank)//2]
        second_half = players_sorted_by_rank[len(players_sorted_by_rank)//2:]
        round1 = Round()

        for player1, player2 in zip(first_half, second_half):
            round1.add_match(Match(player1, player1.points, player2, player2.points))
            self.match_already_done.add((player1, player2))
            self.match_already_done.add((player2, player1))

        self.add_rounds(round1)

    def set_next_round(self):
        '''Method to create the n next rounds'''

        players_sorted_by_points = sorted(self.players, key=lambda x: (x.points, x.ranking), reverse=True)
        round_n = Round()

        for i in range(len(players_sorted_by_points)//2):
            for player1, player2 in zip(repeat(players_sorted_by_points[0]), players_sorted_by_points[1:]):
                temp = (player1, player2)
                reverse_temp = (player2, player1)

                if temp not in self.match_already_done and reverse_temp not in self.match_already_done:
                    round_n.add_match(Match(player1, player1.points, player2, player2.points))
                    self.match_already_done.add(temp)
                    self.match_already_done.add(reverse_temp)
                    players_sorted_by_points.remove(player1)
                    players_sorted_by_points.remove(player2)

                    break

                elif players_sorted_by_points.index(player2) == (len(players_sorted_by_points)-1):
                    round_n.add_match(Match(player1, player1.points, player2, player2.points))
                    self.match_already_done.add(temp)
                    self.match_already_done.add(reverse_temp)
                    players_sorted_by_points.remove(player1)
                    players_sorted_by_points.remove(player2)

                    break

        self.add_rounds(round_n)
