# Whut_CampusNet_AutoLogin
该脚本可以自动登录Whut的校园网，免去每次连接校园网后还要输入用户名密码的繁琐操作，方便您的生活，节约时间。

用法步骤：

1. 校园网登录页面抓包
2. 获取post的requests的header和data的FormData的内容
3. 将代码中的相应内容修改为你自己的数据
4. 使用pyinstaller —F filename.py 打包为exe文件
5. 首先连接校园网，然后双击exe文件运行。
