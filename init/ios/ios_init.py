#-*- coding:utf8 -*-
from init.ios.demoPorject.demoProjectInit import DemoProjectInit

import configparser as ConfigParser

def ios_init():
    """
    初始化ios项目必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/ios/ios_init.conf',encoding='utf-8')

    if 1==int(config.get('isInit','demoProject')):
        DemoProjectInit().init()