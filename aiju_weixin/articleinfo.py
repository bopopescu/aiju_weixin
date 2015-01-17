# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import flufl.enum as enum

import caches

class Article():
    class Type(enum.Enum):
        chef = 10
        book = 20

        event = 100

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

BOOK_LIST = [
    (u'红泥醅酒映雪夜', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2014-12-04%2004:08:33.411/IMG_3753.JPG', 'http://www.aijunyc.com/zhs/article?post=229')
]

EVENT_LIST = [
    (u'1/23 破冰暖心职场社交派对 Icebreaker Networking Mixer', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2015-01-14%2001:41:59.409/IMG_4551.PNG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201789830&idx=1&sn=653d5d5fbcf2831a3090240018fa21de#rd'),
    (u'2/18 28元入座卡耐基主厅，聆听“女郎朗”田佳鑫钢琴演奏会', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2015-01-09%2004:49:14.942/IMG_4477.JPG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201818576&idx=2&sn=96a9f9f0d42c88e286fce0235ef8b43c#rd')
]


def load():
    for r in CHEF_LIST:
        caches.articles[Article.Type.chef.value].append(Article(r[0], r[1], r[2], r[3]))
    for r in BOOK_LIST:
        caches.articles[Article.Type.book.value].append(Article(r[0], r[1], r[2], r[3]))
    for r in EVENT_LIST:
        caches.articles[Article.Type.event.value].append(Article(r[0], r[1], r[2], r[3]))
