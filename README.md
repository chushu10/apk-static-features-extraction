# apk-static-features-extraction

This work is an extention of [Androguard](https://github.com/androguard/androguard) and [MobSF](https://github.com/ajinabraham/Mobile-Security-Framework-MobSF). For more information about Androguard and MobSF, please click the link below:

- [Androguard](https://github.com/androguard/androguard): Reverse engineering, Malware and goodware analysis of Android applications ... and more (ninja !)
- [MobSF](https://github.com/ajinabraham/Mobile-Security-Framework-MobSF): Mobile Security Framework is an intelligent, all-in-one open source mobile application (Android/iOS) automated pen-testing framework capable of performing static, dynamic analysis and web API testing. http://opensecurity.in

**Attentions**: you should fully understand how Androguard and MobSF deal with apks!

This work contains three parts:

- Automatic crawler of Android APK. In directory "apk_downloader".
- Extension of Androguard. In directory "androguard".
- Extension of MobSF. In directory "mobsf"

# How to install

**Attensions**:You should have both python 2 and python 3 installed. Then follow these guids:

1. Copy python scripts in "androguard" to Androguard's main directory
2. Copy python scripts in "mobsf" to MobSF's main directory
3. If there are modules not found, follow the guide promted by python to install the requested modules.

# Automatic crawler of Android APK

There are 4 python scripts in directory "apk_downloader":

- apk_downloader.py(run with python 2)
- my_html_parser.py
- rename.py(run with python 3)
- let_rename_work.py(run with python 3)

"apk_downloader.py" and "my_html_parser.py" are used to download apks from [anruan](anruan.com) app store. If you want to download apps from another app store, change the code in "my_html_parser.py"(you should understand how to parse HTML and get what you want from Web page written in HTML, refer to [this direction](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320023122880232500da9dc4a4486ad00426f081c15000)). "apk_downloader.py" will generate sub-directories in its current directory, these sub-directories contain the apps downloaded.

"rename.py" is used to rename the app names to its corresponding hash md5 digest, since most of the apps downloaded are named in Chinese. However, all of the Android static code analyzer cannot tackle with Chinese characters. "let_rename_work.py" is simply a lazy script used to automatically trigger "rename.py" work in every directory. "rename.py" generate a "filename_digest.json" which saves the relations between the original filename and its hash md5 digest.

# Extension of Androguard

There are 2 python scripts in directory "androguard":

- get_apk_features.py(run with python 2)
- let_get_apk_features_work.py(run with python 2)

"get_apk_features.py" is used to extract apk features using androguard analyzer, it will generate a "weka_testset.arff" file for later study, and a "cannot_analyze.txt" file in case there are apps that cannot be analyzed by androguard. "let_get_apk_features_work.py" is simply a lazy script used to automatically trigger "get_apk_features_work.py" work in every directory. 

# Extension of MobSF

There are 3 python scripts in directory "mobsf":

- get_permissions.py(run with python 3)
- get_remained.py(run with python 3)
- get_unclicked.py(run with python 3)

You should first run "mass_static_analysis.py" of MobSF to upload the apks in your folder.

"get_permissions.py" extract the permission information from MobSF analyze result, it will generate a "permissions.json" file which saves the relations between the analyzed apk and its permissions.

"get_remained.py" checks if there are apks cannot analyzed, it will generate a folder named "cannot_be_analyzed" and move these apks to this folder.

"get_unclicked.py" clicks each link provided by MobSF. Because MobSF cannot tackle with apks more than a few hundred in a short period of time, so that most of the apks are left un-analyzed. You can click the link by hand, but that is a waste of time, Use "get_unclicked.py" do it for you.