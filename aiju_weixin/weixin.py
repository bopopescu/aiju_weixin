# -*- coding: utf-8 -*- 

import requests
import hashlib, ConfigParser, json
import xml.etree.ElementTree as ET

# retrieve config info
config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

APP_TOKEN = config.get('aj_wx_public','app_token')
APP_SECRET = config.get('aj_wx_public','app_secret')
APP_ID = config.get('aj_wx_public','app_id')

# 验证消息真实性
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

def get_new_access_token(app_id=None,app_secret=None):

	if (app_id is None or app_secret is None):
		app_id = APP_ID
		app_secret = APP_SECRET
	
	wx_access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(app_id,app_secret)
	r = requests.get(wx_access_token_url, headers={'Connection':'close'})
	
	if r.status_code == 200:
		resp = json.loads(r.text)
		if "errcode" in resp:
			print "get_access_token failed in weixin.py."
			print resp
			return -1
		else:
			return resp["access_token"]
	else:
		print "get_access_token failed in weixin.py."
		print "Status code: " + r.status_code
		print "err msg: " + r.text
		return -1	

def get_usr_info(usr_open_id, access_token):

	if usr_open_id is None:
		return -1

	request_url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}&lang=zh_CN".format(access_token, usr_open_id)
	r = requests.get(request_url, headers={'Connection':'close'})
	return r.text.encode('utf8')
	
def parse_msg(rawmsgstr):
	root = ET.fromstring(rawmsgstr)
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg
