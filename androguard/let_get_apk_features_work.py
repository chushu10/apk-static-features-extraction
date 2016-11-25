#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    parser.add_argument('-s', '--security', help='benign(0) or malware(-1)')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()
    if args.security:
        security = args.security
    else:
        parser.print_help()

    for subdirectory in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, subdirectory)):
            r = subprocess.call(['python', 'get_apk_features.py', '-d', os.path.join(directory, subdirectory), '-s', security])

if __name__ == '__main__':
    main()