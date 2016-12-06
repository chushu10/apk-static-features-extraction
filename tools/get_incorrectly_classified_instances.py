#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, zipfile, argparse, arff

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


def get_size_and_dexsize(path_to_predictions, path_to_arff):
    # read predictions
    f = open(path_to_predictions, 'r')
    content = f.readlines()
    f.close()

    error_index = []
    for line in content:
        if '+' in line:
            error_index.append(int(line.split()[0]))

    # generate error list
    f = open(path_to_arff, 'r')
    file = f.read()
    f.close()

    d = arff.loads(file)

    error_list = []
    i = 0
    for index in error_index:
        obj['data'].append(d['data'][index])
        error_list.append({'size':d['data'][index][0], 'dex_size':d['data'][index][1]})

    # write error vectors to arff
    f = open('incorrectly_classified.arff', 'w')
    arff.dump(obj, f)
    f.close()

    return error_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    error_list = get_size_and_dexsize('./predictions', os.path.join(directory, 'weka_testset.arff'))

    apk_list = []
    for file in os.listdir(directory):
        if ('vir' in file) or ('apk' in file):
            apk_list.append(file)

    f = open('error_apk', 'w')
    error_apk_set = set()
    for error in error_list:
        for apk in apk_list:
            apk_path = os.path.join(directory, apk)
            if (os.path.getsize(apk_path)==error['size']) and (zipfile.ZipFile(apk_path).getinfo('classes.dex').file_size==error['dex_size']):
                if apk not in error_apk_set:
                    f.write(apk + ' ' + str(error['size']) + ' ' + str(error['dex_size']) +'\n')
                    error_apk_set.add(apk)
    f.close()

if __name__ == '__main__':
    main()