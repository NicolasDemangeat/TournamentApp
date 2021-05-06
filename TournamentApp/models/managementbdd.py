#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB

class ManagementTournoi:

    def save_into_db(self, tournoi, table):
        '''Serialize infos and save into DB'''

        serialized_infos = vars(tournoi)
        db = TinyDB('db.json')
        table = db.table(table)
        table.insert(serialized_infos)