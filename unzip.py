#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess, os

for filename in os.listdir('.'):
    if os.path.splitext(filename)[1] == '.7z'):
        r = subprocess.call(['7z', 'x', filename, '-pinfected'])
        os.remove(filename)