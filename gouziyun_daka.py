import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re
import os
# 登陆函数
def login(email,password,time):
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
            cookies = "PHPSESSID=qm0jnamb9tsvevur1t7o49ol4o; crisp-client%2Fsession%2Fe6354567-516a-47f8-a493-2717841e5ef5=session_9509f182-42a7-4482-b89b-6d7f2950c03b; uid=37905; email=chou2079986882%40gmail.com; key=933cd372ee5ac13a01248a3aff95e098fd8ead30642a7; ip=dd1161c0929a98d2706ab909a7484e4f; expire_in=1612781714; crisp-client%2Fsocket%2Fe6354567-516a-47f8-a493-2717841e5ef5=0"
            s = requests.Session()
            res = s.post(login_url,data=data_1,headers=headers)
            # res.content.decode("utf-8")
            # res.encoding="utf-8"
            res=s.post("https://dog1.52dog.xyz/user/checkin")
    except:
        txt_2 = email+"狗子云签到失败||||||"+time
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+txt_2)

# 判断是否签到成功函数，如果成功页面中会出现 ——> <p>上次签到时间：2021-02-02 06:08:42</p>
def judge(email,time):
    # 判断是否签到成功
    headers = {

        'Cookie': 'uid=37904; email=2079986882%40qq.com; key=174161a493fffc40f68e7c711d65426639a8fd8b923f7; ip=bb84d3cb02a7ffa7e870be4a1072c378; expire_in=1612330345; crisp-client%2Fsession%2Fe6354567-516a-47f8-a493-2717841e5ef5=session_4e5f64fc-0354-4c33-9c11-768a6621cc74',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
    }
    sesson = requests.Session()
    start_html = sesson.get(url="https://dog1.52dog.xyz/user", headers=headers)
    soup = BeautifulSoup(start_html.text , 'lxml', exclude_encodings="utf-8")  # 使用BS4框架来解析网页源码
    txt = str(soup.find_all('p')[2])   # 如果成功这个标签会是 ——> <p>上次签到时间：2021-02-02 06:08:42</p>
    if re.match(r"<p>上次签到时间.*?</p>", txt):
        print("ture")
        txt_1 = email + "狗子云签到成功-->" + time
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text=" + txt_1)
    else:
        print("false")
        txt_2 = email + "狗子云签到失败-->" + time
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text=" + txt_2)

if __name__ == '__main__':
    # 1.北京时间
#     t=datetime.today()
#     ti= str(t.year)+"-"+str(t.month)+"-"+str(t.day)+" "+str(t.hour)+":"+str(t.minute)+":"+str(t.second)
    import datetime
    import pytz
#     utc = pytz.timezone('UTC')
    ti = datetime.datetime.now()
    # 2.账号密码信息
    username1 = os.environ["EMAIL1"]        
    password1 = os.environ["PASSWORD1"]
    username2 = os.environ["EMAIL2"]        
    password2 = os.environ["PASSWORD2"] 
    # 执行签到
    # 第一个签到
    login(email=username1,password=password1,time=ti)
    judge(email=username1,time=ti)
    # 第二个签到
    login(email=username2,password=password2,time=ti)
    judge(email=username2,time=ti)
    
