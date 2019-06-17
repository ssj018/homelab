#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

def find_csrf(text):
    pattern = r'''<input type='hidden' name='__csrf_magic' value="(.*)" />'''
    csrf = re.findall(pattern, text)
    return csrf[0].split(";")[0]


def backup():
    url = 'http://pfsense.atzweb.com'
    ss = requests.session()
    ret = ss.get(url)
    csrf = find_csrf(ret.text)
    data = {
        'usernamefld': 'admin',
        'passwordfld': 'Pfsense@mds_2018',
        '__csrf_magic': csrf,
        'login': 'Sign In'

    }

    backup_url = 'http://pfsense.atzweb.com/diag_backup.php'
    ss.post(url, data=data)

    backup_ret = ss.get(backup_url)
    backup_crsf = find_csrf(backup_ret.text)

    backup_data = {
        "__csrf_magic": backup_crsf,
        "donotbackuprrd": "yes",
        "download": "Download configuration as XML"
    }
    config_ret = ss.post(backup_url, data=backup_data)
    config = config_ret.text
    print(config)
    with open("conf/config.xml_{}".format(today), 'w') as f:
        f.writelines(config)


if __name__ == '__main__':
    backup()
