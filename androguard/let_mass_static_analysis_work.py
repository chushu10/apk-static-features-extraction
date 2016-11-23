#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

directory = '/Users/liuchushu/Downloads/Dataset/vir-dataset'
def main():
    for subdirectory in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, subdirectory)):
            r = subprocess.call(['python', 'mass_static_analysis.py', '-d', os.path.join(directory, subdirectory)])

if __name__ == '__main__':
    main()