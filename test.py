import time
import requests
import os
import argparse
# ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

username1 = os.environ["EMAIL1"]        
password1 = os.environ["PASSWORD1"]
username2 = os.environ["EMAIL2"]        
password2 = os.environ["PASSWORD2"]

# parser = argparse.ArgumentParser(description='auto signin script.')
# parser.add_argument('stuid', help='your student number', type=str)
# parser.add_argument('password', help='your CAS password', type=str)
# args = parser.parse_args()
r=requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+username1)
r=requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+username2)

