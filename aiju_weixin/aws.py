# -*- coding: utf-8 -*-

from boto.s3.connection import S3Connection
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

AWS_WX_BUCKET=config.get('aj_aws','aj_wx_bucket')

def upload_to_s3(objects)
	
	if objects is None:
		return -1

	conn = S3Connection()
	bucket = conn.get_bucket(AWS_WX_BUCKET)
	
	
