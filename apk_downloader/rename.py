#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, os, json, urllib, argparse

# calc hash md5 digest
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# rename filename as hash md5 digest
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='path of the directory')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()

    # filename_digest dict
    filename_digest = {}
    repeat_filename_digest = {}
    filename_list = os.listdir(directory)
    # digest set, in case there are duplicates
    digest_set = set()
    for filename in filename_list:
        # file must be apk
        if (os.path.splitext(filename)[1] != '.apk') and (os.path.splitext(filename)[1] != '.vir'):
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

    # alert duplicates
    print '\n'
    for filename in repeat_filename_digest:
        print filename + ' repeated, it\'s digest is ' + repeat_filename_digest[filename]
        os.remove(os.path.join(directory, filename))

    # 将原始文件名-摘要字典存入json文件中
    f = open(os.path.join(directory, 'filename_digest.json'), 'w')
    json.dump(filename_digest, f)
    f.close()

if __name__ == '__main__':
    main()