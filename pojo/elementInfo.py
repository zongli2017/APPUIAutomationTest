#-*- coding:utf8 -*-

class ElementInfo:
    def __init__(self):
        self._locator_type=None
        self._locator_value=None
        self._expected_value=None
        self._wait_type=None
        self._wait_seconds=None
        self._wait_expected_value=None

    @property
    def expected_value(self):
        return self._expected_value

    @expected_value.setter
    def expected_value(self,expected_value):
        self._expected_value=expected_value

    @property
    def locator_type(self):
        return self._locator_type

    @locator_type.setter
    def locator_type(self,locator_type):
        self._locator_type=locator_type

    @property
    def locator_value(self):
        return self._locator_value

    @locator_value.setter
    def locator_value(self,locator_value):
        self._locator_value=locator_value

    @property
    def wait_type(self):
        return self._wait_type

    @wait_type.setter
    def wait_type(self,wait_type):
        self._wait_type=wait_type

    @property
    def wait_seconds(self):
        return self._wait_seconds

    @wait_seconds.setter
    def wait_seconds(self,wait_seconds):
        self._wait_seconds=wait_seconds

    @property
    def wait_expected_value(self):
        return self._wait_expected_value

    @wait_expected_value.setter
    def wait_expected_value(self,wait_expected_value):
        self._wait_expected_value=wait_expected_value