#!/usr/bin/python3
'''distributes archive to web servers'''

from fabric.api import put, run, env
from os.path import splitext


env.hosts = ['44.210.21.227', '100.25.205.170']


def do_deploy(archive_path):
    '''distributes archive to webservers'''
    if archive_path is None:
        return False
    try:
        put(archive_path, '/tmp/')
        archive_no_ext, ext = splitext(archive_path)
        archive_no_fold = archive_path.replace('versions/', '')
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))
        archive_loc = '/data/web_static/releases/{}/'.format(archive_no_ext)
        run('tar -xzf /tmp/{} -C {}'.format(archive_no_fold, archive_loc))
        run('rm /tmp/{}'.format(archive_no_fold))
        run('mv {}/web_static/* {}'.format(archive_loc, archive_loc))
        run('rm -rf {}/web_static'.format(archive_loc))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(archive_loc))
    except Exception:
        return False
    else:
        return True
