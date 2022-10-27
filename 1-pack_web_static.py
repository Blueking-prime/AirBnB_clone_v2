#!/usr/bin/python3
'''compresses webstatic files into a .tgz archive'''
from fabric.api import local


def do_pack():
    '''Pack web_static contents into archive'''

    local('mkdir -p versions')
    arch = local('echo "web_static_$(date +%Y%m%d%H%M%S).tgz"', capture=True)
    result = local(f'tar -cvzf versions/{arch} web_static')
    if result.failed:
        return None
    else:
        return f'versions/{arch}'
