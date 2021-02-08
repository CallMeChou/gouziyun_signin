import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import re
import os
# 登陆函数
def login(email,password,tim):
    try:
        for i in range(2):
            login_url = "https://dog1.52dog.xyz/auth/login"
            data_1 = {
                "email": email,
                "passwd": password
            }
            headers = {
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
            }
            s = requests.Session()
            res = s.post(login_url,data=data_1,headers=headers)
            # res.content.decode("utf-8")
            # res.encoding="utf-8"
            res=s.post("https://dog1.52dog.xyz/user/checkin")
            return s
    except:
        txt_2 = email+"狗子云签到失败||||||"+tim
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+txt_2)

# 判断是否签到成功函数，如果成功页面中会出现 ——> <p>上次签到时间：2021-02-02 06:08:42</p>
def judge(email,tim,s):
    # 判断是否签到成功
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
    }
    start_html = s.get(url="https://dog1.52dog.xyz/user", headers=headers)
    soup = BeautifulSoup(start_html.text , 'lxml', exclude_encodings="utf-8")  # 使用BS4框架来解析网页源码
    txt = str(soup.find_all('p')[2])   # 如果成功这个标签会是 ——> <p>上次签到时间：2021-02-02 06:08:42</p>
    if re.match(r"<p>上次签到时间.*?</p>", txt):
        print("ture")
    else:
        print("false")
        txt_2 = email + "狗子云签到失败-->" + tim
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text=" + txt_2)

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
    judge(email=username1,tim=ti,s=login(email=username1,password=password1,tim=ti))
    # 第二个签到
    judge(email=username2,tim=ti,s=login(email=username2,password=password2,tim=ti))
    
