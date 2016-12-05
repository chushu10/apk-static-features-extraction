#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, zipfile, argparse, arff

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
        error_list.append({'size':d['data'][index][0], 'dex_size':d['data'][index][1]})

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