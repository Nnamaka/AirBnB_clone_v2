#!/usr/bin/python3
""" Delete out of date archive files"""
from fabric.api import env, local, run

env.user = "ubuntu"
env.hosts = ["3.94.181.72", "54.173.9.45"]


def do_clean(number=0):
    """ Remove archived files """

    path = '/data/web_static/releases'

    number = 2 if number == 0 else number + 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))

    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
