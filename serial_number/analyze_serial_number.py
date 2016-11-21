#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    serial_set = set()
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            json_path = os.path.join(folder_path, 'serial_name.json')
            f = open(json_path, 'r')
            serial_name = json.load(f)
            f.close()
            for sn in serial_name:
                serial_set.add(sn)

    print(len(serial_set))

    serial_list = []
    for sn in serial_set:
        serial_list.append(sn)

    f = open('benign_sn.json', 'w')
    json.dump(serial_list, f)
    f.close()


if __name__ == '__main__':
    main()