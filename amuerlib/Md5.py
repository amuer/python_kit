# -*- coding: utf-8 -*-
__author__ = 'wangqiang'

import hashlib

def GenerateFilMD5(file):
    f = open(file, "rb")
    m = hashlib.md5()
    while True:
        fileContent = f.read(1024)
        if not fileContent:
            break
        m.update(fileContent)
    return m.hexdigest().lower()

