# -*- coding: utf-8 -*-

import argparse
from flask import Flask, request
import json
import sys
import urllib
import urllib2

import articleinfo
import main

APP_ID = 'wx92ab0673ca2fcc80'
APP_SECRET = 'a6a1ae038ce493282cee5ceef98f1fc2'

TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={secret}'.format(app_id=APP_ID, secret=APP_SECRET)

MENU_CREATE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='
MENU_GET_URL = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token='
MENU_DELETE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='

def get_menu_structure():
	valid_menu = {
    "button": [
        {
            "name": "爱聚专题",
            "sub_button": [
                {
                    "type": "click",
                    "name": "爱聚厨房",
                    "key": articleinfo.Article.Type.chef.name
                },
                {
                    "type": "click",
                    "name": "爱聚书房",
                    "key": articleinfo.Article.Type.book.name
                }
            ]
        },
        {
            "name": "爱聚活动",
            "sub_button": [
                {
                    "type": "view",
                    "name": "爱聚推荐",
                    "url": "http://www.aijunyc.com/zhs/article?post=285"
                }
            ]
        },
        {
            "type": "view",
            "name": "爱聚团队",
	    "url": "http://www.aijunyc.com"
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
    response = urllib2.urlopen(MENU_GET_URL+token)
    ret_dict = json.loads(response.read())
    print(ret_dict)

def delete_menu(token):
    response = urllib2.urlopen(MENU_DELETE_URL+token)
    ret_dict = json.loads(response.read())
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
        get_menu(token)
    if args.delete:
        token = get_token()
        delete_menu(token)
