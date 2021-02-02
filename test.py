import time
ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(ti)
with open("1.txt","a+") as f:
    f.write(ti)

  
  
