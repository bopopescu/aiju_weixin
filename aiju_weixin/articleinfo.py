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
    (u'爱聚厨房】马克先生的“地狱厨师”养成记',u'我在电视机前端着速冻饺子刷朋友圈，却看着马克先生给自己煎了一块肥厚的三文鱼配四颗晶莹剔透的鲜贝，心里感慨生活质量的差距，恨不能当即拉黑之.', 'http://mmbiz.qpic.cn/mmbiz/W6UfGJf1ib6jh1M14zFicmG0tI4JYWNIdKujlG0UWo4yMCiaT6BLaj3yMzQ0svjo2trIoMpSPyWMgeq4sooFqXegA/640?tp=webp&wxfrom=5', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=202595645&idx=1&sn=0659baae4de1fe3f4bcd46c93370f13a&key=8ea74966bf01cfb68cd2eb74f87f705d1530b6c2319f68f5544cca1bd154a9afb43ac67baaf23a4d1f128eb3510603c2&ascene=1&uin=MjgwOTEwNjk0Nw%3D%3D&devicetype=webwx&version=70000001&pass_ticket=JyH3koUVcLfLR81SM3OY9%2BxgniFFTG0QxCVoh%2FgdpxJigd1DMTD3svxJWlHVW6HR'),
    (u'文艺青年韩小厨的班尼蛋和优格百汇', '', 'http://mmbiz.qpic.cn/mmbiz/W6UfGJf1ib6hk1zzSayjlltY7xl1HH2F3qSnAtYU32qjESSXu58ibPoCP7icBttn8hWjebnOucdQ2oZibydvmAzEow/640?tp=webp&wxfrom=5', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201769545&idx=1&sn=b7263c841190927ea406c7dcb06236b9#rd'),
    (u'华尔街的厨子--Leo Hu', '', 'http://mmbiz.qpic.cn/mmbiz/W6UfGJf1ib6jibovz70a1riauUOBPvwQ5JGiaspqeiasrt4CrMUEcqFricmEMPfcrW0P0Wn6htosISXKIbPeD4xactvA/640?tp=webp&wxfrom=5', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201474488&idx=1&sn=d60556ccfdbd58310e35fd645d8de5e1#rd'),
    (u'法式红酒炖牛肉', '', 'https://s3.amazonaws.com/wx-cloudfront-bucket/chufang-girl-1', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201050395&idx=1&sn=bc857a7228ca54df0fa05fc28a9a34d0#rd'),
    (u'花胶淮山鸡脚汤', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/45/article/2014-11-24%2019:51:39.713/5.jpg', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=200826085&idx=1&sn=303563084e5815fb306cb5d9d707014d#rd')
]

BOOK_LIST = [
    (u'红泥醅酒映雪夜', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2014-12-04%2004:08:33.411/IMG_3753.JPG', 'http://www.aijunyc.com/zhs/article?post=229')
]

EVENT_LIST = [
    (u'01/23 破冰暖心暖心派对活动回顾', '', 'http://mmbiz.qpic.cn/mmbiz/W6UfGJf1ib6jGmEWw6M8oMMpbxKTiaiaM41WVq7q5exuRv3Jul6w6WILAoicBA28T2MoVeiaV7r4IZegWG71Ks14xvw/640?tp=webp', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=202055480&idx=2&sn=f381be6a340af332d825e30b032d5cbe&scene=1&key=79cf83ea5128c3e534dd56e20584c5481e012b1270bf393b22502c2e19119305e15222dccfe38e36425648ea906f3de3&ascene=0&uin=NzE4NTAxNjYw&devicetype=iMac+MacBookAir5%2C2+OSX+OSX+10.9.5+build(13F34)&version=11020012&pass_ticket=HCO%2Fr1%2BBV9z5WSuoCFAibXaB6rkqAiE2RGc63poxbYsn2eBFC7nKf4jYCqFbbjU4'),
    (u'2/13 How I met your mother? 以爱之名，缘聚纽约情人节派对！', '', 'https://mmbiz.qlogo.cn/mmbiz/W6UfGJf1ib6jGmEWw6M8oMMpbxKTiaiaM41vtkvzdRT8phd5S0QDZVo2Ft7Idv2jib0sgicl9Y7t7Wticv5qrGgUu4kQ/0', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=202052270&idx=1&sn=92e83727d36f74ed8eaddb31b7cb23f0#rd'),
#    (u'1/23 破冰暖心职场社交派对 Icebreaker Networking Mixer', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2015-01-14%2001:41:59.409/IMG_4551.PNG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201789830&idx=1&sn=653d5d5fbcf2831a3090240018fa21de#rd'),
    (u'2/18 28元入座卡耐基主厅，聆听“女郎朗”田佳鑫钢琴演奏会', '', 'https://s3.amazonaws.com/aiju-cloudfront-bucket/69/article/2015-01-09%2004:49:14.942/IMG_4477.JPG', 'http://mp.weixin.qq.com/s?__biz=MzA4MzU0NDIxMg==&mid=201818576&idx=2&sn=96a9f9f0d42c88e286fce0235ef8b43c#rd')
]

def load():

    for r in CHEF_LIST:
        caches.articles[Article.Type.chef.value].append(Article(r[0], r[1], r[2], r[3]))
    for r in BOOK_LIST:
        caches.articles[Article.Type.book.value].append(Article(r[0], r[1], r[2], r[3]))
    for r in EVENT_LIST:
        caches.articles[Article.Type.event.value].append(Article(r[0], r[1], r[2], r[3]))
