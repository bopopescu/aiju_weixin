# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request
from weixin import *
from external_tools import *

import json
import time
import ConfigParser

import articleinfo
import articles
import caches
import aws

config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

# globals
APP_ROOT = "/"
APP_TOKEN = config.get('aj_wx_public','app_token')
AJ_DB_HOSTNAME= config.get('aj_db','website_mysql_host')

access_token = None
access_token_create_time = 0

app = Flask(__name__)

# set up bindings
app.config['SQLALCHEMY_DATABASE_URI'] = AJ_DB_HOSTNAME

# create the database object
DB = SQLAlchemy(app)

RETURN_TEXT_RESPONSE = """
                     <xml>
                     <ToUserName><![CDATA[{0}]]></ToUserName>
                     <FromUserName><![CDATA[{1}]]></FromUserName>
                     <CreateTime>{2}</CreateTime>
                     <MsgType><![CDATA[text]]></MsgType>
                     <Content><![CDATA[{3}]]></Content>
                     </xml>
                     """

# verify for weixin server.
# weixin server will send GET request first to verify this backend
@app.route(APP_ROOT, methods=['GET'])
def weixin_access_verify():
    echostr = request.args.get('echostr')
    if verification(request):
        print " Verification success!"
        return echostr
    print "Verification fail :("
    return 'access verification fail'


# reciever msgs from weixin server
@app.route(APP_ROOT, methods=['POST'])
def weixin_msg():
    if verification(request):
        data = request.data
        msg = parse_msg(data)

        usr_open_id = msg["FromUserName"]
        app_id = msg["ToUserName"]

        msg_type = msg["MsgType"]
        
        if msg_type == 'text':
            usr_msg =  msg["Content"]
            u = msg["Content"].encode('utf-8')

            usr_msg = u"I am AIJU. You just sent: {0} to me.".format(usr_msg)
            return return_text_msg_to_wechat(app_id, usr_open_id, usr_msg)
       
        elif msg_type == 'image':
            media_id = msg["MediaId"]
            pic_url = msg["PicUrl"]            

            user_info = get_usr_info(usr_open_id, get_access_token())

            uploaded_img_url = aws.upload_usr_img_to_s3(pic_url, usr_open_id)

            return return_text_msg_to_wechat(app_id, usr_open_id, u"谢谢你分享你的照片～照片的连锁是：" + "\n" +  uploaded_img_url)
       
        elif msg_type == 'location':

            results = DB.engine.execute('select * from hunyin.post where genre = 6 and EventDate > date_add(curdate(), INTERVAL -2 day)')
            nearby_events = []
            for result in results:
                
                url = 'http://www.aijunyc.com/zhs/article?post=' + str(result['PostID'])
                pic_url = result['CoverImage']
                title = result['title']
                description = result['shortdesc']
                geolocation = result['GeoLocation']
                
                if ',' in geolocation:   
                    locationX = float(str(geolocation.split(',')[0]))
                    locationY = float(str(geolocation.split(',')[1]))
                    distance = haversine(locationX, locationY, float(str(msg['Location_X'])), float(str(msg['Location_Y'])))
                    title = u'🚶 离你: ' + str(round(distance,1)) + u"km🚶 " + title[11:]

                nearby_events.append(articleinfo.Article(title,description,pic_url,url))

            if len(nearby_events) == 0:
                url = 'http://www.aijunyc.com/zhs/index'
                pic_url = 'https://s3.amazonaws.com/wx-cloudfront-bucket/sorry3'
                title = u'我们竟然暂时没有独家活动(ಥ﹏ಥ)'
                description = u'不妨到我们的官网哪看看其他和我们合作的平台的活动吧'
                nearby_events.append(articleinfo.Article(title,description,pic_url,url))
                return articles.create_news_xml(nearby_events[:1], app_id, usr_open_id)

            return articles.create_news_xml(nearby_events[:10], app_id, usr_open_id)

        elif msg_type == 'video':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your video!')
        elif msg_type == 'voice':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your voice!')
        elif msg_type == 'link':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your link!')
        elif msg_type == 'event':
            return receive_event_msg(msg, app_id, usr_open_id)

def return_text_msg_to_wechat(app_id, usr_open_id, usr_msg):
	resp_create_time = int(time.time())
	return RETURN_TEXT_RESPONSE.format(usr_open_id,app_id,resp_create_time, usr_msg.encode('utf-8'))

def get_access_token():
	global access_token, access_token_create_time

	if access_token is None or int(time.time()) - access_token_create_time > 7200000:
		print "Access Token Expires"
		print "Updating access token..."
		access_token_create_time = int(time.time())
		access_token = get_new_access_token()
		
	return access_token

def receive_event_msg(msg, app_id, usr_open_id):
    if msg["Event"] == 'CLICK':
        if msg["EventKey"] == articleinfo.Article.Type.chef.name:
            return articles.return_news_xml(articleinfo.Article.Type.chef.value, app_id, usr_open_id)
        elif msg["EventKey"] == articleinfo.Article.Type.book.name:
            return articles.return_news_xml(articleinfo.Article.Type.book.value, app_id, usr_open_id)
        elif msg["EventKey"] == articleinfo.Article.Type.event.name:
            return articles.return_news_xml(articleinfo.Article.Type.event.value, app_id, usr_open_id)
    elif msg["Event"] == "location_select":
        return ""
    elif msg["Event"] == 'subscribe':
        return return_text_msg_to_wechat(app_id, usr_open_id, u'感谢关注爱聚!')
    return ""


if __name__ == "__main__":
    articleinfo.load()
    app.run(debug=True, host="0.0.0.0", port=80)
