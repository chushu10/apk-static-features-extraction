# coding:utf-8
import urllib2, urllib, os, sys, socket, ConfigParser
from my_html_parser import DownloadLinkParser, AppNameParser

socket.setdefaulttimeout(10)

# show real time download progress
def report(count, blockSize, totalSize):
    percent = int(count * blockSize * 100 / totalSize)
    sys.stdout.write('\r    %d%%' % percent + ' complete')
    sys.stdout.flush()

# download function, need four parameters:
# - dir_name: type of the downloaded apps
# - main_url: url of this type
# - start_page: download from which page
# - end_page: donwload to which page
def download(dir_name,main_url,start_page,end_page):
    # make dir
    try:
        os.mkdir(dir_name)
    except:
        print dir_name + ' exists.'
    # cd to dir
    os.chdir(dir_name)
    
    print '----------------------start download ' + dir_name + ' type----------------'
    open('../app_download.log', 'a').write('----------------------start download ' + dir_name + ' type----------------\n')
    download_num = 0
    
    # a for loop to download apps of every type
    for i in xrange(start_page,end_page):
        print '\nstart download page ', i
        open('../app_download.log', 'a').write('\nstart download page ' + str(i) + '\n')
        open_url = main_url % i
        
        # open the download page
        try:
            main_page = urllib2.urlopen(open_url).read()
        except:
            print 'open:' + open_url + ' error'
            open('../app_download.log', 'a').write('open:' + open_url + ' error')
            continue
        
        # Use HTMLParser to get download urls and app names
        download_link_parser = DownloadLinkParser()
        download_link_parser.feed(main_page)

        app_name_parser = AppNameParser()
        app_name_parser.feed(main_page)

        list_url = download_link_parser.get_download_link()
        list_name = app_name_parser.get_app_name()
        
        # check if download urls match app names
        if len(list_name) != len(list_url):
            print 'list_name length is not equal with list_url length in page: ' + open_url
            open('../app_download.log', 'a').write('list_name length is not equal with list_url length in page: ' + open_url)
            continue
        
        # download all the apps of one page
        for i in xrange(len(list_url)):
            download_num += 1
            print download_num, '  ' + list_name[i] + ' start download......'
            open('../app_download.log', 'a').write(str(download_num) + '  ' + list_name[i] + ' start download......')
            try:
                # reporthook parameter is to show the real time download progress
                urllib.urlretrieve(list_url[i], list_name[i] + '.apk', reporthook=report)
                print '\n  ' + list_name[i] + ' download Ok.....\n'
                open('../app_download.log', 'a').write('\n  ' + list_name[i] + ' download Ok.....\n')
            except:
                print '\n  ' + list_name[i] + ' download error.....\n'
                open('../app_download.log', 'a').write('\n  ' + list_name[i] + ' download error.....\n')
                try:
                    # error, delete the file
                    os.remove(list_name[i] + '.apk')
                except:
                    pass
                continue
    # cd to parent directory
    os.chdir('..')
def main():
    # create config object
    cf = ConfigParser.ConfigParser()
    # read config file
    cf.read('app_config.conf')
    sections = cf.sections()
    for i in sections:
        # ignore download=0 sections
        if cf.get(i, 'download') == '0':
            continue
        dir_name = i
        # get url, start_page, end_page
        try:
            url = cf.get(i, 'url')
            start_page = cf.get(i, 'start_page')
            end_page = cf.get(i, 'end_page')
        except:
            # config file error, exit
            print 'Section ' + i + ' lacks config item\n'
            exit()
        # print dir_name,url,start_page,end_page
        download(dir_name,url, int(start_page), int(end_page))
        
if __name__=='__main__':
    main()