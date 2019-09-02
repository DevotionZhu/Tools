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
        os.system('rm -rf *')


def copy_file(user, host, source_path, target_path):
    try:
        for key, value in source_path.items():
            cmd = 'scp -r %s@%s:/%s* %s' % (user, host, value, target_path[key])
            print(cmd)
            os.system(cmd)
    except Exception as error:
        print(error.message)


def restart_server():
    restart_cmd = OrderedDict()
    restart_cmd['sys'] = './server_sys.sh restart systemcenter'
    restart_cmd['knowledge'] = './server_knowledge.sh restart'
    restart_cmd['engine'] = './server_engine.sh restart'
    restart_cmd['med'] = './server_med.sh restart all'
    restart_cmd['report'] = './server_report.sh restart'

    try:
        os.chdir('/mnt/yiyao/bin/')
        for key, value in restart_cmd.items():
            os.system(value)
            print('%s is starting' % (key))
            time.sleep(60)

        pid = os.popen("ps -ef|grep soft/tomcat8|grep -v grep|awk '{print$2}'").readlines()
        print(pid)
        if pid:
            cmd = 'kill -9 %s' % pid[0]
            print(cmd)
            os.system(cmd)
            time.sleep(5)
        os.chdir('/mnt/yiyao/soft/tomcat8/bin')
        os.system('source /etc/profile')
        time.sleep(5)
        os.system('./startup.sh')


    except Exception as error:
        print(error.message)


if __name__ == '__main__':
    source_path = {"web": "/mnt/yiyao/web/",
                   "webapps": '/mnt/yiyao/soft/tomcat/webapps/',
                   'sys': '/mnt/yiyao/sys/ext/',
                   'knowledge': '/mnt/yiyao/knowledge/ext/',
                   'engine': '/mnt/yiyao/engine/ext/'}
    target_path = {"web": "/mnt/yyspace/web/",
                   "webapps": '/mnt/yyspace/soft/tomcat8/webapps/',
                   'sys': '/mnt/yyspace/sys/ext/',
                   'knowledge': '/mnt/yyspace/knowledge/ext/',
                   'engine': '/mnt/yyspace/engine/ext/'}
    user = 'caoq'
    host = '10.1.1.89'

    print('Delete File》》》》》》》》》》》》》》')
    delete_file(target_path)

    print('Update File》》》》》》》》》》》》》》')
    copy_file(user, host, source_path, target_path)

    print('Restart Server》》》》》》》》》》》》》')
    restart_server()

    print('>>>end>>>')
