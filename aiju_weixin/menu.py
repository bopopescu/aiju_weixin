# -*- coding: utf-8 -*-

import argparse
from flask import Flask, request
import json
import sys
import urllib
import urllib2

import main

APP_ID = 'wx92ab0673ca2fcc80'
APP_SECRET = 'a6a1ae038ce493282cee5ceef98f1fc2'

TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={secret}'.format(app_id=APP_ID, secret=APP_SECRET)

MENU_CREATE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='
MENU_GET_URL = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token='
MENU_DELETE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='

def get_menu_structure():
	invalid_menu = {
        "button": [
<<<<<<< HEAD
            {
                "name": u"爱聚文章",
                'sub_button': [
                    {
                        'type': 'view',
                        'name': u'爱聚厨房',
                        'url': 'https://www.aijunyc.com/'
                    },
                    {
                        'type': 'view',
                        'name': u'爱聚书房',
                        'url': 'https://www.aijunyc.com/'
                    }
                ]
            },
            {
                "name": u'爱聚活动',
                'sub_button': [
                    {
                        'type': 'click',
                        'name': u'爱聚福利',
                        'key': 'benefit'
                    },
                    {
                        'type': 'click',
                        'name': u'爱聚回顾',
                        'key': 'review'
                    }
                ]
            },
            {
                'type': 'click',
                "name": u'爱聚团队',
                'key': 'about_us'
            }
        ]
=======
        {
            "name": "爱聚文章",
            "sub_button": [
                {
                    "type": "view",
                    "name": "爱聚厨房",
                    "url": "https://www.aijunyc.com/"
                },
                {
                    "type": "view",
                    "name": "爱聚书房",
                    "url": "https: //www.aijunyc.com/"
                }
            ]
        },
        {
            "name": "爱聚活动",
            "sub_button": [
                {
                    "type": "click",
                    "name": "爱聚福利",
                    "key": "benefit"
                },
                {
                    "type": "click",
                    "name": "爱聚回顾",
                    "key": "review"
                }
            ]
        },
        {
            "type": "click",
            "name": "爱聚团队",
            "key": "about_us"
        }]
>>>>>>> c1f2e4398cc226388ce6690f820f37920a8ddcbb
    }
	

	valid_menu = {
    "button": [
        {
            "name": "爱聚文章",
            "sub_button": [
                {
                    "type": "view",
                    "name": "爱聚厨房",
                    "url": "http://www.aijunyc.com"
                },
                {
                    "type": "view",
                    "name": "爱聚书房",
                    "url": "http://www.aijunyc.com"
                }
            ]
        },
        {
            "name": "爱聚活动",
            "sub_button": [
                {
                    "type": "click",
                    "name": "爱聚福利",
                    "key": "benefit"
                },
                {
                    "type": "click",
                    "name": "爱聚回顾",
                    "key": "review"
                }
            ]
        },
        {
            "type": "click",
            "name": "爱聚团队",
            "key": "about_us"
        }
    ]
	}	

	return valid_menu

def get_token():
    print(TOKEN_URL)
    f = urllib2.urlopen(TOKEN_URL)
    data = f.read()
    data = json.loads(data)
    access_token = data['access_token']
    return access_token

def create_menu(token):
    menu = get_menu_structure()
    menu = json.dumps(menu, ensure_ascii=False)#.encode('utf-8')
    request = urllib2.Request(MENU_CREATE_URL+token)
    request.add_header('Content-Type', 'application/json')
    reload(sys)
    sys.setdefaultencoding('utf-8')
    response = urllib2.urlopen(request, menu)
    ret_dict = json.loads(response.read())
    print(ret_dict)

def get_menu(token):
    request = urllib2.urlopen(MENU_GET_URL+token)
    ret_dict = json.loads(request)
    print(ret_dict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', action='store_true', help='create menu')
    parser.add_argument('-g', '--get', action='store_true', help='get menu')
    parser.add_argument('-d', '--delete', action='store_true', help='delete menu')

    args = parser.parse_args()

    if args.create:
        token = get_token()
        create_menu(token)
    if args.get:
        token = get_token()
