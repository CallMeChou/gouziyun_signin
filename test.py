import time
import requests
import os
import argparse
# ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

username = os.environ["EMAIL"]        
password = os.environ["PASSWORD"]

parser = argparse.ArgumentParser(description='auto signin script.')
parser.add_argument('stuid', help='your student number', type=str)
parser.add_argument('password', help='your CAS password', type=str)
args = parser.parse_args()
r=requests.post("https://sc.ftqq.com/SCU157350Te9a01b046907e9e3ef2e03af71dbe5fa6018c6d67e1a4.send?text="+username)


