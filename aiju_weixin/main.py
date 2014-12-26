# -*- coding: utf-8 -*-

import hashlib, time
import xml.etree.ElementTree as ET

import wechatconst

from flask import Flask, request


app = Flask(__name__)

APP_ROOT = '/'
APP_TOKEN = 'Aiju_NewYork_NewYork_2014'

RETURN_TEXT_RESPONSE = """
                     <xml>
                     <ToUserName><![CDATA[{0}]]></ToUserName>
                     <FromUserName><![CDATA[{1}]]></FromUserName>
                     <CreateTime>{2}</CreateTime>
                     <MsgType><![CDATA[text]]></MsgType>
                     <Content><![CDATA[{3}]]></Content>
                     </xml>
                     """

@app.cli.command('create_menu')
def create_menu_command():
    menu.create_menu()
    print('Menu created')

# verify for weixin server.
# weixin server will send GET request first to verify this backend
@app.route(APP_ROOT, methods=['GET'])
def weixin_access_verify():
    print "Handshake between WeChat's server with this Python server"
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

        msg_template = wechatconst.WECHAT_TEMPLATES[msg_type]
        
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
 
def return_image_msg_to_wechat(app_id, usr_open_id, msg_template, pic_url, media_id):
    resp_create_time = int(time.time())
    return msg_template.format(
        to_user=usr_open_id, 
        from_user=app_id, 
        pic_url=pic_url, 
        media_id=media_id, 
        timestamp=resp_create_time,
        msg_id=123456,
    )

def return_text_msg_to_wechat(app_id, usr_open_id, resp_msg):
    resp_create_time = int(time.time())
    return RETURN_TEXT_RESPONSE.format(usr_open_id,app_id,resp_create_time, resp_msg.encode('utf8'))

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
    app.run(debug=True, host="0.0.0.0", port=80)
