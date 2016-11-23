#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

directory = '/home/sec06/下载/Dataset-malware'
def main():
    for subdirectory in os.listdir():
        r = subprocess.call(['python', 'get_apk_features.py', '-d', os.path.join(directory, subdirectory), '-s', '-1'])

if __name__ == '__main__':
    main()