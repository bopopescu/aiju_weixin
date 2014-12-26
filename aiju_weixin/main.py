# -*- coding: utf-8 -*-

from flask import Flask, request
from weixin import verification, parse_msg, get_access_token, get_usr_info
import requests, json
import hashlib, time
import xml.etree.ElementTree as ET
import ConfigParser

app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

APP_ROOT = "/"
APP_TOKEN = config.get('aj_wx_public','app_token')
access_token_create_time = 0

RETURN_TEXT_RESPONSE = """
                     <xml><ToUserName><![CDATA[{0}]]></ToUserName>
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
	
	#get_access_token()	
	#print get_access_token()	

	if verification(request):
		data = request.data
		msg = parse_msg(data)
		
		usr_msg =  msg["Content"]
		usr_open_id = msg["FromUserName"]
		app_id = msg["ToUserName"]

		return return_text_msg_to_wechat(app_id, usr_open_id, usr_msg)
    
	print "msg verification fail"
	return "nothing"

def return_text_msg_to_wechat(app_id, usr_open_id, usr_msg):
    resp_create_time = int(time.time())
    resp_msg = u"I am AIJU. You just sent: {0} to me.".format(usr_msg)
    print resp_msg
	print 
	
	if access_token is None or int(time.time()) - access_token_create_time > 7200000:
		print "Updating access token"
		access_token = get_access_token()
	else
		print "access token still current"
		print get_usr_info(usr_open_id, access_token)
		

    return RETURN_TEXT_RESPONSE.format(usr_open_id,app_id,resp_create_time,resp_msg.encode('utf8'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
