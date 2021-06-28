#! /usr/bin/env python3
# coding: utf-8

import os
import sys

BASE_DIR = os.getcwd()
sys.path.append(BASE_DIR)
from TournamentApp.controllers.app import ApplicationController

app = ApplicationController()
app.start()