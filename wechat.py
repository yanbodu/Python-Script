#coding=utf8
import itchat

# auto reply
@itchat.msg_register('Text')
def text_reply(msg):

    if not msg['FromUserName'] == myUserName:

        message = msg['Text']

        # reply messages
        if '你好' in message:
             itchat.send_msg(msg='你好呀[Joyful]\n', toUserName=msg['FromUserName'] )
        elif '再见' in message:
            itchat.send_msg(msg='再见[Bye]\n', toUserName=msg['FromUserName'] )
        elif '...' in message:
            itchat.send_msg(msg='点什么点[Scold]\n', toUserName=msg['FromUserName'] )
        elif '你是谁' in message:
            itchat.send_msg(msg='你猜呀\n', toUserName=msg['FromUserName'] )
        elif '谁' in message:
            itchat.send_msg(msg='我是Python回复助手0.0版\n', toUserName=msg['FromUserName'] )
        elif '呦' in message:
            itchat.send_msg(msg='呦呦切克闹\n', toUserName=msg['FromUserName'] )
        elif '我是你爸爸' in message:
            itchat.send_msg(msg='爸爸没你这个儿子\n', toUserName=msg['FromUserName'] )
        elif '叫爸爸' in message:
            itchat.send_msg(msg='儿砸！！\n', toUserName=msg['FromUserName'] )
        elif '大爷' in message:
            itchat.send_msg(msg='把你厉害的\n', toUserName=msg['FromUserName'] )
        elif '傻逼' in message or '尼玛' in message or '麻痹' in message:
            itchat.send_msg(msg='[Smile]\n', toUserName=msg['FromUserName'] )
        elif '？' in message:
            itchat.send_msg(msg='？？？\n', toUserName=msg['FromUserName'] )
        elif '哈' in message or '嘿' in message:
            itchat.send_msg(msg='笑屁哦[Smile]\n', toUserName=msg['FromUserName'] )

        else:
            itchat.send_msg(msg='我听不懂你在讲什么 略略略\n', toUserName=msg['FromUserName'] )


if __name__ == '__main__':
    itchat.auto_login()
    # own UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
