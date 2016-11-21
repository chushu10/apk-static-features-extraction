# coding:utf-8

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class DownloadLinkParser(HTMLParser):
    '''Parse the download page of anruan.com, get donwload urls'''
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.downloadlink = []

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and len(attrs) >= 1:
            if attrs[0][1] == 'down_btn undis':
                self.recording = True
                return

        if tag == 'a' and self.recording:
            self.downloadlink.append(attrs[0][1])

    def handle_endtag(self, tag):
        if tag == 'div' and self.recording:
            self.recording = False

    def get_download_link(self):
        return self.downloadlink

class AppNameParser(HTMLParser):
    '''Parse the download page of anruan.com, get app names
       the encoding type of anruan.com is gbk, so we have to
       decode the app names using gbk and encode it with utf-8'''
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.appname = []

    def handle_starttag(self, tag, attrs):
        if tag == 'li' and len(attrs) >= 1:
            if attrs[0][1] == 'recent':
                self.recording = True
                return

        if tag == 'img' and self.recording:
            self.appname.append(attrs[0][1].decode('gbk').encode('utf-8'))

    def handle_endtag(self, tag):
        if tag == 'a' and self.recording:
            self.recording = False

    def get_app_name(self):
        return self.appname