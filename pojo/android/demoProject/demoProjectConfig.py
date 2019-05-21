# -*- coding:utf-8 -*-
class DemoProjectConfig:
    def __init__(self):
        self._platformName = None
        self._automationName = None
        self._platformVersion = None
        self._deviceName = None
        self._appActivity = None
        self._appPackage = None
        self._app = None

    @property
    def platformName(self):
        return self._platformName

    @platformName.setter
    def platformName(self,platformName):
        self._platformName=platformName

    @property
    def automationName(self):
        return self._automationName

    @automationName.setter
    def automationName(self,automationName):
        self._automationName=automationName

    @property
    def platformVersion(self):
        return self._platformVersion

    @platformVersion.setter
    def platformVersion(self,platformVersion):
        self._platformVersion=platformVersion

    @property
    def deviceName(self):
        return self._deviceName

    @deviceName.setter
    def deviceName(self,deviceName):
        self._deviceName=deviceName

    @property
    def appActivity(self):
        return self._appActivity

    @appActivity.setter
    def appActivity(self,appActivity):
        self._appActivity=appActivity

    @property
    def appPackage(self):
        return self._appPackage

    @appPackage.setter
    def appPackage(self,appPackage):
        self._appPackage=appPackage

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self,app):
        self._app=app

    def get_desired_capabilities(self):
        desired_capabilities={}
        desired_capabilities.update({'platformName':self._platformName})
        if self._automationName:
            desired_capabilities.update({'automationName':self._automationName})
        desired_capabilities.update({'platformVersion':self._platformVersion})
        desired_capabilities.update({'deviceName':self._deviceName})
        if self._appActivity and self._appPackage:
            desired_capabilities.update({'appActivity':self._appActivity})
            desired_capabilities.update({'appPackage':self._appPackage})
        if self._app:
            desired_capabilities.update({'app':self._app})
        return desired_capabilities