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

def blacklist_match(blacklist, database_path):
    malware_list = []
    benign_list = []
    for i in range(1, get_max_id(database_path) + 1):
        SerialNumber, APP_NAME = get_cert_info(i, database_path)
        if SerialNumber == '' or APP_NAME == '':
            continue
        print('Scanning app %d' % i)
        if SerialNumber in blacklist:
            malware_list.append(APP_NAME)
        else:
            benign_list.append(APP_NAME)
    return malware_list, benign_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    # load malware sn
    f = open('malware_sn.json', 'r')
    blacklist = json.load(f)
    f.close()

    blacklist.remove('936eacbe 07f201df')
    #blacklist.remove('70114e4d')

    # get data
    malware_list = []
    benign_list = []

    for folder in os.listdir(directory):
        print('Start scanning %s:\n' % folder)
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            database_path = os.path.join(folder_path, 'db.sqlite3')
            if os.path.isfile(database_path):
                m_list, b_list = blacklist_match(blacklist, database_path)
                malware_list = malware_list + m_list
                benign_list = benign_list + b_list
            else:
                for sub_folder in os.listdir(folder_path):
                    sub_folder_path = os.path.join(folder_path, sub_folder)
                    if os.path.isdir(sub_folder_path):
                        sub_database_path = os.path.join(sub_folder_path, 'db.sqlite3')
                        m_list, b_list = blacklist_match(blacklist, sub_database_path)
                        malware_list = malware_list + m_list
                        benign_list = benign_list + b_list

    print('%d malwares.' % len(malware_list))
    print('%d benign apps.' % len(benign_list))

if __name__ == '__main__':
    main()