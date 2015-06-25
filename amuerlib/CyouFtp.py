# -*- coding: utf-8 -*-
__author__ = 'wangqiang'

import ftplib
import CheckSth
import os

class CyouFtp():
    def __init__(self, configMap):
        CheckSth.checkDicValue(configMap)
        self.ip = configMap["ip"]
        self.port = configMap["port"]
        self.user = configMap["user"]
        self.password = configMap["password"]
        self.ftp = ftplib.FTP()

    def __del__(self):
        self.ftp.close()

    def connectServer(self):
        try:
            # 最后一个参数是连接的超时时间
            self.ftp.connect(self.ip, self.port, 30)
            self.ftp.login(self.user, self.password)
            return 0
        except Exception:
            return -1

    def closeServer(self):
        pass

    def mkdir(self):
        pass

    def uploadFile(self, srcFile, dstPath, dstFileName):
        if not os.path.isfile(srcFile):
            return -1

        dstFileAbsPath = os.path.join(dstPath, dstFileName)

        try:
            self.ftp.delete(dstFileAbsPath)
            self.ftp.rmd(dstPath)
        except Exception, e:
            pass

        try:
            self.ftp.mkd(dstPath)
        except Exception, e:
            return -2

        localFile = open(srcFile, "rb")
        self.ftp.storbinary('STOR %s' % dstFileAbsPath, localFile)
        localFile.close()
        return 0

