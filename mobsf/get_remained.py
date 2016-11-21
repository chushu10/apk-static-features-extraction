#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, os, argparse, shutil

def get_max_id(table):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select MAX(id) from ' + table)
    MAX_ID = cursor.fetchone()
    cursor.close()
    conn.close()
    return MAX_ID[0]

def get_name_list(table, column):
    name_list = []
    size = get_max_id(table)
    for id in range(1, size + 1):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('select ' + column + ' from ' + table + ' where id=?', (id,))
        value = cursor.fetchone()
        cursor.close()
        conn.close()
        if value is not None:
            name_list.append(value[0])
    return name_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()
    '''if there are some apks remain unanalyzed, use this sql to import from external db
    insert into StaticAnalyzer_staticanalyzerandroid(TITLE,APP_NAME,SIZE,MD5,SHA1,SHA256,
    PACKAGENAME,MAINACTIVITY,TARGET_SDK,MAX_SDK,MIN_SDK,ANDROVERNAME,ANDROVER,MANIFEST_ANAL,
    PERMISSIONS,FILES,CERTZ,ACTIVITIES,RECEIVERS,PROVIDERS,SERVICES,LIBRARIES,CNT_ACT,
    CNT_PRO,CNT_SER,CNT_BRO,CERT_INFO,ISSUED,NATIVE,DYNAMIC,REFLECT,CRYPTO,OBFUS,API,DANG,
    URLS,DOMAINS,EMAILS,STRINGS,ZIPPED,MANI,EXPORTED_ACT,E_ACT,E_SER,E_BRO,E_CNT)
     select TITLE,APP_NAME,SIZE,MD5,SHA1,SHA256,PACKAGENAME,MAINACTIVITY,TARGET_SDK,MAX_SDK,
     MIN_SDK,ANDROVERNAME,ANDROVER,MANIFEST_ANAL,PERMISSIONS,FILES,CERTZ,ACTIVITIES,RECEIVERS,
     PROVIDERS,SERVICES,LIBRARIES,CNT_ACT,CNT_PRO,CNT_SER,CNT_BRO,CERT_INFO,ISSUED,NATIVE,
     DYNAMIC,REFLECT,CRYPTO,OBFUS,API,DANG,URLS,DOMAINS,EMAILS,STRINGS,ZIPPED,MANI,
     EXPORTED_ACT,E_ACT,E_SER,E_BRO,E_CNT from remained.StaticAnalyzer_staticanalyzerandroid;'''
    recent_list = get_name_list('MobSF_recentscansdb', 'NAME')
    analyze_list = get_name_list('StaticAnalyzer_staticanalyzerandroid', 'APP_NAME')
    remained_list = []
    count = 0
    for filename in recent_list:
        if filename not in analyze_list:
            remained_list.append(filename)
            print(filename)
            count += 1
    print('%d apks remain unanalyzed' % count)

    print('\napks that are not uploaded:')
    # Compare recent_list with directory_list
    directory_list = os.listdir(directory)
    for filename in directory_list:
        if filename not in recent_list:
            if not os.path.isdir(os.path.join(directory, filename)):
                print(filename)

    print('\n')
    # Move file to directory cannot_be_analyzed
    for filename in remained_list:
        source = os.path.join(directory, filename)
        destination = os.path.join(os.path.join(directory, 'cannot_be_analyzed'), filename)
        shutil.move(source, destination)

    # Repeat apk
    count = 0
    for filename in analyze_list:
        occur_times = 0
        for i in range(0, len(analyze_list)):
            if filename == analyze_list[i]:
                occur_times += 1
        if occur_times >= 2:
            count += 1
            print('%s repeated' % filename)
    print('%d apks repeated' % count)

if __name__ == '__main__':
    main()