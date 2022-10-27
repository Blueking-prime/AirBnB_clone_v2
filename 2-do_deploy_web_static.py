#!/usr/bin/python3
'''distributes archive to web servers'''
from fabric.api import local, put, run, env
from os.path import splitext


env.hosts = ['44.210.21.227', '100.25.205.170']


def do_deploy(archive_path):
    '''distributes archive to webservers'''
    if archive_path is None:
        return False
    try:
        put(archive_path, '/tmp/')
        archive_no_ext, ext = splitext(archive_path)
        archive_no_fold = archive_path.removeprefix('versions/')
        run(f'mkdir -p /data/web_static/releases/{archive_no_ext}/')
        archive_location = f'/data/web_static/releases/{archive_no_ext}/'
        run(f'tar -xzf /tmp/{archive_no_fold} -C {archive_location}')
        run(f'rm /tmp/{archive_no_fold}')
        run(f'mv {archive_location}/web_static/* {archive_location}')
        run(f'rm -rf {archive_location}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {archive_location} /data/web_static/current')
    except Exception:
        return False
    else:
        return True
