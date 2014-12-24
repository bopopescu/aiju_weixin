# -*- coding: utf-8 -*- 
import hashlib, ConfigParser
import xml.etree.ElementTree as ET

# retrieve config info
config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')
APP_TOKEN = config.get('aj_wx_public','app_token')

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

def parse_msg(rawmsgstr):
    root = ET.fromstring(rawmsgstr)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg
