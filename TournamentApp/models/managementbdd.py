#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB

class ManagementBdd:

    def save_into_db(self, table):
        '''Serialize infos and save into DB'''

        serialized_infos = self.__dict__
        db = TinyDB('db.json')
        table = db.table(table)
        table.insert(serialized_infos)