#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: smtp_sendmail_html.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 15:11:11
############################

import smtplib
from email.mime.text import MIMEText
mailto_list=["YYY@YYY.com"]
mail_host="smtp.XXX.com"    # 设置服务器
mail_user="XXX"    # 用户名
mail_pass="XXXX"    # 口令
mail_postfix="XXX.com"    # 收件箱的后缀

def send_mail(to_list, sub, content):    # tolist:收件人；sub:主题；content:邮件内容
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"    # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype="html", _charset="gb2312")    # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    # 设置主题
    msg['From'] = me
    msg['to'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)    # 连接smtp服务器
        s.login(mail_user, mail_pass)    # 登录服务器
        s.sendmail(me, to_list, msg.as_string())    # 发送邮件
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == "__main__":
    if send_mail(mailto_list, "hello", "<a href='http://www.zeroonecloud.com'>One Zero</a>"):
        print("发送成功")
    else:
        print("发送失败")
