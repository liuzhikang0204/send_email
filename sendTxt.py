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
    sender = "xuxin_0107@163.com"   # 自己的邮箱账号
    sender_password = "xuxin123456"  # 授权码,不是账号密码
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
    # send_mail("17704628364@163.com")