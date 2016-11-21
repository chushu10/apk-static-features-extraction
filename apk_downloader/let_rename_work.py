#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

def main():
    for directory in os.listdir('/home/sec06/下载/Dataset-malware'):
        r = subprocess.call(['python', 'rename.py', '-d', os.path.join('/home/sec06/下载/Dataset-malware', directory)])

if __name__ == '__main__':
    main()