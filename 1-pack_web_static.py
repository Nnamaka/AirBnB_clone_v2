#!/usr/bin/python3
"""
This is python script that archives the content of the web_static
folder in  a '.tgz' format.
"""

from datetime import datetime
from fabric.api import local

# get the current time
now = datetime.now()

# time string format
formatt = "%Y%m%d%H%M%S"

archive_path = "versions/" + "web_static_" + now.strftime(formatt) + ".tgz"
print("Archive path is {}".format(archive_path))


def do_pack():
    """ Compresses the web_static folder """
    command = "mkdir -p versions && tar -czvf {} web_static/"
    .format(archive_path)
    result = local(command)

    if result.failed:
        print(result)
        return None

    return archive_path
