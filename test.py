import time
ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("this is a test")
with open("log.txt","a+") as f:
  f.write(ti)
  
  
