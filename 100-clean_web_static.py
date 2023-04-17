#!/usr/bin/python3
""" Delete out of date archive files"""

env.user = "ubuntu"
env.hosts = ["3.94.181.72", "54.173.9.45"]


def do_clean(number=0):
    """
    House Keeping for archived files

    Arguments:
        number: the number of files to delete
    Returns:
        returns nothing
    """

    path = '/data/web_static/releases'

    if number == 0 or number == 1:
        number = 1
    elif number == 2:
        number = 2

    clean_local = 'ls -t versioins | tail -n +{} | xargs rm -rf'.\
        format(number)

    clean_server = "ls -t {}| tail -n +{} | xargs rm -rf".format(
        path, number)

    run(clean_server)
    local(clean_local)
