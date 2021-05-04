#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.tournament import Tournament
from TournamentApp.models.player import Player

tournoi = Tournament('tournoi', 'ici', 4, 'bullet', 'rien de précis')
tournoi.save_into_db('tournoi')