#!/usr/bin/python3
""" Delete out of date archive files"""

env.user = "ubuntu"
env.hosts = ["3.94.181.72", "54.173.9.45"]


def do_clean(number=0):
    """ Remove archived files """

    path = '/data/web_static/releases'

    number = 2 if number == 0 else number + 1

    clean_local = 'ls -t versions | tail -n +{} | xargs rm -rf'.\
        format(number)

    clean_server = "ls -t {}| tail -n +{} | xargs rm -rf".format(
        path, number)

    run(clean_server)
    local(clean_local)
