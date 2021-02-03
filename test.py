import time
import requests
import os
ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
r=requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+ti)
with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(ti)
  
