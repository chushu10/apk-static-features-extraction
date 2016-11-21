#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, os, json, urllib, argparse

# 计算文件的hash值
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 将文件名重命名为hash值
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='path of the directory')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    # 文件名-摘要字典
    filename_digest = {}
    repeat_filename_digest = {}
    filename_list = os.listdir(directory)
    # 摘要集合，防止重复
    digest_set = set()
    for filename in filename_list:
        # 跳过rename.py和filename_digest.json文件
        if filename == 'rename.py' or filename == 'filename_digest.json':
            continue

        digest = md5(os.path.join(directory, filename))
        if filename == digest + '.apk':
            print('Don\'t run this script more than once!')
            exit()
        decoded_filename = filename#.decode('gbk')
        
        if digest not in digest_set:
            digest_set.add(digest)
            filename_digest[decoded_filename] = digest
            print('renaming ' + decoded_filename + ' as ' + digest + '.apk')
            os.rename(os.path.join(directory, filename), os.path.join(directory, digest + '.apk'))
        else:
            repeat_filename_digest[decoded_filename] = digest

    # 提示重复的文件名及其摘要
    print('\n')
    for filename in repeat_filename_digest:
        print(filename + ' repeated, it\'s digest is ' + repeat_filename_digest[filename])
        os.remove(os.path.join(directory, filename))

    # 将原始文件名-摘要字典存入json文件中
    f = open(os.path.join(directory, 'filename_digest.json'), 'w')
    json.dump(filename_digest, f)
    f.close()

if __name__ == '__main__':
    main()