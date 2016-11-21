#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, re, json, argparse, os
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__tagname = ''
        self.__permissions = []

    def handle_starttag(self, tag, attrs):
        self.__tagname = tag

    def handle_data(self, data):
        if self.__tagname == 'td':
            if re.match(r'android.permission.*', data):
                self.__permissions.append(data)

    def get_permissions(self):
        return self.__permissions;
        

def get_permissions(family, id):
    conn = sqlite3.connect('db/'+family+'/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select APP_NAME, PERMISSIONS from StaticAnalyzer_staticanalyzerandroid where id=?', (id,))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(values) != 0:
        return values[0]

def get_max_id(family):
    conn = sqlite3.connect('db/'+family+'/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select MAX(id) from StaticAnalyzer_staticanalyzerandroid')
    MAX_ID = cursor.fetchone()
    cursor.close()
    conn.close()
    return MAX_ID[0]

def main():
    # receive directory from cli
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--family', help='name of the malware family')
    args = parser.parse_args()
    if args.family:
        family = args.family
    else:
        parser.print_help()

    # get permissions from db and dump to json
    f = open('db/'+family+'/permissions.json', 'w')
    apk_list = {}
    count = 1
    for i in range(1, get_max_id(family) + 1):
        if get_permissions(family, i) is not None:
            print('scanning %d apk' % count)
            count += 1
            APP_NAME, HTMLText = get_permissions(family, i)
        else:
            continue
        parser = MyHTMLParser()
        parser.feed(HTMLText)
        permission_list = parser.get_permissions()
        d = dict(permissions=permission_list)
        apk_list[APP_NAME] = d
    json.dump(apk_list, f)
    f.close()

if __name__ == '__main__':
    main()
