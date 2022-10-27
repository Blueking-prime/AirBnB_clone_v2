#!/usr/bin/python3
'''compresses webstatic files into a .tgz archive'''

from fabric.api import local


def do_pack():
    '''Pack web_static contents into archive'''
    local('mkdir -p versions')
    arch = local('echo "web_static_$(date +%Y%m%d%H%M%S).tgz"', capture=True)
    result = local('tar -cvzf versions/{} web_static'.format(arch))

    if result.failed:
        return None
    else:
        return 'versions/{}'.format(arch)
