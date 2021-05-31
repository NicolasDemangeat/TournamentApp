#! /usr/bin/env python3
# coding: utf-8

class RapportMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print('Veuillez choisir une option en entrant le chiffre correspondant.')        
        for key, entry in self.menu.items():
            print(f'{key} : {entry.option}')
        print()

    def get_user_choice(self):
        while True:
            self._display_menu()            
            choice = input('>> ')
            if choice in self.menu:
                return self.menu[choice]