#coding=utf8
import itchat

# auto reply
@itchat.msg_register('Text')
def text_reply(msg):
    # reply others' message
    if not msg['FromUserName'] == myUserName:
        return '[自动回复]您好，我现在有事不在，一会再和您联系。\n'

if __name__ == '__main__':
    itchat.auto_login()

    # own UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
