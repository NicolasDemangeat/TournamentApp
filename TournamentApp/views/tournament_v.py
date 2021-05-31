#! /usr/bin/env python3
# coding: utf-8

class TournamentView:

    def tournament_sequence(self):
        return [
            '\nVeuillez saisir le nom du tournoi : ',
            '\nVeuillez saisir le lieux du tournoi : ',
            '\nVeuillez saisir le nombre de rounds : ',
            '\nVeuillez saisir le style de controle du temps : ',
            '\nVeuillez saisir la description du tournoi : '
        ]

    def players_sequence(self):
        return [
            '\nVeuillez saisir le prénom du joueur : ',
            '\nVeuillez saisir le nom du joueur : ',
            '\nVeuillez saisir la date de naissance du joueur : ',
            '\nVeuillez saisir le genre du joueur : ',
            '\nVeuillez saisir le rang du joueur : '
        ]
    
    def player_continue(self):
        continuer = True
        while continuer:
            print('Voulez vous continuer de créer des joueurs pour ce tournoi ? [o / n]')
            choice = input('>> ')
            if choice.lower() == 'n':
                continuer = False
                return False                
            elif choice.lower() == 'o':
                continuer = False
                return True
