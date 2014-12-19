
m flask import Flask, request
import hashlib, time
import xml.etree.ElementTree as ET

app = Flask(__name__)

APP_ROOT = '/'
APP_TOKEN = 'Aiju_NewYork_NewYork_2014'

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
        #print data
        #print
        #print type(msg)
        usr_msg =  msg["Content"]
        usr_open_id = msg["FromUserName"]
        app_id = msg["ToUserName"]

        #print usr_msg
        #print usr_open_id
        #print app_id

    return return_text_msg_to_wechat(app_id, usr_open_id, usr_msg)

def return_text_msg_to_wechat(app_id, usr_open_id, usr_msg):
    print "return text msg to user"
    resp_create_time = int(time.time())
    resp_msg = u"I am AIJU. You just sent: {0} to me.".format(usr_msg)
    print resp_msg
    return RETURN_TEXT_RESPONSE.format(usr_open_id,app_id,resp_create_time,resp_msg.encode('utf8'))

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
