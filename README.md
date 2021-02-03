# 狗子云 每日签到

https://dog1.52dog.xyz/user

这是一个用来FQ的网站，注册登录送1G流量

利用 python 

datetime（获取当前时间）

requests（主要是用来post表单）

bs4、re（用来解析usr网页内容，判断是否签到成功）

os（操作密码）


ps：
  server酱（推送微信消息，提示你是否成功）
  
# 密码和账号

1. fork到自己的仓库

2. 添加 Secrets
setting ——>  Secrets ——> New repository secret

3. 添加 EMAIL 对应自己的账号
  
   添加 PASSWORD 对应账号

4. 更改 gouziyun_daka.yml文件中的对应项

   更改 gouziyun_daka.py中的数据（我这里有两个账号所以有是EMAIL1和EMAIL2，根据情况改就行，如果只有一个账号删除.py文件的最后两行代码，删除.yml文件中env下的EMAIL2和PASSWORD2）

5. 点击star



end ————————————————————————————————————————————————————————————————— end

