#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    for subdirectory in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, subdirectory)):
            r = subprocess.call(['python', 'mass_static_analysis.py', '-d', os.path.join(directory, subdirectory)])

if __name__ == '__main__':
    main()