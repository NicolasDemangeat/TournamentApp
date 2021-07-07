#! /usr/bin/env python3
# coding: utf-8

import datetime


class Constraint:
    """This class contains all methods to check input data"""

    def not_empty(self, value):
        self.value = value

        case = self.value.replace(' ', '')

        if len(self.value) == 0 or len(case) == 0:
            return False
        else:
            return True

    def is_integer(self, value):
        self.value = value

        try:
            self.value = int(self.value)
            return True
        except ValueError:
            return False

    def is_float(self, value):
        self.value = value

        try:
            self.value = float(self.value)
            return True
        except ValueError:
            return False

    def is_positiv(self, value):
        try:
            self.value = int(value)
        except ValueError:
            return False

        if self.value < 0:
            return False
        else:
            return True

    def is_date(self, value):
        self.value = value.split('/')

        try:
            day = int(self.value[0])
            month = int(self.value[1])
            year = int(self.value[2])
        except ValueError:
            return False

        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False
