import requests
from . import config
from . import loger


logger = loger.setup_logger(__name__)

headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }




# 客服消息
class kefu:

    # 发送客服状态
    def kefu_status(self,user,status,token):
        url = 'https://api.weixin.qq.com/cgi-bin/message/custom/typing?access_token={}'.format(token)
        data= { "touser":user, "command":status}
        res = requests.post(url=url, json=data, headers=headers)
        return res.json()

    # 发送文本消息
    def send_text(self, user, content,token):
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}".format(token)
        data = {
            "touser": user,
            "msgtype": "text",
            "text":{ "content": content}
                }
        res = requests.post(url=url, json=data, headers=headers)
        return res.json()


# 模板消息
class  muban:
    # 发送模板消息
    def sendmuban(self, template_id,user, urlred,content,token):
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(token)
        data = {
            "touser": user,
            "template_id": template_id,
            'url':urlred,
            "data":content
                }
        res = requests.post(url=url, json=data, headers=headers)
        return res.json()


# 聊天功能---调用gpt模型
class chat_msg:
    def __init__(self) :
        self.chat_url=config.chat_url
        self.chat_apikey=config.chat_apikey
    def chat_gpt(self,msg,model):
        url=self.chat_url
        headers['Sec-Fetch-Mode']='cors'
        headers['Authorization']='Bearer '+self.chat_apikey
        data={
            'model':model,
            'messages':msg,
            'max_tokens': 6000,
            'stream': False,
        }
        req=requests.post(url,headers=headers,json=data,timeout=120)
        try:
            rep=req.json()['choices'][0]['message']['content']
        except Exception as e:
            logger.error("gpt请求失败: %s",str(e))
            rep='gpt请求失败'
        return rep




