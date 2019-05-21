# -*- coding:utf-8 -*-
class Config:
    def __init__(self):
        self._appium_hub=None

    @property
    def appium_hub(self):
        return self._appium_hub

    @appium_hub.setter
    def appium_hub(self,appium_hub):
        self._appium_hub=appium_hub
