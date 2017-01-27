#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import arff, os, argparse
from terminaltables import AsciiTable

def main():
    f = open('../weka_arff/benign_53422_all.arff', 'r')
    file = f.read()
    f.close()
    dataset = arff.loads(file)
    
    count = 0
    d = dict()

    # less_than = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,
    #              105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200,
    #              205,210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300,]
    less_than = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
                 41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    # less_than = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
    #              42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
    #              82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120]

    # Widgets
    d['buttonCount'] = 0      # 25
    button = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['TextViewCount'] = 0    # 26
    text = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['EditViewCount'] = 0    # 27
    edit = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['ImageButtonCount'] = 0 # 28
    ibutton = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['CheckBoxCount'] = 0    # 29
    checkbox = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    # 30
    radiogroup = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    # 31
    radiobutton = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['ToastCount'] = 0       # 32
    toast = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    # 33
    spinner = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    # 34
    listview = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

    d['hPictureCount'] = 0  # 64
    h_pic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['mPictureCount'] = 0  # 65
    m_pic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['lPictureCount'] = 0  # 66
    l_pic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    d['xPictureCount'] = 0  # 67
    x_pic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

    for data in dataset['data']:
        count += 1
        # d['buttonCount'] += data[24]      # 25
        # d['TextViewCount'] += data[25]    # 26
        # d['EditViewCount'] += data[26]    # 27
        # d['ImageButtonCount'] += data[27] # 28
        # d['CheckBoxCount'] += data[28]    # 29
        # d['RadioGroupCount'] += data[29]  # 30
        # d['RadioButtonCount'] += data[30] # 31
        # d['ToastCount'] += data[31]       # 32
        # d['SpinnerCount'] += data[32]     # 33
        # d['ListViewCount'] += data[33]    # 34
        for i in range(0,len(less_than)):
            if data[24] <= less_than[i]:
                button[i] += 1
            if data[25] <= less_than[i]:
                text[i] += 1
            if data[26] <= less_than[i]:
                edit[i] += 1
            if data[27] <= less_than[i]:
                ibutton[i] += 1
            if data[28] <= less_than[i]:
                checkbox[i] += 1
            if data[29] <= less_than[i]:
                radiogroup[i] += 1
            if data[30] <= less_than[i]:
                radiobutton[i] += 1
            if data[31] <= less_than[i]:
                toast[i] += 1
            if data[32] <= less_than[i]:
                spinner[i] += 1
            if data[33] <= less_than[i]:
                listview[i] += 1

        # d['hPictureCount'] += data[63]  # 64
        # d['mPictureCount'] += data[64]  # 65
        # d['lPictureCount'] += data[65]  # 66
        # d['xPictureCount'] += data[66]  # 67
        # for i in range(0,len(less_than)):
        #     if data[63] < less_than[i]:
        #         h_pic[i] += 1
        #     if data[64] < less_than[i]:
        #         m_pic[i] += 1
        #     if data[65] < less_than[i]:
        #         l_pic[i] += 1
        #     if data[66] < less_than[i]:
        #         x_pic[i] += 1


    print 'Total instances', count

    print 'button:'
    coordinates = ''
    for i in range(0, len(button)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(button[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'text:'
    coordinates = ''
    for i in range(0, len(text)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(text[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'edit:'
    coordinates = ''
    for i in range(0, len(edit)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(edit[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'ibutton:'
    coordinates = ''
    for i in range(0, len(ibutton)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(ibutton[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'checkbox:'
    coordinates = ''
    for i in range(0, len(checkbox)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(checkbox[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'radiogroup:'
    coordinates = ''
    for i in range(0, len(radiogroup)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(radiogroup[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'radiobutton:'
    coordinates = ''
    for i in range(0, len(radiobutton)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(radiobutton[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'toast:'
    coordinates = ''
    for i in range(0, len(toast)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(toast[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'spinner:'
    coordinates = ''
    for i in range(0, len(spinner)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(spinner[i] * 100 / count)
        coordinates += ')'
    print coordinates

    print 'listview:'
    coordinates = ''
    for i in range(0, len(listview)):
        coordinates += '('
        coordinates += str(less_than[i])
        coordinates += ','
        coordinates += str(listview[i] * 100 / count)
        coordinates += ')'
    print coordinates

    # print 'h_pic:'
    # coordinates = ''
    # for i in range(0, len(h_pic)):
    #     coordinates += '('
    #     coordinates += str(less_than[i])
    #     coordinates += ','
    #     coordinates += str(h_pic[i] * 100 / count)
    #     coordinates += ')'
    # print coordinates

    # print 'm_pic:'
    # coordinates = ''
    # for i in range(0, len(m_pic)):
    #     coordinates += '('
    #     coordinates += str(less_than[i])
    #     coordinates += ','
    #     coordinates += str(m_pic[i] * 100 / count)
    #     coordinates += ')'
    # print coordinates

    # print 'l_pic:'
    # coordinates = ''
    # for i in range(0, len(l_pic)):
    #     coordinates += '('
    #     coordinates += str(less_than[i])
    #     coordinates += ','
    #     coordinates += str(l_pic[i] * 100 / count)
    #     coordinates += ')'
    # print coordinates

    # print 'x_pic:'
    # coordinates = ''
    # for i in range(0, len(x_pic)):
    #     coordinates += '('
    #     coordinates += str(less_than[i])
    #     coordinates += ','
    #     coordinates += str(x_pic[i] * 100 / count)
    #     coordinates += ')'
    # print coordinates

if __name__ == '__main__':
    main()