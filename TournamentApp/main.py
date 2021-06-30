#! /usr/bin/env python3
# coding: utf-8
from TournamentApp.controllers.app import ApplicationController
import os
import sys
BASE_DIR = os.getcwd()
sys.path.append(BASE_DIR)

app = ApplicationController()
app.start()
