# -*- coding: utf-8 -*-

GENERAL_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[{msg_type}]]></MsgType>
                   {additional_info}
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
TEXT_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[text]]></MsgType>
                   <Content><![CDATA[{text}]]></Content>
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
IMAGE_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[image]]></MsgType>
                   <PicUrl><![CDATA[{pic_url}]]></PicUrl>
                   <MediaId><![CDATA[{media_id}]]></MediaId>
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
VOICE_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[voice]]></MsgType>
                   <MediaId><![CDATA[{media_id}]]></MediaId>
                   <Format><![CDATA[{format}]]></Format>
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
VIDEO_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[video]]></MsgType>
                   <MediaId><![CDATA[{media_id}]]></MediaId>
                   <ThumbMediaId><![CDATA[{thumb_media_id}]]></ThumbMediaId>
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
LOCATION_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[location]]></MsgType>
                   <Location_X>{latitude}</Location_X>
                   <Location_Y>{longitude}</Location_Y>
                   <Scale>{scale}</Scale>
                   <Label><![CDATA[{label}]]></Label>
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
LINK_TEMPLATE = """
                   <xml>
                   <ToUserName><![CDATA[{to_user}]]></ToUserName>
                   <FromUserName><![CDATA[{from_user}]]></FromUserName> 
                   <CreateTime>{timestamp}</CreateTime>
                   <MsgType><![CDATA[link]]></MsgType>
                   <Title><![CDATA[{title}]]></Title>
                   <Description><![CDATA[{description}]]></Description>
                   <Url><![CDATA[{url}]]></Url>
                   <MsgId>{msg_id}</MsgId>
                   </xml>
                   """
NEWS_TEMPLATE = """
              <xml>
              <ToUserName><![CDATA{to_user}]></ToUserName>
              <FromUserName><![CDATA{from_user}]></FromUserName>
              <CreateTime>{timestamp}</CreateTime>
              <MsgType><![CDATA[news]]></MsgType>
              <ArticleCount>{length}</ArticleCount>
              <Articles>{news}</Articles>
              </xml> 
              """
NEWS_ITEM_TEMPLATE = """
              <item>
              <Title><![CDATA{title1}]></Title> 
              <Description><![CDATA{description}]></Description>
              <PicUrl><![CDATA{picurl}]></PicUrl>
              <Url><![CDATA{url}]></Url>
              </item>
              """

WECHAT_TEMPLATES = {
'text': TEXT_TEMPLATE,
'image': IMAGE_TEMPLATE,
'voice': VOICE_TEMPLATE,
'video': VIDEO_TEMPLATE,
'location': LOCATION_TEMPLATE,
'link': LINK_TEMPLATE,
}
