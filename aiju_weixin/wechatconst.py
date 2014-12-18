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
TEXT_TEMPLATE = GENERAL_TEMPLATE.format(msg_type='text', 
                                        additional_info='<Content><![CDATA[{text}]]></Content>')
IMAGE_TEMPLATE = GENERAL_TEMPLATE.format(msg_type='image',
                                         additional_info="""<PicUrl><![CDATA[{pic_url}]]></PicUrl>
                                                            <MediaId><![CDATA[{media_id}]]></MediaId>""")
VOICE_TEMPLATE = GENERAL_TEMPLATE.format(msg_type='voice',
                                         additional_info="""<MediaId><![CDATA[{media_id}]]></MediaId>
                                                            <Format><![CDATA[{format}]]></Format>""")
VIDEO_TEMPLATE = GENERAL_TEMPLATE.format(msg_type='video',
                                         additional_info="""<MediaId><![CDATA[{media_id}]]></MediaId>
                                                            <ThumbMediaId><![CDATA[{thumb_media_id}]]></ThumbMediaId>""")
LOCATION_TEMPLATE = GENERAL_TEMPLATE.format(msg_type='location',
                                            additional_info="""<Location_X>{latitude}</Location_X>
                                                               <Location_Y>{longitude}</Location_Y>
                                                               <Scale>{scale}</Scale>
                                                               <Label><![CDATA[{label}]]></Label>""")
LINK_TEMPLATE = GENERAL_TEMPLATE.format(msg_type='link',
                                        additional_info="""<Title><![CDATA[{title}]]></Title>
                                                           <Description><![CDATA[{description}]]></Description>
                                                           <Url><![CDATA[{url}]]></Url>""")

WECHAT_TEMPLATES = {
'text': TEXT_TEMPLATE,
'image': IMAGE_TEMPLATE,
'voice': VOICE_TEMPLATE,
'video': VIDEO_TEMPLATE,
'location': LOCATION_TEMPLATE,
'link': LINK_TEMPLATE,
}
#TEXT_TEMPLATE = """
#                <xml>
#                <ToUserName><![CDATA[toUser]]></ToUserName>
#                <FromUserName><![CDATA[fromUser]]></FromUserName> 
#                <CreateTime>1348831860</CreateTime>
#                <MsgType><![CDATA[text]]></MsgType>
#                <Content><![CDATA[this is a test]]></Content>
#                <MsgId>1234567890123456</MsgId>
#                </xml>
#                """
#IMAGE_TEMPLATE = """
#                 <xml>
#                 <ToUserName><![CDATA[toUser]]></ToUserName>
#                 <FromUserName><![CDATA[fromUser]]></FromUserName>
#                 <CreateTime>1348831860</CreateTime>
#                 <MsgType><![CDATA[image]]></MsgType>
#                 <PicUrl><![CDATA[this is a url]]></PicUrl>
#                 <MediaId><![CDATA[media_id]]></MediaId>
#                 <MsgId>1234567890123456</MsgId>
#                 </xml>
#                """
#VOICE_TEMPLATE = """
#                 <xml>
#                 <ToUserName><![CDATA[toUser]]></ToUserName>
#                 <FromUserName><![CDATA[fromUser]]></FromUserName>
#                 <CreateTime>1357290913</CreateTime>
#                 <MsgType><![CDATA[voice]]></MsgType>
#                 <MediaId><![CDATA[media_id]]></MediaId>
#                 <Format><![CDATA[Format]]></Format>
#                 <MsgId>1234567890123456</MsgId>
#                 </xml>
#                 """                        
#VIDEO_TEMPLATE = """
#                 <xml>
#                 <ToUserName><![CDATA[toUser]]></ToUserName>
#                 <FromUserName><![CDATA[fromUser]]></FromUserName>
#                 <CreateTime>1357290913</CreateTime>
#                 <MsgType><![CDATA[video]]></MsgType>
#                 <MediaId><![CDATA[media_id]]></MediaId>
#                 <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
#                 <MsgId>1234567890123456</MsgId>
#                 </xml>
#                 """          
#LOCATION_TEMPLATE = """
#                    <xml>
#                    <ToUserName><![CDATA[toUser]]></ToUserName>
#                    <FromUserName><![CDATA[fromUser]]></FromUserName>
#                    <CreateTime>1351776360</CreateTime>
#                    <MsgType><![CDATA[location]]></MsgType>
#                    <Location_X>23.134521</Location_X>
#                    <Location_Y>113.358803</Location_Y>
#                    <Scale>20</Scale>
#                    <Label><![CDATA[位置信息]]></Label>
#                    <MsgId>1234567890123456</MsgId>
#                    </xml> 
#                    """     
#LINK_TEMPLATE = """
#               <xml>
#               <ToUserName><![CDATA[toUser]]></ToUserName>
#               <FromUserName><![CDATA[fromUser]]></FromUserName>
#               <CreateTime>1351776360</CreateTime>
#               <MsgType><![CDATA[link]]></MsgType>
#               <Title><![CDATA[公众平台官网链接]]></Title>
#               <Description><![CDATA[公众平台官网链接]]></Description>
#               <Url><![CDATA[url]]></Url>
#               <MsgId>1234567890123456</MsgId>
#               </xml> 
#               """
