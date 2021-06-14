#! /usr/bin/env python3
# coding: utf-8

class TournamentView:

    def tournament_sequence(self):
        liste_sentences = [
            '\nVeuillez saisir le nom du tournoi : ',
            '\nVeuillez saisir le lieux du tournoi : ',
            '\nVeuillez saisir le nombre de rounds : ',
            '\nVeuillez saisir le style de controle du temps : ',
            '\nVeuillez saisir la description du tournoi : '
        ]

        liste_choices = []

        for sentence in liste_sentences:
            print(sentence)
            liste_choices.append(input('>> '))

        return liste_choices

    def players_sequence(self):
        print('\nCréation des joueurs.')

        liste_sentences = [
            '\nVeuillez saisir le prénom du joueur : ',
            '\nVeuillez saisir le nom du joueur : ',
            '\nVeuillez saisir la date de naissance du joueur : ',
            '\nVeuillez saisir le genre du joueur : ',
            '\nVeuillez saisir le rang du joueur : '
        ]

        liste_choices = []

        for sentence in liste_sentences:
            print(sentence)
            liste_choices.append(input('>> '))
        
        return liste_choices

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

    def matchs_selection(self, tournoi, round_num):
        print('Voici la liste des matchs : ')
        for value in tournoi.rounds[round_num].matchs:
            print(value.get_match)

    def set_players_score(self, tournoi):
        choices = []
        for i, value in enumerate(tournoi.players):
            print(f'Combien de point pour le joueur {value.first_name} : ')
            choices.append(float(input('>> ')))
        
        return choices
    
    def winner_announcement(self, tournoi):
        for i, player in enumerate(tournoi.players):
            print(f'Le numéro {i+1} du tournoi est [{player.first_name}] avec un score de {player.points}')