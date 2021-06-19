#! /usr/bin/env python3
# coding: utf-8

class TournamentView:

    def tournament_sequence(self):
        sentences = [
            '\nVeuillez saisir le nom du tournoi : ',
            '\nVeuillez saisir le lieux du tournoi : ',
            '\nVeuillez saisir le nombre de rounds : ',
            '\nVeuillez saisir le style de controle du temps : ',
            '\nVeuillez saisir la description du tournoi : '
        ]

        choices = []

        for sentence in sentences:
            print(sentence)
            choices.append(input('>> '))

        return choices

    def players_sequence(self):
        print('\nCréation des joueurs.')

        sentences = [
            '\nVeuillez saisir le prénom du joueur : ',
            '\nVeuillez saisir le nom du joueur : ',
            '\nVeuillez saisir la date de naissance du joueur : ',
            '\nVeuillez saisir le genre du joueur : ',
            '\nVeuillez saisir le rang du joueur : '
        ]

        choices = []

        for sentence in sentences:
            print(sentence)
            choices.append(input('>> '))

        return choices

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

    def set_players_score(self, tournoi, round_num):
        print('Voici la liste des matchs : ')
        for match in tournoi.rounds[round_num].matchs:
            print(match.get_match)

        choices = {}

        for match in tournoi.rounds[round_num].matchs:
            for player in match.get_players:
                while True:
                    print(f'Combien de point pour le joueur {player.first_name} : ')
                    try:
                        choices[player] = float(input('>> '))
                        break
                    except ValueError:
                        print('Un chiffre est attendu, veuillez réessayer.')

        return choices
    
    def winner_announcement(self, tournoi):
        for i, player in enumerate(sorted(tournoi.players, key=lambda x: (x.points, x.ranking), reverse=True)):
            print(f'Le numéro {i+1} du tournoi est [{player.first_name}] avec un score de {player.points}')