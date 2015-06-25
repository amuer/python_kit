# -*- coding: utf-8 -*-
__author__ = 'wangqiang'
import random

def GeneratePasswd():
    codeList = ""
    while True:
        code = random.randint(0, 94) + 33
        _code = chr(code)
        if (_code >= 'a' and _code <= 'z' and _code != 'o' and _code != 'l' and _code != 'i') \
                or (_code >= 'A' and _code <= 'Z' and _code != 'O' and _code != 'I' and _code != 'L') \
                or (_code > '1' and _code <= '9'):
            codeList += _code
            if len(codeList) >= 12:
                return codeList
