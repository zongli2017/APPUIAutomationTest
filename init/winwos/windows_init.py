#-*- coding:utf8 -*-
from init.winwos.demoPorject.demoProjectInit import DemoProjectInit

import configparser as ConfigParser

def windows_init():
    """
    初始化Windows必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/windows/windows_init.conf',encoding='utf-8')

    if 1==int(config.get('isInit','demoProject')):
        DemoProjectInit().init()