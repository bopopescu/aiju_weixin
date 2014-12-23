# -*- coding: utf-8 -*-

from flask import Flask, request
import json

import main

APP_ID = ''
APP_SECRET = ''

def create_menu():
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
