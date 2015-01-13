# -*- coding: utf-8 -*-

from flask import Flask, request
from weixin import *
import json
import time
import ConfigParser

import articleinfo
import aws
import caches
import wechatconst

app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

APP_ROOT = "/"
APP_TOKEN = config.get('aj_wx_public','app_token')
access_token = None
access_token_create_time = 0

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
    if verification(request) and echostr is not None:
        print " Verification success!"
        return echostr
	print "Verification fail :("
    return 'access verification fail'


# reciever msgs from weixin server
@app.route(APP_ROOT, methods=['POST'])
def weixin_msg():
    print "inside weixin_msg"
    if verification(request):
        data = request.data
        msg = parse_msg(data)

        usr_open_id = msg["FromUserName"]
        app_id = msg["ToUserName"]

        msg_type = msg["MsgType"]

        if msg_type == 'text':
            usr_msg =  msg["Content"]
            usr_msg = u"I am AIJU. You just sent: {0} to me.".format(usr_msg)
            return return_text_msg_to_wechat(app_id, usr_open_id, usr_msg)
        elif msg_type == 'image':
            media_id = msg["MediaId"]
            pic_url = msg["PicUrl"]
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your picture!')
        elif msg_type == 'location':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your location!')
        elif msg_type == 'video':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your video!')
        elif msg_type == 'voice':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your voice!')
        elif msg_type == 'link':
            return return_text_msg_to_wechat(app_id, usr_open_id, 'Thanks for sharing your link!')
        elif msg_type == 'event':
            return receive_event_msg(msg)
 

def return_text_msg_to_wechat(app_id, usr_open_id, usr_msg):
	resp_create_time = int(time.time())
	#resp_msg = u"I am AIJU. You just sent: {0} to me.".format(usr_msg)

	resp_msg = json.loads(get_usr_info(usr_open_id, get_access_token()))

	print resp_msg['province'].encode('utf-8')
	print get_usr_info(usr_open_id, get_access_token())

	#return RETURN_TEXT_RESPONSE.format(usr_open_id,app_id,resp_create_time,get_usr_info(usr_open_id, get_access_token()).encode("utf8"))

	return ""


def get_access_token():
	global access_token, access_token_create_time

	if access_token is None or int(time.time()) - access_token_create_time > 7200000:
		print "Access Token Expires"
		print "Updating access token..."
		access_token_create_time = int(time.time())
		access_token = get_new_access_token()
		
	return access_token
>>>>>>> ac59f9c6728335ef529295dcb68d8addb715e0b6

def receive_event_msg(msg):
    if msg["Event"] == 'CLICK':
      if msg["EventKey"] == u'爱聚厨房':
          return articles.return_news_xml(articleinfo.Article.Type.chef.value, app_id, usr_open_id)
      elif msg["EventKey"] == u'爱聚书房':
          return articles.return_news_xml(articleinfo.Article.Type.book.value, app_id, usr_open_id)

def parse_msg(rawmsgstr):
    root = ET.fromstring(rawmsgstr)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

def verification(req):
    print "inside verificantion"
    signature = req.args.get('signature')
    timestamp = req.args.get('timestamp')
    nonce = req.args.get('nonce')

    if signature is None or timestamp is None or nonce is None:
        return False

    token = APP_TOKEN
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = ''.join(tmplist)
    hashstr = hashlib.sha1(tmpstr).hexdigest()

    if hashstr == signature:
        return True
    return False

if __name__ == "__main__":
    articleinfo.load()
    app.run(debug=True, host="0.0.0.0", port=80)
