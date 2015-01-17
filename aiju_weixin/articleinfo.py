# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import flufl.enum as enum

import caches

class Article():
    class Type(enum.Enum):
        chef = 10
        book = 20

        clubbing = 30
        networking = 31

    def __init__(self, title, description, pic_url, url):
        self.title = title
        self.description = description
        self.pic_url = pic_url
        self.url = url

    def __repr__(self):
        return 'Article({0})'.format(self.title)


CHEF_LIST = [
    (u'文艺青年韩小厨的班尼蛋和优格百汇', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2015-01-12%2002:03:16.659/IMG_4519.JPG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201769545&idx=1&sn=b7263c841190927ea406c7dcb06236b9#rd'),
    (u'华尔街的厨子--Leo Hu', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2014-12-29%2003:35:04.248/IMG_4273.JPG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201474488&idx=1&sn=d60556ccfdbd58310e35fd645d8de5e1#rd'),
    (u'法式红酒炖牛肉', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2014-12-08%2003:44:39.348/IMG_3797.JPG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201050395&idx=1&sn=bc857a7228ca54df0fa05fc28a9a34d0#rd'),
    (u'花胶淮山鸡脚汤', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/45/article/2014-11-24%2019:51:39.713/5.jpg', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=200826085&idx=1&sn=303563084e5815fb306cb5d9d707014d#rd')
]

def load():
    for r in CHEF_LIST:
        caches.articles[Article.Type.chef.value].append(Article(r[0], r[1], r[2], r[3]))
