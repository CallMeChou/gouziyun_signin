import requests
from datetime import datetime
# time
t=datetime.today()
ti= str(t.year)+"-"+str(t.month)+"-"+str(t.day)+" "+str(t.hour)+":"+str(t.minute)+":"+str(t.second)
# data
email_list = ["2079986882@qq.com","chou2079986882@gmial.com"]
pass_words = ["Zhou3.1415926","Zhou3.1415926"]


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
        txt_1 = email+"狗子云签到成功||||||"+time
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+txt_1)
    except:
        txt_2 = email+"狗子云签到失败||||||"+time
        requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+txt_2)


if __name__ == '__main__':
    for i in range(2):
        login(email=email_list[i],password=pass_words[i],time=ti)
