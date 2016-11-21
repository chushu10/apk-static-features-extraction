#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sqlite3, argparse, re, json

def get_max_id(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('select MAX(id) from StaticAnalyzer_staticanalyzerandroid')
    MAX_ID = cursor.fetchone()
    cursor.close()
    conn.close()
    return MAX_ID[0]

def get_cert_info(id, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('select CERT_INFO, APP_NAME from StaticAnalyzer_staticanalyzerandroid where id = %d' % id)
    CERT_INFO = cursor.fetchone()
    cursor.close()
    conn.close()
    if CERT_INFO is None:
        return '', ''
    m = re.search('SerialNumber: \[(.+?)\]', CERT_INFO[0])
    if m:
        return m.group(1).strip(), CERT_INFO[1]
    else:
        return '', CERT_INFO[1]

def get_serial_name_dict(serial_set, serial_name, database_path):
    MAX_ID = get_max_id(database_path)
    for i in range(1, MAX_ID + 1):
        SerialNumber, APP_NAME = get_cert_info(i, database_path)
        if SerialNumber == '' or APP_NAME == '':
            continue
        print('Scanning app %d' % i)
        if SerialNumber not in serial_set:
            serial_set.add(SerialNumber)
            serial_name[SerialNumber] = dict(appnames=[])
            serial_name[SerialNumber]['appnames'].append(APP_NAME)
        else:
            serial_name[SerialNumber]['appnames'].append(APP_NAME)
    return serial_name, MAX_ID

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    # get data
    serial_set = set()
    serial_name = {}
    TOTAL = 0
    database_path = os.path.join(directory, 'db.sqlite3')
    if os.path.isfile(database_path):
        serial_name, MAX_ID = get_serial_name_dict(serial_set, serial_name, database_path)
        TOTAL += MAX_ID
    else:
        for folder in os.listdir(directory):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):
                print('Start scanning folder %s\n' % folder)
                database_path = os.path.join(folder_path, 'db.sqlite3')
                serial_name, MAX_ID = get_serial_name_dict(serial_set, serial_name, database_path)
                TOTAL += MAX_ID

    print('%d serial number sign %d apps' % (len(serial_name), TOTAL))

    f = open(os.path.join(directory, 'serial_name.json'), 'w')
    json.dump(serial_name, f)
    f.close()

if __name__ == '__main__':
    main()