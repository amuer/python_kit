# -*- coding: utf-8 -*-
__author__ = 'wangqiang'

import zipfile
import os

def comparess(dir, zipFileName):
    filelist = []
    if os.path.isfile(dir):
        filelist.append(dir)
    else:
        for root, dirs, files in os.walk(dir):
            for name in files:
                filelist.append(os.path.join(root, name))

    zipFile = zipfile.ZipFile(zipFileName, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dir):]
        zipFile.write(tar, arcname)
    zipFile.close()

def removeZipFile(zipFile):
    if os.path.exists(zipFile):
        os.remove(zipFile)

def comparessWith7z(dir, zipFileName, password):
    if os.path.isdir(dir):
        removeZipFile(zipFileName)
        cmd = "7z" + " " + "a" + " " + zipFileName + " " + dir + " " + "-p" + password
        print cmd
        os.system(cmd)
