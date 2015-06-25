# -*- coding: utf-8 -*-
__author__ = 'wangqiang'

import ConfigParser
import os

class IniConfig():
    def __init__(self, path):
        if os.path.exists(path):
            self.conf = ConfigParser.ConfigParser()
            self.conf.readfp(open(path))
            self.path = path
        else:
            raise IOError

    def getKey(self, type ,key):
        return self.conf.get(type, key)

    def setKey(self, type, key, value):
        self.conf.set(type, key, value)
        self.write()

    def write(self):
        self.conf.write(open(self.path, "w"))
