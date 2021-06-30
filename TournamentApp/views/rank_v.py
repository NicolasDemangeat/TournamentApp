#! /usr/bin/env python3
# coding: utf-8


class UpdateRankingView:

    def get_player_firstname(self):
        print('\n Veuillez saisir le prénom du joueur : ')
        first_name = input('>> ')

        return first_name

    def get_player_lastname(self):
        print('\nVeuillez saisir le nom de famille du joueur : ')
        last_name = input('>> ')

        return last_name

    def gat_player_birth_date(self):
        print('\nVeuillez saisir la date de naissance du joueur : ')
        birth_date = input('>> ')

        return birth_date

    def dont_exist(self):
        print("\n! ERREUR ! Ce joueur n'est pas dans la base de donnée.")
        print('Veuillez recommencer.')

    def new_rank(self):
        print("\nQuel est le nouveau calssement du joueur ?")
        rank = input('>> ')

        return rank

    def end_update(self):
        print('\nLe classement du joueur à bien été mis à jour.')
        print("Voulez-vous mettre à jour le classement d'un autre joueur ? ['o' ou 'n'] ")
        yes_or_no = input('>> ')

        return yes_or_no
