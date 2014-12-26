# -*- coding: utf-8 -*-

from flask import Flask, request
import json
import urllib
import urllib2

import main

APP_ID = ''
APP_SECRET = ''

TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={secret}'.format(app_id=APP_ID, secret=APP_SECRET)

f = urllib2.urlopen(TOKEN_URL)
data = f.read()
data = json.loads(data)
access_token = data['access_token']

MENU_CREATE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + access_token
MENU_DELETE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=' + access_token

def get_menu():
    menu = {
        "button": [
            {
                "name": u'爱聚文章',
                'sub_button': [
                    {
                        'type': 'view',
                        'name': u'爱聚厨房',
                        'url': 'https://www.aijunyc.com/zhs/article?post=238',
                    },
                    {
                        'type': 'view',
                        'name': u'爱聚书房',
                        'key': 'https://www.aijunyc.com/zhs/article?post=229',
                    },
                ]
            },
            {
                "name": u'爱聚活动',
                'sub_button': [
                    {
                        'type': 'click',
                        'name': u'爱聚福利',
                        'key': 'benefit',
                    },
                    {
                        'type': 'click',
                        'name': u'爱聚回顾',
                        'key': 'review',
                    },
                ]
            },
            {
                "name": u'爱聚团队',
                'type': 'click',
                'key': 'about_us',
                    },
                ]
            },
        ]
    }
    return menu

def create_menu():
    menu = create_menu()
    menu = json.dumps(menu).encode('utf-8')
    request = urllib2.urlopen(MENU_URL, menu)
