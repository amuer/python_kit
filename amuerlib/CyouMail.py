# -*- coding: UTF-8 -*-
__author__ = 'wangqiang'

import smtplib
from email.mime.text import MIMEText

class CyouMail():

    def __init__(self, user, password, postfix, smtpServer, port):
        self.user = user
        self.password = password
        self.smtpServer = smtpServer
        self.postfix = postfix
        self.port = port

    def sendTo(self, receiver, subject, content):
        me = self.user
        msg = MIMEText(content, _subtype='plain', _charset="utf-8")
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = receiver

        try:
            server = smtplib.SMTP()
            server.connect(self.smtpServer, self.port)
            #server.ehlo()
            #server.starttls()
            #server.ehlo
            server.login(self.user, self.password)
            server.sendmail(me, receiver, msg.as_string())
            server.close()
            return 0
        except Exception, e:
            print e
            return -1