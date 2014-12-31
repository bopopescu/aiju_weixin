# -*- coding: utf-8 -*-

from boto.s3.connection import S3Connection
import ConfigParser
import requests

config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

AWS_WX_BUCKET=config.get('aj_aws','aj_wx_bucket')

s3_conn = None

def upload_img_to_s3(img_url)
	global s3_conn	

	if img_url is None or img_url == "":
		return -1
	
	if s3_conn is None:
		s3_conn = S3Connection()
	
	# retrieve img
	response = requests.get(img_url, stream=True)
	
	if not response.ok:
		print "error"
	
	for block in response.iter_content(1024):
		if not block:
			break

	bucket = s3_conn.get_bucket(AWS_WX_BUCKET)
	
	
