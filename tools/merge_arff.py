#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arff, os, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    parser.add_argument('-m', '--mode', help='merge mode(0=merge by folders, 1=merge two arff files')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()
    if args.mode:
        mode = args.mode
    else:
        parser.print_help()

    obj = {
            'description': u'',
            'relation': 'testset',
            'attributes': [
                ('apk_size', 'REAL'),
                ('dex_size', 'REAL'),
                ('min_andrversion', 'INTEGER'),
                ('max_andrversion', 'INTEGER'),
                ('target_andrversion', 'INTEGER'),
                ('security', ['-1','0']),
                ('methodCount', 'INTEGER'),
                ('classCount', 'INTEGER'),
                ('crypto_count', 'INTEGER'),
                ('dynCode_count', 'INTEGER'),
                ('native_count', 'INTEGER'),
                ('reflect_count', 'INTEGER'),
                ('sendSMS', ['1', '0']),
                ('deleteSMS', ['1', '0']),
                ('interruptSMS', ['1', '0']),
                ('httpPost', ['1', '0']),
                ('deviceId', ['1', '0']),
                ('simCountry', ['1', '0']),
                ('installedPkg', ['1', '0']),
                ('loadOtherCode', ['1', '0']),
                ('subprocess', ['1', '0']),
                ('executeOtherCode', ['1', '0']),
                ('jni', ['1', '0']),
                ('unix', ['1', '0']),
                ('buttonCount', 'INTEGER'),
                ('TextViewCount', 'INTEGER'),
                ('EditViewCount', 'INTEGER'),
                ('ImageButtonCount', 'INTEGER'),
                ('CheckBoxCount', 'INTEGER'),
                ('RadioGroupCount', 'INTEGER'),
                ('RadioButtonCount', 'INTEGER'),
                ('ToastCount', 'INTEGER'),
                ('SpinnerCount', 'INTEGER'),
                ('ListViewCount', 'INTEGER'),
                ('fileCount', 'INTEGER'),
                ('INTERNET', ['1', '0']),
                ('SET_DEBUG_APP', ['1', '0']),
                ('MODIFY_PHONE_STATE', ['1', '0']),
                ('RECORD_AUDIO', ['1', '0']),
                ('RECEIVE_BOOT_COMPLETED', ['1', '0']),
                ('RECEIVE_MMS', ['1', '0']),
                ('RECEIVE_SMS', ['1', '0']),
                ('RECEIVE_WAP_PUSH', ['1', '0']),
                ('SEND_SMS', ['1', '0']),
                ('CALL_PHONE', ['1', '0']),
                ('CALL_PRIVILEGED', ['1', '0']),
                ('PROCESS_OUTGOING_CALLS', ['1', '0']),
                ('READ_CALL_LOG', ['1', '0']),
                ('READ_EXTERNAL_STORAGE', ['1', '0']),
                ('READ_LOGS', ['1', '0']),
                ('ACCESS_COARSE_LOCATION', ['1', '0']),
                ('ACCESS_FINE_LOCATION', ['1', '0']),
                ('BLUETOOTH', ['1', '0']),
                ('CAMERA', ['1', '0']),
                ('INSTALL_PACKAGES', ['1', '0']),
                ('NFC', ['1', '0']),
                ('READ_CONTACTS', ['1', '0']),
                ('permissionCount', 'INTEGER'),
                ('activityCount', 'INTEGER'),
                ('serviceCount', 'INTEGER'),
                ('receiverCount', 'INTEGER'),
                ('providerCount', 'INTEGER'),
                ('exportedCount', 'INTEGER'),
                ('hPictureCount', 'INTEGER'),
                ('mPictureCount', 'INTEGER'),
                ('lPictureCount', 'INTEGER'),
                ('xPictureCount', 'INTEGER'),
                ('totalCount', 'INTEGER'),
            ],
            'data': [],
        }

    #size = {
    #    'anquan': 15,
    #    'ditu': 11,
    #    'liaotian': 12,
    #    'meihua': 298,
    #    'paishe': 39,
    #    'richeng': 67,
    #    'shangwu': 24,
    #    'shiyong': 192,
    #    'tongxun': 50,
    #    'tuxiang': 43,
    #    'wangluo': 77,
    #    'xitong': 295,
    #    'xuexi': 33,
    #    'yingyin': 60,
    #    'yuedu': 27,
    #}

    # Part 1: merge arff by folders
    if mode == '0':
        for folder in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, folder)):
                print 'Merging ' + folder
                f = open(os.path.join(os.path.join(directory, folder), 'weka_testset.arff'), 'r')
                file = f.read()
                f.close()

                d = arff.loads(file)
                i = 0
                for data in d['data']:
                    # if you want to shrink the dataset, uncomment two lines below
                    #if i == size[folder]:
                    #    break
                    obj['data'].append(data)
                    i += 1

        f = open(os.path.join(directory, 'weka_testset.arff'), 'w')
        arff.dump(obj, f)
        f.close()

    # Part 2: merge two arff files
    if mode == '1':
        f1 = open(os.path.join(directory, 'weka_testset_1.arff'), 'r')
        file1 = f1.read()
        f1.close()

        f2 = open(os.path.join(directory, 'weka_testset_2.arff'), 'r')
        file2 = f2.read()
        f2.close()

        d1 = arff.loads(file1)
        d2 = arff.loads(file2)

        for data in d1['data']:
            obj['data'].append(data)
        for data in d2['data']:
            obj['data'].append(data)

        f = open(os.path.join(directory, 'weka_testset.arff'), 'w')
        arff.dump(obj, f)
        f.close()

if __name__ == '__main__':
    main()