#!/usr/bin/python3
""" Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives """
from fabric.api import *
from datetime import datetime
from os.path import exists


def do_clean(number=0):
    """Function that deletes out-of-date archives"""
