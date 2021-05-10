import requests
url = "https://qmsg.zendee.cn/send/0cb7ec3b53ee6db28ff921b6af54f9db"
data={
    "msg":''+"狗子签到成功@face=2@",
    "qq":"2079986882"
}
requests.post(url, data=data)