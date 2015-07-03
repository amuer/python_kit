#!/usr/bin/python
#coding=utf-8

import os
import sys
import codecs

class TrimBom:
    
    basePath = ''
    fileList = []
    trimExtList = ['php', 'css', 'js', 'py', 'pl', 'html', 'htm','java']

    #ȥ���ַ����е�bom����
    def trim_bom(self, str):
        if not str:
            return ''
        
        if len(str) < 3:
            return ''
        
        if str[:3] == codecs.BOM_UTF8:
            return str[3:]
        
        return str

    #ȥ��ĳ�ļ���bomͷ
    def trim_file_bom(self, fileName):
        if not fileName:
            return False
        
        if not os.path.exists(fileName):
            return False

        try:
            fp = open(fileName, 'r')
            html_sourse = fp.read()
            fp.close()
        except:
            return False

        html_result = self.trim_bom(html_sourse)

        if html_result == html_sourse:
            return False

        try:
            fp = open(fileName, 'w')
            fp.write(html_result)
            fp.close()
        except:
            return False

        return True

    #��ȡָ�������ļ����б�
    def getFileListByExt(self, path):
        if not path:
            return False

        path = os.path.normpath(path)

        if not os.path.exists(path):
            return False

        if os.path.isfile(path) and path.split('.')[-1] in self.trimExtList:
            trimFlag = self.trim_file_bom(path)

            if trimFlag:
                print ('process %s success...' % path.replace(self.basePath, '').replace('\\', '/'))
            
        elif os.path.isdir(path):
            fileNameList = os.listdir(path)
            for fileName in fileNameList:
                fileName = os.path.normpath('%s/%s' % (path,fileName))
                self.getFileListByExt(fileName)
        
        return False

    #���к������
    def run(self, path):
        self.basePath = os.path.normpath(path)
        self.getFileListByExt(path)

if __name__ == '__main__':
    tObj = TrimBom()
    tObj.run('./src')