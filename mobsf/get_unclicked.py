#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, requests

def get_url_by_id(id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select URL from MobSF_recentscansdb where id=?', (id,))
    URL = cursor.fetchone()
    cursor.close()
    conn.close()
    return URL[0]

def get_max_id():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select MAX(id) from MobSF_recentscansdb')
    MAX_ID = cursor.fetchone()
    cursor.close()
    conn.close()
    return MAX_ID[0]

def get_report(url, index):
    protocol = 'http://'
    host = '127.0.0.1'
    port = '8000'
    URL = protocol+host+':'+port+'/'+url
    r = requests.get(URL)
    if r.status_code == 200:
        print('Ok', index)

def main():
    for i in range(1, get_max_id() + 1):
        url = get_url_by_id(i)
        get_report(url, i)


if __name__ == '__main__':
    main()