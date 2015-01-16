# -*- coding: utf-8 -*-

from boto.s3.connection import S3Connection
import ConfigParser
import urllib2, StringIO, uuid, time

#config = ConfigParser.ConfigParser()
#config.read('/home/ec2-user/aiju_weixin/config.cfg')

#AWS_WX_BUCKET=config.get('aj_aws','aj_wx_bucket')
AWS_WX_BUCKET = "wx-cloudfront-bucket"

config = ConfigParser.ConfigParser()
config.read('/home/ec2-user/aiju_weixin/config.cfg')

AWS_WX_BUCKET=config.get('aj_aws','aj_wx_bucket')

s3_conn = None

def upload_usr_img_to_s3(img_url, usr_open_id):
	global s3_conn	
	
	if img_url is None or img_url == "" or usr_open_id is None or usr_open_id == "":
		return -1
	
	try:
		if s3_conn is None:
			s3_conn = S3Connection("AKIAIK35HZG4AYXYAXUQ","lPd9iNIcHUGFVhTNXjaFvpZdSuUE/llFLbr4WvhH")
	
		# retrieve img
		img_obj = urllib2.urlopen(img_url)
		fp = StringIO.StringIO(img_obj.read())

		# s3
		bucket = s3_conn.get_bucket(AWS_WX_BUCKET)
		new_obj_key = '{0}/image/wx-upload/{1}'.format(usr_open_id,uuid.uuid1())
		k = bucket.new_key(new_obj_key)
		size = k.set_contents_from_file(fp, headers={"Content-Type":"image/png"})
		k.set_acl('public-read')
		
		return size
	
	except Exception, e:
		print e
		return -1
