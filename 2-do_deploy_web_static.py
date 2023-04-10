#!/usr/bin/python3
"""
A python script that distributes an archive
on a webserver(s)
"""

from fabric.api import local, run, env, put
import os

# define fab enviroment variables
env.user = "ubuntu"
env.hosts = "3.94.181.72"


def do_deploy(arc_path):
    """ Upload archive to server """
    if not os.path.exists(arc_path):
        print("no deployment")
        return False
    else:
        # upload archive to tmp directory
        put(arc_path, "/tmp/")
        print("failded here")
        arc_dest = "/data/web_static/releases/" + \
            arc_path[9:-4]
        print("failed 2here")
        run("sudo mkdir -p {} && sudo tar -xzvf {} \
            -C {}/".format(arc_dest, "/tmp/"+arc_path[9:], arc_dest))

        # remove the archive from the temp folder
        run("sudo rm {}".format("/tmp/"+arc_path[9:]))

        # delete the symbolic link
        run("sudo mv {}/web_static/* {}".format(arc_dest,
            arc_dest))
        run("sudo rm -rf {}/web_static".format(arc_dest))
        run("sudo rm -rf /data/web_static/current")

        # create symbolic link
        run("sudo ln -s {} /data/web_static/current".format(
            arc_dest))
        return True
