#!/usr/bin/env python
# -*- coding: utf-8 -*-

import androlyze, argparse, zipfile, os, arff, traceback, sys

class OrderedClassMembers(type):
    @classmethod
    def __prepare__(self, name, bases):
        return collections.OrderedDict()

    def __new__(self, name, bases, classdict):
        classdict['__ordered__'] = [key for key in classdict.keys()
                if key not in ('__module__', '__qualname__')]
        return type.__new__(self, name, bases, classdict)

class FeatureVector(object):

    __metaclass__ = OrderedClassMembers
    
    def __init__(self, apk_category, apk_size, dex_size, min_andrversion, max_andrversion,
                 target_andrversion, versionName, installLocation, security, methodCount,
                 classCount, crypto_count, dynCode_count, native_count, reflect_count,
                 sendSMS, deleteSMS, interruptSMS, httpPost, deviceId, simCountry,
                 installedPkg, loadOtherCode, subprocess, executeOtherCode, jni, unix,
                 buttonCount, TextViewCount, EditViewCount, ImageButtonCount, CheckBoxCount,
                 RadioGroupCount, RadioButtonCount, ToastCount, SpinnerCount, ListViewCount,
                 fileCount, INTERNET, SET_DEBUG_APP, MODIFY_PHONE_STATE, RECORD_AUDIO,
                 RECEIVE_BOOT_COMPLETED, RECEIVE_MMS, RECEIVE_SMS, RECEIVE_WAP_PUSH,
                 SEND_SMS, CALL_PHONE, CALL_PRIVILEGED, PROCESS_OUTGOING_CALLS, READ_CALL_LOG,
                 READ_EXTERNAL_STORAGE, READ_LOGS, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION,
                 BLUETOOTH, CAMERA, INSTALL_PACKAGES, NFC, READ_CONTACTS, sharedUserId,
                 permissionCount, activityCount, serviceCount, receiverCount, providerCount,
                 exportedCount, backupAgent, killAfterRestore, allowTaskReparenting, process,
                 taskAffinity, hPictureCount, mPictureCount, lPictureCount, xPictureCount, totalCount):
        self.apk_category = apk_category
        self.apk_size = apk_size
        self.dex_size = dex_size
        self.min_andrversion = min_andrversion
        self.max_andrversion = max_andrversion
        self.target_andrversion = target_andrversion
        self.versionName = versionName
        self.installLocation = installLocation
        self.security = security
        self.methodCount = methodCount
        self.classCount = classCount
        self.crypto_count = crypto_count
        self.dynCode_count = dynCode_count
        self.native_count = native_count
        self.reflect_count = reflect_count
        self.sendSMS = sendSMS
        self.deleteSMS = deleteSMS
        self.interruptSMS = interruptSMS
        self.httpPost = httpPost
        self.deviceId = deviceId
        self.simCountry = simCountry
        self.installedPkg = installedPkg
        self.loadOtherCode = loadOtherCode
        self.subprocess = subprocess
        self.executeOtherCode = executeOtherCode
        self.jni = jni
        self.unix = unix
        self.buttonCount = buttonCount
        self.TextViewCount = TextViewCount
        self.EditViewCount = EditViewCount
        self.ImageButtonCount = ImageButtonCount
        self.CheckBoxCount = CheckBoxCount
        self.RadioGroupCount = RadioGroupCount
        self.RadioButtonCount = RadioButtonCount
        self.ToastCount = ToastCount
        self.SpinnerCount = SpinnerCount
        self.ListViewCount = ListViewCount
        self.fileCount = fileCount
        self.INTERNET = INTERNET
        self.SET_DEBUG_APP = SET_DEBUG_APP
        self.MODIFY_PHONE_STATE = MODIFY_PHONE_STATE
        self.RECORD_AUDIO = RECORD_AUDIO
        self.RECEIVE_BOOT_COMPLETED = RECEIVE_BOOT_COMPLETED
        self.RECEIVE_MMS = RECEIVE_MMS
        self.RECEIVE_SMS = RECEIVE_SMS
        self.RECEIVE_WAP_PUSH = RECEIVE_WAP_PUSH
        self.SEND_SMS = SEND_SMS
        self.CALL_PHONE = CALL_PHONE
        self.CALL_PRIVILEGED = CALL_PRIVILEGED
        self.PROCESS_OUTGOING_CALLS = PROCESS_OUTGOING_CALLS
        self.READ_CALL_LOG = READ_CALL_LOG
        self.READ_EXTERNAL_STORAGE = READ_EXTERNAL_STORAGE
        self.READ_LOGS = READ_LOGS
        self.ACCESS_COARSE_LOCATION = ACCESS_COARSE_LOCATION
        self.ACCESS_FINE_LOCATION = ACCESS_FINE_LOCATION
        self.BLUETOOTH = BLUETOOTH
        self.CAMERA = CAMERA
        self.INSTALL_PACKAGES = INSTALL_PACKAGES
        self.NFC = NFC
        self.READ_CONTACTS = READ_CONTACTS
        self.sharedUserId = sharedUserId
        self.permissionCount = permissionCount
        self.activityCount = activityCount
        self.serviceCount = serviceCount
        self.receiverCount = receiverCount
        self.providerCount = providerCount
        self.exportedCount = exportedCount
        self.backupAgent = backupAgent
        self.killAfterRestore = killAfterRestore
        self.allowTaskReparenting = allowTaskReparenting
        self.process = process
        self.taskAffinity = taskAffinity
        self.hPictureCount = hPictureCount
        self.mPictureCount = mPictureCount
        self.lPictureCount = lPictureCount
        self.xPictureCount = xPictureCount
        self.totalCount = totalCount
        print (apk_category, apk_size, dex_size, min_andrversion, max_andrversion,
                 target_andrversion, versionName, installLocation, security, methodCount,
                 classCount, crypto_count, dynCode_count, native_count, reflect_count,
                 sendSMS, deleteSMS, interruptSMS, httpPost, deviceId, simCountry,
                 installedPkg, loadOtherCode, subprocess, executeOtherCode, jni, unix,
                 buttonCount, TextViewCount, EditViewCount, ImageButtonCount, CheckBoxCount,
                 RadioGroupCount, RadioButtonCount, ToastCount, SpinnerCount, ListViewCount,
                 fileCount, INTERNET, SET_DEBUG_APP, MODIFY_PHONE_STATE, RECORD_AUDIO,
                 RECEIVE_BOOT_COMPLETED, RECEIVE_MMS, RECEIVE_SMS, RECEIVE_WAP_PUSH,
                 SEND_SMS, CALL_PHONE, CALL_PRIVILEGED, PROCESS_OUTGOING_CALLS, READ_CALL_LOG,
                 READ_EXTERNAL_STORAGE, READ_LOGS, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION,
                 BLUETOOTH, CAMERA, INSTALL_PACKAGES, NFC, READ_CONTACTS, sharedUserId,
                 permissionCount, activityCount, serviceCount, receiverCount, providerCount,
                 exportedCount, backupAgent, killAfterRestore, allowTaskReparenting, process,
                 taskAffinity, hPictureCount, mPictureCount, lPictureCount, xPictureCount, totalCount)
        

def analyze(path_to_apk, apk_category, security):
    apk_zip = zipfile.ZipFile(path_to_apk)
    apk_size = os.path.getsize(path_to_apk)
    dex_size = apk_zip.getinfo('classes.dex').file_size

    # Analyze apk
    a, d, dx = androlyze.AnalyzeAPK(path_to_apk, decompiler='dad')

    # APK features
    if a.get_min_sdk_version() is not None:
        min_andrversion = str(a.get_min_sdk_version())
    else:
        min_andrversion = 0
    if a.get_max_sdk_version() is not None:
        max_andrversion = str(a.get_max_sdk_version())
    else:
        max_andrversion = 0
    if a.get_target_sdk_version() is not None:
        target_andrversion = str(a.get_target_sdk_version())
    else:
        target_andrversion = 0
    if a.get_androidversion_name() is not None:
        versionName = str(a.get_androidversion_name())
    else:
        versionName = ''
    installLocation = 0
    methodCount = d.get_len_methods()
    classCount = len(d.get_classes())
    crypto_count = len(dx.get_tainted_packages().search_methods('Ljava/crypto/.', '.', '.'))
    dynCode_count = len(dx.get_tainted_packages().search_methods('Ldalvik/system/DexClassLoader/.', '.', '.'))
    native_count = len(dx.get_tainted_packages().search_methods('Ljava/lang/System;', '.', '.'))
    reflect_count = len(dx.get_tainted_packages().search_methods('Ljava/lang/reflect/Method;', '.', '.'))
    fileCount = len(a.get_files())

    # API features
    # sendSMS
    if (len(dx.get_tainted_packages().search_methods('Landroid/telephony/SmsManager;', 'send[a-zA-Z]+Message', '.')) > 0) or (len(dx.get_tainted_packages().search_methods('Landroid/telephony/gsm/SmsManager;', 'send[a-zA-Z]+Message', '.')) > 0):
        sendSMS = 1
    else:
        sendSMS = 0
    # deleteSMS
    deleteSMS = 0
    # interruptSMS
    if len(dx.get_tainted_packages().search_methods('Landroid/content/BroadcastReceiver;', 'abortBroadcast', '.')) > 0:
        interruptSMS = 1
    else:
        interruptSMS = 0
    # httpPost
    if (len(dx.get_tainted_packages().search_methods('Lorg/apache/http/client/methods/HttpPost;', '.', '.')) > 0) or (len(dx.get_tainted_packages().search_methods('Ljava/net/HttpURLConnection;', '.', '.')) > 0):
        httpPost = 1
    else:
        httpPost = 0
    # deviceId
    if len(dx.get_tainted_packages().search_methods('Landroid/telephony/TelephonyManager;', 'getDeviceId', '.')) > 0:
        deviceId = 1
    else:
        deviceId = 0
    # simCountry
    if len(dx.get_tainted_packages().search_methods('Landroid/telephony/TelephonyManager;', 'getSimCountryIso', '.')) > 0:
        simCountry = 1
    else:
        simCountry = 0
    # installedPkg
    if len(dx.get_tainted_packages().search_methods('Landroid/content/pm/PackageManager;', 'getInstalledPackages', '.')) > 0:
        installedPkg = 1
    else:
        installedPkg = 0
    # loadOtherCode
    loadOtherCode = 0
    # subprocess
    if (len(dx.get_tainted_packages().search_methods('Ljava/lang/ProcessBuilder;','start','.')) > 0) or (len(dx.get_tainted_packages().search_methods('Ljava/lang/Runtime;','exec','.')) > 0):
        subprocess = 1
    else:
        subprocess = 0
    # executeOtherCode
    executeOtherCode = 0
    # jni
    if len(dx.get_tainted_packages().search_methods('Ljava/lang/System;', 'loadLibrary', '.')) > 0:
        jni = 1
    else:
        jni = 0
    # unix
    unix = 0

    # Widget features
    fields = dx.get_tainted_fields()
    field_list = []
    for field in fields:
        field_list.append(field)
    # buttonCount
    buttonCount, TextViewCount, EditViewCount, ImageButtonCount, CheckBoxCount, RadioGroupCount, RadioButtonCount, ToastCount, SpinnerCount, ListViewCount = 0,0,0,0,0,0,0,0,0,0
    for field in field_list:
        if 'Landroid/widget/Button;' in field[1]:
            buttonCount += 1
        elif 'Landroid/widget/TextView;' in field[1]:
            TextViewCount += 1
        elif 'Landroid/widget/ImageButton;' in field[1]:
            ImageButtonCount += 1
        elif 'Landroid/widget/CheckBox;' in field[1]:
            CheckBoxCount += 1
        elif 'Landroid/widget/RadioGroup;' in field[1]:
            RadioGroupCount += 1
        elif 'Landroid/widget/RadioButton;' in field[1]:
            RadioButtonCount += 1
        elif 'Landroid/widget/Spinner;' in field[1]:
            SpinnerCount += 1
        elif 'Landroid/widget/ListView;' in field[1]:
            ListViewCount += 1

    # Permission features
    # INTERNET
    if 'android.permission.INTERNET' in a.get_permissions():
        INTERNET = 1
    else:
        INTERNET = 0
    # SET_DEBUG_APP
    if 'android.permission.SET_DEBUG_APP' in a.get_permissions():
        SET_DEBUG_APP = 1
    else:
        SET_DEBUG_APP = 0
    # MODIFY_PHONE_STATE
    if 'android.permission.MODIFY_PHONE_STATE' in a.get_permissions():
        MODIFY_PHONE_STATE = 1
    else:
        MODIFY_PHONE_STATE = 0
    # RECORD_AUDIO
    if 'android.permission.RECORD_AUDIO' in a.get_permissions():
        RECORD_AUDIO = 1
    else:
        RECORD_AUDIO = 0
    # RECEIVE_BOOT_COMPLETED
    if 'android.permission.RECEIVE_BOOT_COMPLETED' in a.get_permissions():
        RECEIVE_BOOT_COMPLETED = 1
    else:
        RECEIVE_BOOT_COMPLETED = 0
    # RECEIVE_MMS
    if 'android.permission.RECEIVE_MMS' in a.get_permissions():
        RECEIVE_MMS = 1
    else:
        RECEIVE_MMS = 0
    # RECEIVE_SMS
    if 'android.permission.RECEIVE_SMS' in a.get_permissions():
        RECEIVE_SMS = 1
    else:
        RECEIVE_SMS = 0
    # RECEIVE_WAP_PUSH
    if 'android.permission.RECEIVE_WAP_PUSH' in a.get_permissions():
        RECEIVE_WAP_PUSH = 1
    else:
        RECEIVE_WAP_PUSH = 0
    # SEND_SMS
    if 'android.permission.SEND_SMS' in a.get_permissions():
        SEND_SMS = 1
    else:
        SEND_SMS = 0
    # CALL_PHONE
    if 'android.permission.CALL_PHONE' in a.get_permissions():
        CALL_PHONE = 1
    else:
        CALL_PHONE = 0
    # CALL_PRIVILEGED
    if 'android.permission.CALL_PRIVILEGED' in a.get_permissions():
        CALL_PRIVILEGED = 1
    else:
        CALL_PRIVILEGED = 0
    # PROCESS_OUTGOING_CALLS
    if 'android.permission.PROCESS_OUTGOING_CALLS' in a.get_permissions():
        PROCESS_OUTGOING_CALLS = 1
    else:
        PROCESS_OUTGOING_CALLS = 0
    # READ_CALL_LOG
    if 'android.permission.READ_CALL_LOG' in a.get_permissions():
        READ_CALL_LOG = 1
    else:
        READ_CALL_LOG = 0
    # READ_EXTERNAL_STORAGE
    if 'android.permission.READ_EXTERNAL_STORAGE' in a.get_permissions():
        READ_EXTERNAL_STORAGE = 1
    else:
        READ_EXTERNAL_STORAGE = 0
    # READ_LOGS
    if 'android.permission.READ_LOGS' in a.get_permissions():
        READ_LOGS = 1
    else:
        READ_LOGS = 0
    # ACCESS_COARSE_LOCATION
    if 'android.permission.ACCESS_COARSE_LOCATION' in a.get_permissions():
        ACCESS_COARSE_LOCATION = 1
    else:
        ACCESS_COARSE_LOCATION = 0
    # ACCESS_FINE_LOCATION
    if 'android.permission.ACCESS_FINE_LOCATION' in a.get_permissions():
        ACCESS_FINE_LOCATION = 1
    else:
        ACCESS_FINE_LOCATION = 0
    # BLUETOOTH
    if 'android.permission.BLUETOOTH' in a.get_permissions():
        BLUETOOTH = 1
    else:
        BLUETOOTH = 0
    # CAMERA
    if 'android.permission.CAMERA' in a.get_permissions():
        CAMERA = 1
    else:
        CAMERA = 0
    # INSTALL_PACKAGES
    if 'android.permission.INSTALL_PACKAGES' in a.get_permissions():
        INSTALL_PACKAGES = 1
    else:
        INSTALL_PACKAGES = 0
    # NFC
    if 'android.permission.NFC' in a.get_permissions():
        NFC = 1
    else:
        NFC = 0
    # READ_CONTACTS
    if 'android.permission.READ_CONTACTS' in a.get_permissions():
        READ_CONTACTS = 1
    else:
        READ_CONTACTS = 0

    # Manifest features
    # sharedUserId
    if a.get_AndroidManifest().getElementsByTagName('manifest')[0].getAttribute('android:sharedUserId') is not None:
        sharedUserId = a.get_AndroidManifest().getElementsByTagName('manifest')[0].getAttribute('android:sharedUserId')
    else:
        sharedUserId = ''
    # permissionCount
    permissionCount = 0
    # activityCount
    activityCount = len(a.get_activities())
    # serviceCount
    serviceCount = len(a.get_services())
    # receiverCount
    receiverCount = len(a.get_receivers())
    # providerCount
    providerCount = len(a.get_providers())
    # exportedCount
    exportedCount = 0
    for activity in a.get_AndroidManifest().getElementsByTagName('activity'):
        if activity.getAttribute('android:exported') == 'true':
            exportedCount += 1
    for service in a.get_AndroidManifest().getElementsByTagName('service'):
        if activity.getAttribute('android:exported') == 'true':
            exportedCount += 1
    for receiver in a.get_AndroidManifest().getElementsByTagName('receiver'):
        if activity.getAttribute('android:exported') == 'true':
            exportedCount += 1
    for provider in a.get_AndroidManifest().getElementsByTagName('provider'):
        if activity.getAttribute('android:exported') == 'true':
            exportedCount += 1
    # backupAgent
    if a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:backupAgent') is not None:
        backupAgent = a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:backupAgent')
    else:
        backupAgent = ''
    # killAfterRestore
    if a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:killAfterRestore') is not None:
        killAfterRestore = a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:killAfterRestore')
    else:
        killAfterRestore = ''
    # allowTaskReparenting
    if a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:allowTaskReparenting') is not None:
        allowTaskReparenting = a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:allowTaskReparenting')
    else:
        allowTaskReparenting = ''
    # process
    if a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:process') is not None:
        process = a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:process')
    else:
        process = ''
    # taskAffinity
    if a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:taskAffinity') is not None:
        taskAffinity = a.get_AndroidManifest().getElementsByTagName('application')[0].getAttribute('android:taskAffinity')
    else:
        taskAffinity = ''
    # hPictureCount
    # mPictureCount
    # lPictureCount
    # xPictureCount
    hPictureCount, mPictureCount, lPictureCount, xPictureCount = 0, 0, 0, 0
    for info in a.zip.infolist():
        if 'res/drawable-hdpi' in info.filename:
            hPictureCount += 1
        elif 'res/drawable-mdpi' in info.filename:
            mPictureCount += 1
        elif 'res/drawable-ldpi' in info.filename:
            lPictureCount += 1
        elif 'res/drawable-xhdpi' in info.filename:
            xPictureCount += 1
    # totalCount
    totalCount = hPictureCount + mPictureCount + lPictureCount + xPictureCount

    # Initialize FeatureVector
    fv = FeatureVector(apk_category, apk_size, dex_size, min_andrversion, max_andrversion,
                 target_andrversion, versionName, installLocation, security, methodCount,
                 classCount, crypto_count, dynCode_count, native_count, reflect_count,
                 sendSMS, deleteSMS, interruptSMS, httpPost, deviceId, simCountry,
                 installedPkg, loadOtherCode, subprocess, executeOtherCode, jni, unix,
                 buttonCount, TextViewCount, EditViewCount, ImageButtonCount, CheckBoxCount,
                 RadioGroupCount, RadioButtonCount, ToastCount, SpinnerCount, ListViewCount,
                 fileCount, INTERNET, SET_DEBUG_APP, MODIFY_PHONE_STATE, RECORD_AUDIO,
                 RECEIVE_BOOT_COMPLETED, RECEIVE_MMS, RECEIVE_SMS, RECEIVE_WAP_PUSH,
                 SEND_SMS, CALL_PHONE, CALL_PRIVILEGED, PROCESS_OUTGOING_CALLS, READ_CALL_LOG,
                 READ_EXTERNAL_STORAGE, READ_LOGS, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION,
                 BLUETOOTH, CAMERA, INSTALL_PACKAGES, NFC, READ_CONTACTS, sharedUserId,
                 permissionCount, activityCount, serviceCount, receiverCount, providerCount,
                 exportedCount, backupAgent, killAfterRestore, allowTaskReparenting, process,
                 taskAffinity, hPictureCount, mPictureCount, lPictureCount, xPictureCount, totalCount)
    return fv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='directory of the dataset')
    parser.add_argument('-s', '--security', help='benign(0) or malware(-1)')
    args = parser.parse_args()
    if args.directory:
        directory = args.directory
    else:
        parser.print_help()
    if args.security:
        security = args.security
    else:
        parser.print_help()

    # arff object
    obj = {
        'description': u'',
        'relation': 'testset',
        'attributes': [
            ('apk_category', 'STRING'),
            ('apk_size', 'REAL'),
            ('dex_size', 'REAL'),
            ('min_andrversion', 'INTEGER'),
            ('max_andrversion', 'INTEGER'),
            ('target_andrversion', 'INTEGER'),
            ('versionName', 'STRING'),
            ('installLocation', 'INTEGER'),
            ('security', ['-1','0']),
            ('methodCount', 'INTEGER'),
            ('classCount', 'INTEGER'),
            ('crypto_count', 'INTEGER'),
            ('dynCode_count', 'INTEGER'),
            ('native_count', 'INTEGER'),
            ('reflect_count', 'INTEGER'),
            ('sendSMS', ['1', '0']),
            ('deleteSMS', ['1', '0']),
            ('interruptSMS', ['1', '0']),
            ('httpPost', ['1', '0']),
            ('deviceId', ['1', '0']),
            ('simCountry', ['1', '0']),
            ('installedPkg', ['1', '0']),
            ('loadOtherCode', ['1', '0']),
            ('subprocess', ['1', '0']),
            ('executeOtherCode', ['1', '0']),
            ('jni', ['1', '0']),
            ('unix', ['1', '0']),
            ('buttonCount', 'INTEGER'),
            ('TextViewCount', 'INTEGER'),
            ('EditViewCount', 'INTEGER'),
            ('ImageButtonCount', 'INTEGER'),
            ('CheckBoxCount', 'INTEGER'),
            ('RadioGroupCount', 'INTEGER'),
            ('RadioButtonCount', 'INTEGER'),
            ('ToastCount', 'INTEGER'),
            ('SpinnerCount', 'INTEGER'),
            ('ListViewCount', 'INTEGER'),
            ('fileCount', 'INTEGER'),
            ('INTERNET', ['1', '0']),
            ('SET_DEBUG_APP', ['1', '0']),
            ('MODIFY_PHONE_STATE', ['1', '0']),
            ('RECORD_AUDIO', ['1', '0']),
            ('RECEIVE_BOOT_COMPLETED', ['1', '0']),
            ('RECEIVE_MMS', ['1', '0']),
            ('RECEIVE_SMS', ['1', '0']),
            ('RECEIVE_WAP_PUSH', ['1', '0']),
            ('SEND_SMS', ['1', '0']),
            ('CALL_PHONE', ['1', '0']),
            ('CALL_PRIVILEGED', ['1', '0']),
            ('PROCESS_OUTGOING_CALLS', ['1', '0']),
            ('READ_CALL_LOG', ['1', '0']),
            ('READ_EXTERNAL_STORAGE', ['1', '0']),
            ('READ_LOGS', ['1', '0']),
            ('ACCESS_COARSE_LOCATION', ['1', '0']),
            ('ACCESS_FINE_LOCATION', ['1', '0']),
            ('BLUETOOTH', ['1', '0']),
            ('CAMERA', ['1', '0']),
            ('INSTALL_PACKAGES', ['1', '0']),
            ('NFC', ['1', '0']),
            ('READ_CONTACTS', ['1', '0']),
            ('sharedUserId', 'STRING'),
            ('permissionCount', 'INTEGER'),
            ('activityCount', 'INTEGER'),
            ('serviceCount', 'INTEGER'),
            ('receiverCount', 'INTEGER'),
            ('providerCount', 'INTEGER'),
            ('exportedCount', 'INTEGER'),
            ('backupAgent', 'STRING'),
            ('killAfterRestore', 'STRING'),
            ('allowTaskReparenting', 'STRING'),
            ('process', 'STRING'),
            ('taskAffinity', 'STRING'),
            ('hPictureCount', 'INTEGER'),
            ('mPictureCount', 'INTEGER'),
            ('lPictureCount', 'INTEGER'),
            ('xPictureCount', 'INTEGER'),
            ('totalCount', 'INTEGER'),
        ],
        'data': [],
    }

    cannot_analyze = []
    i = 0
    print os.path.basename(os.path.normpath(directory))
    for filename in os.listdir(directory):
        if (os.path.splitext(filename)[1] == '.apk') or (os.path.splitext(filename)[1] == '.vir'):
            print i+1, filename + ':'
            try:
                fv = analyze(os.path.join(directory, filename), os.path.basename(os.path.normpath(directory)), security)
            except Exception, e:
                print "Exception in user code:"
                print '-'*60
                traceback.print_exc(file=sys.stdout)
                print '-'*60
                cannot_analyze.append(filename)
                continue
            obj['data'].append([])
            for attr_name in obj['attributes']:
                for attr in dir(fv):
                    if attr_name[0] == attr:
                        obj['data'][i].append(getattr(fv, attr))

            i += 1
            # if i == 2:
            #    break

    print 'Cannot analyze:'
    cannot = open(os.path.join(directory, 'cannot_analyze.txt'), 'w')
    cannot.write('Cannot analyze:\n')
    for filename in cannot_analyze:
        print filename
        cannot.write(filename + '\n')
    cannot.close()

    f = open(os.path.join(directory, 'weka_testset.arff'), 'w')
    arff.dump(obj, f)
    f.close()

if __name__ == '__main__':
    main()