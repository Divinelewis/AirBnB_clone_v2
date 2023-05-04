#!/usr/bin/python3
"""A script to compress web_static packages
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['52.91.145.188', '100.25.137.235']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
        """for deploying Deploy web files to server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # To upload archive
                put(archive_path, '/tmp/')

                # To create target dir
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # To uncompress archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # To remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # To move contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # To remove extraneous web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                # To delete pre-existing sym link
                run('sudo rm -rf /data/web_static/current')

                # To re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # return True on success
        return True
