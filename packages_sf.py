#!/usr/bin/env Python
# coding:utf8

"""
1:此脚本运行在目标服务器上
2.运行前需进行两台服务器之间的免密登录设置
"""

import os
import time
from collections import OrderedDict


def delete_file(target_path):
    for key, value in target_path.items():
        os.chdir(value)
        os.system('sudo rm -rf *')


def copy_file(user, host, source_path, target_path):
    try:
        for key, value in source_path.items():
            cmd = 'scp -r %s@%s:/%s* %s' % (user, host, value, target_path[key])
            print(cmd)
            os.system(cmd)
    except Exception as error:
        print(error)


def restart_server():
    restart_cmd = OrderedDict()
    restart_cmd['sys'] = 'sudo ./server_sys.sh restart'
    restart_cmd['knowledge'] = 'sudo ./server_knowledge.sh restart'
    restart_cmd['engine'] = 'sudo ./server_engine.sh restart'

    try:
        os.chdir('/mnt/yysoft/bin/')
        os.system('source /etc/profile')
        for key, value in restart_cmd.items():
            os.system(value)
            print('%s is starting' % (key))
            time.sleep(60)

    except Exception as error:
        print(error)


if __name__ == '__main__':
    source_path = {"web": "/data/web/",
                   'sys': '/data/sys/ext/',
                   'knowledge': '/data/knowledge/ext/',
                   'engine': '/data/engine/ext/'}
    target_path = {"web": "/mnt/yysoft/web/",
                   'sys': '/mnt/yysoft/sys/ext/',
                   'knowledge': '/mnt/yysoft/knowledge/ext/',
                   'engine': '/mnt/yysoft/engine/ext/'}
    user = 'yyuser'
    host = '10.1.1.172'

    print('Delete File》》》》》》》》》》》》》》')
    delete_file(target_path)

    print('Update File》》》》》》》》》》》》》》')
    copy_file(user, host, source_path, target_path)

    print('Restart Server》》》》》》》》》》》》》')
    restart_server()

    print('>>>end>>>')
