# coding=utf8
# A Python script to auto-reply message in Wechat
# @ Yanbo

import requests
import itchat
from itchat.content import *

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

# get response message
def get_response(msg):
    # connect with tuling-robot
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # retrun text from the robot
        return r.get('text')
    # return None if cannot connect with server
    except:
        return None

# send message
@itchat.msg_register([PICTURE,TEXT])
def tuling_reply(msg):
    # the message from others
    if not msg['FromUserName'] == myUserName:
        # text type message
        if msg['Type'] == TEXT:
            # default message
            defaultReply = 'I received: ' + msg['Text']
            # tuling AI message
            reply = get_response(msg['Text'])
            if reply:
                itchat.send_msg(msg=reply, toUserName=msg['FromUserName'])
            else:
                itchat.send_msg(msg=defaultReply, toUserName=msg['FromUserName'])
        # None-Text message
        else:
            itchat.send_msg(msg='给我发文字啦', toUserName=msg['FromUserName'])


# initialization  
itchat.auto_login(hotReload=True)
myUserName = itchat.get_friends(update=True)[0]["UserName"]
itchat.run()
