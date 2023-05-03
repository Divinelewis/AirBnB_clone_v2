#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """This script generates an archive of the contents of web_static folder"""

    name_of_file = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(name_of_file))

        return "versions/web_static_{}.tgz".format(name_of_file)

    except Exception as e:
        return None
