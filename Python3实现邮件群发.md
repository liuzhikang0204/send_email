**（1）在 mysql 数据库创建 mail 数据库，并创建 mail 表**

![1574065133990](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1574065133990.png)

**（2）将邮箱的电子邮件地址存在于mail 表中**

![1574065214602](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1574065214602.png)

**（3）编写 python 程序**

```python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import time
import MySQLdb

# 从数据库中获取ip地址列表
def get_addr():
    # 连接数据库
    conn = MySQLdb.Connection('127.0.0.1', 'root', '123456', 'mail')
    cursor = conn.cursor()
    # 执行SQL语句，获取邮箱地址
    cursor.execute("SELECT * FROM mail")
    result = cursor.fetchall()
    return result

# 发送邮件
def send_mail(to_list):
    mail_server = "smtp.163.com"    # 邮箱host
    mail_port = 25  # 端口号
    sender = "XXXXXXXXX@163.com"   # 自己的邮箱账号
    sender_password = "XXXXXX"  # 授权码,不是账号密码
    receivers = to_list     # 对方的邮箱账号

    # 邮件内容
    message = MIMEText('Python邮件发送测试...', 'plain', 'utf-8')
    message['From'] = sender    # 发送者
    message['To'] = receivers   # 接受者

    # 设置邮件的主题
    send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    subject = '邮件测试' + send_time
    message['Subject'] = subject

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_server, mail_port)    # 连接邮箱的服务器
        smtp_obj.login(sender, sender_password)     # 登录自己的邮箱
        smtp_obj.sendmail(sender, [receivers], message.as_string())     # 真正开始发送邮件
        print('success!')
    except smtplib.SMTPException as e:
        print('failure!')
        print(e)

if __name__ == '__main__':

    result = get_addr()
    for record in result:
        send_mail(record[1])
        # 休眠5秒，短时间大量发送邮件可能会造成发送失败或者账号被封
        time.sleep(5)

    # 也可以直接填写对方的邮箱账号
    # send_mail("XXXX@163.com")
```



另外，也可以直接填写对方的邮箱账号，进行特定用户的邮件发送。

Github地址：<https://github.com/xuxin199601/send_email>





**成功发送邮件！**

自己邮箱中的已发送列表：

![1574063910906](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1574063910906.png)

对方邮箱中的收信箱:

![1574064193036](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1574064193036.png)



但是，但是......

如果短时间大量发送邮件可能会造成发送失败或者账号被封

![1574064102453](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1574064102453.png)



![1574064082958](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1574064082958.png)



