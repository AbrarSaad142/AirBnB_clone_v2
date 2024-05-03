#!/usr/bin/python3
"""This module contains the function do_deploy
that distributes an archive to your web servers"""


from fabric.api import *
from datetime import datetime
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ["52.72.66.73", "34.227.91.227"]


def deploy():
    """creates and distributes an archive to your web servers"""
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result
