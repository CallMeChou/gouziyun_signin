import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import etree
import re
import os

headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
        }
# 登陆函数
def login(email, password, tim):
    try:
        login_url = "https://dog.dog21.xyz/auth/login"
        data_1 = {
            "email": email,
            "passwd": password,
            "remember_me": "on",
            "code": ""
        }
        s = requests.Session()
        res = s.post(login_url, data=data_1, headers=headers)
        # res.content.decode("utf-8")
        # res.encoding="utf-8"
        res = s.post("https://dog.dog21.xyz/user/checkin")
        return s
    except:
        print("登录失败")
        url = "https://qmsg.zendee.cn/send/0cb7ec3b53ee6db28ff921b6af54f9db"
        data ={
            "msg": "【"+email+"】: "+ti+" "*50+"狗子登录失败@face=5@",
            'qq':'2079986882'
        }
        requests.post(url, data=data)


# 判断是否签到成功函数，如果成功页面中会出现 ——> <p>上次签到时间：2021-02-02 06:08:42</p>
def judge(email, tim, s):
    # 判断是否签到成功
    start_html = s.get(url="https://dog.dog21.xyz/user", headers=headers)
    soup = BeautifulSoup(start_html.text, 'lxml', exclude_encodings="utf-8")  # 使用BS4框架来解析网页源码
    selector = etree.HTML(str(soup))
    txt = selector.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/a/text()")
    # txt = str(soup.find_all("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/a/text()"))   # 如果成功这个标签会是 ——> <p>上次签到时间：2021-02-02 06:08:42</p>
    # print(txt)
    if txt[0] == "已签到":
        print("ture")
        url = "https://qmsg.zendee.cn/send/0cb7ec3b53ee6db28ff921b6af54f9db"
        data={
            "msg": "【"+email+"】: "+ti+" "*50+"狗子签到成功@face=2@",
            "qq":"2079986882"
        }
        requests.post(url, data=data)
    else:
        print("false")
        url = "https://qmsg.zendee.cn/send/0cb7ec3b53ee6db28ff921b6af54f9db"
        data = {
            "msg": "【"+email+"】: "+ti+" "*50+"狗子签到失败@face=5@",
            'qq': '2079986882'
        }
        requests.post(url, data=data)


if __name__ == '__main__':
    # 1.北京时间
    #     t=datetime.today()
    #     ti= str(t.year)+"-"+str(t.month)+"-"+str(t.day)+" "+str(t.hour)+":"+str(t.minute)+":"+str(t.second)
    ti = str(time.strftime("%Y-%m-%d", time.localtime()))
    # 2.账号密码信息
    username1 = os.environ["EMAIL1"]
    password1 = os.environ["PASSWORD1"]
    username2 = os.environ["EMAIL2"]
    password2 = os.environ["PASSWORD2"]
    # 执行签到
    # 第一个签到
    judge(email=username1, tim=ti, s=login(email=username1, password=password1, tim=ti))
    # 第二个签到
    judge(email=username2,tim=ti,s=login(email=username2,password=password2,tim=ti))

