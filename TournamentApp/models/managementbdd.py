#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.match import Match
from TournamentApp.models.player import Player
from TournamentApp.models.round import Round
from TournamentApp.models.tournament import Tournament
from tinydb import TinyDB, where, Query


class ManagementDataBase:
    """This class contains all methods for save data into DataBase."""

    def __init__(self):
        self.db = TinyDB('db_echec.json')
        self.tournaments_table = self.db.table('tournaments')
        self.players_table = self.db.table('players')
        self.query = Query()

    def serialize_players(self, player):
        serialize_player = {"first_name": player.first_name,
                            "last_name": player.last_name,
                            "birth_date": player.birth_date,
                            "gender": player.gender,
                            "ranking": player.ranking,
                            "points": player.points}

        return serialize_player

    def serialize_tournament(self, tournament):
        '''Serialize players, rounds and matchs'''
        instances_players = tournament.players
        instances_rounds = tournament.rounds

        dicts_players = []
        dicts_rounds = []
        # serialized players
        for player in instances_players:
            instance = self.serialize_players(player)
            dicts_players.append(instance)
        # serialized rounds
        for round in instances_rounds:
            matchs_list = []
            name = round.name
            start_date = round.start_date
            end_date = round.end_date
            instances_matchs = round.matchs

            # serialized matchs
            for match in instances_matchs:
                player_1 = match.player_1
                player_2 = match.player_2

                serialized_player_1 = self.serialize_players(player_1)
                serialized_player_2 = self.serialize_players(player_2)

                points_p1 = match.points_p1
                points_p2 = match.points_p2

                serialized_match = ([serialized_player_1, f'{points_p1}'],
                                    [serialized_player_2, f'{points_p2}'])

                instance_match = {
                    "match": serialized_match,
                    "player_1": serialized_player_1,
                    "player_2": serialized_player_2,
                    "points_p1": points_p1,
                    "points_p2": points_p2
                    }

                matchs_list.append(instance_match)

            instance_round = {"name": name, "start_date": start_date, "end_date": end_date, "matchs": matchs_list}

            dicts_rounds.append(instance_round)

        tournament_serialized = {
            "name": tournament.name,
            "place": tournament.place,
            "nb_rounds": tournament.nb_rounds,
            "time_control": tournament.time_control,
            "description": tournament.description,
            "date": tournament.date,
            "players_tournament": dicts_players,
            "all_round": dicts_rounds,
            "end_date": tournament.end_date,
            "round_played": tournament.round_played,
            "match_already_done": tournament.match_already_done
            }

        return tournament_serialized

    def save_players(self, player):
        '''check if player exsit and replace him'''

        if self.players_table.search(
                    (where("first_name") == player.first_name) &
                    (where("last_name") == player.last_name) &
                    (where("birth_date") == player.birth_date)):

            serialize_player = self.serialize_players(player)
            self.players_table.remove(
                (where("first_name") == player.first_name) &
                (where("last_name") == player.last_name) &
                (where("birth_date") == player.birth_date))

            self.players_table.insert(serialize_player)
        else:
            serialize_player = self.serialize_players(player)
            self.players_table.insert(serialize_player)

    def save_tournament(self, tournament):
        '''check if tournament exist and replace it'''

        if self.tournaments_table.contains((where("name") == tournament.name) & (
                where("place") == tournament.place) & (
                where("date") == tournament.date) & (
                where("description") == tournament.description)):

            serialize_tournament = self.serialize_tournament(tournament)

            self.tournaments_table.remove((where("name") == tournament.name) & (
                where("place") == tournament.place) & (
                where("date") == tournament.date))

            self.tournaments_table.insert(serialize_tournament)
        else:
            serialize_tournament = self.serialize_tournament(tournament)
            self.tournaments_table.insert(serialize_tournament)

    def load_tournament(self, tournament):
        """Return an instance of tournament"""

        # dict to instance
        name = tournament["name"]
        place = tournament["place"]
        nb_rounds = tournament["nb_rounds"]
        time_control = tournament["time_control"]
        description = tournament["description"]
        date = tournament["date"]
        round_played = tournament["round_played"]
        match_already_done = tournament["match_already_done"]

        tournament_instance = Tournament(name, place, nb_rounds, time_control, description)
        tournament_instance.date = date
        tournament_instance.round_played = round_played
        tournament_instance.match_already_done = match_already_done

        rounds = []

        dict_round = tournament["all_round"]

        for round in dict_round:
            round_instance = Round()
            round_instance.name = round["name"]
            round_instance.start_date = round["start_date"]
            round_instance.end_date = round["end_date"]

            dict_list_matchs = round["matchs"]

            matchs_list = []

            for match in dict_list_matchs:
                # player_1 dict to instance
                first_name_p1 = match["player_1"]['first_name']
                last_name_p1 = match["player_1"]['last_name']
                birth_date_p1 = match["player_1"]['birth_date']
                gender_p1 = match["player_1"]['gender']
                ranking_p1 = match["player_1"]['ranking']
                points_p1 = match["player_1"]['points']
                points_m1 = match["points_p1"]

                # player_2 dict to instance
                first_name_p2 = match["player_2"]['first_name']
                last_name_p2 = match["player_2"]['last_name']
                birth_date_p2 = match["player_2"]['birth_date']
                gender_p2 = match["player_2"]['gender']
                ranking_p2 = match["player_2"]['ranking']
                points_p2 = match["player_2"]['points']
                points_m2 = match["points_p2"]

                player_1 = Player(
                    first_name_p1,
                    last_name_p1,
                    birth_date_p1,
                    gender_p1,
                    ranking_p1,
                    points_p1
                )

                player_2 = Player(
                    first_name_p2,
                    last_name_p2,
                    birth_date_p2,
                    gender_p2,
                    ranking_p2,
                    points_p2
                )

                match = Match(player_1, points_m1, player_2, points_m2)

                matchs_list.append(match)

            # update round instance matchs list attributs
            round_instance.matchs = matchs_list

            # update tournament rounds list attributs
            rounds.append(round_instance)
        tournament_instance.rounds = rounds

        # player list attributs
        list_dict_players_tournament = tournament['players_tournament']
        players_tournament = []

        for player in list_dict_players_tournament:
            first_name = player["first_name"]
            last_name = player["last_name"]
            birth_date = player["birth_date"]
            gender = player["gender"]
            ranking = player["ranking"]
            points = player["points"]

            player_instance = Player(first_name, last_name, birth_date, gender, ranking, points)

            players_tournament.append(player_instance)

        tournament_instance.players = players_tournament

        return tournament_instance

    def load_player(self, player):
        # load a player from dict to instance
        first_name = player["first_name"]
        last_name = player["last_name"]
        birth_date = player["birth_date"]
        gender = player["gender"]
        ranking = player["ranking"]
        points = player["points"]

        player = Player(first_name, last_name, birth_date, gender, ranking, points)

        return player

    def find_player(self, first_name, last_name, birth_date):
        """Check if player exist"""

        if self.players_table.contains((where("first_name") == first_name) & (
                where("last_name") == last_name) & (
                where("birth_date") == birth_date)):
            return True
        else:
            return False

    def rank_update(self, first_name, last_name, birth_date, rank):
        self.players_table.update(
            {'ranking': rank},
            ((where('first_name') == first_name) &
                (where('last_name') == last_name) &
                (where('birth_date') == birth_date)))
