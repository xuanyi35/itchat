# last version of auto chat
import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.PICTURE)
def general_reply(msg):
    f = "G:\itchat/smile.jpg"
    fromU = itchat.search_friends(userName=msg['FromUserName'])['NickName']   
    if 'Anneyston' in fromU :
        print("ignore")
    elif fromU == '轩少' :
        print("ignore")
    elif fromU == 'Anneyston' :
        print("ignore")
    else:
        try:
             itchat.send_image(f,msg['FromUserName'])
             print("success")
        except:
             print("error")



@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    fromU = itchat.search_friends(userName=msg['FromUserName'])['NickName']   
    if 'Zhai' in fromU :
        reply =None
    elif 'Anneyston' in fromU :
        reply =None
    elif fromU == '轩少' :
        reply =None
    else:
        reply = '{轩萌萌}: ' + get_response(msg['Text'])  
    itchat.send(reply, msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()