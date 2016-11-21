#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='path of the directory')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    filename_list = []
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1] == '.apk':
            filename_list.append(filename_list)

    f = open('filename_list.json', 'w')
    json.dump(filename_list, f)
    f.close()

if __name__ == '__main__':
    main()