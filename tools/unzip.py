#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, os, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    for filename in os.listdir(directory):
        print os.path.join(directory, filename)
        if os.path.splitext(filename)[1] == '.7z':
            r = subprocess.call(['7z', 'x', os.path.join(directory, filename), '-pinfected'], shell=True)
            if r == 0:
                os.remove(os.path.join(directory, filename))

if __name__ == '__main__':
    main()