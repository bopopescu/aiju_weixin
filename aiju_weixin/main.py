# -*- coding: utf-8 -*-

from flask import Flask, request
import hashlib, time
import xml.etree.ElementTree as ET

app = Flask(__name__)

APP_ROOT = '/'
APP_TOKEN = 'Aiju_NewYork_NewYork_2014'
# verify for weixin server.
# weixin server will send GET request first to verify this backend
@app.route(APP_ROOT, methods=['GET'])
def weixin_access_verify():
    echostr = request.args.get('echostr')
    if verification(request) and echostr is not None:
        return echostr
	print "verification successful!"
    return 'access verification fail'

# reciever msgs from weixin server
@app.route(APP_ROOT, methods=['POST'])
def weixin_msg():
    if verification(request):
        data = request.data
        msg = parse_msg(data)
        print msg

def parse_msg(rawmsgstr):
    root = ET.fromstring(rawmsgstr)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

def verification(req):
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
    app.run(debug=True)
