#-*- coding:utf8 -*-
from init.android.demoProject.demoProjectInit import DemoProjectInit

import configparser as ConfigParser

def android_init():
    """
    初始化android项目必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/android/android_init.conf',encoding='utf-8')

    if 1==int(config.get('isInit','demoProject')):
        DemoProjectInit().init()
