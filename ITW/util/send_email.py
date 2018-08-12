#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from flask import current_app


def send_email(receiver, user_name, template, subject, **kwargs):
    ret=True
    try:
        app = current_app._get_current_object()
        cc_add = 'itw2018gz@gmail.com'
        to_list = [receiver, cc_add]
        my_sender = app.config['MAIL_USERNAME']
        my_pass = app.config['MAIL_PASSWORD']
        msg=MIMEText(template,'html','utf-8')
        msg['From']=formataddr(["ITW2018", my_sender])          # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr([user_name, receiver])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Cc']=formataddr(['ITW2018', cc_add])                # 抄送地址
        msg['Subject']= subject                                 # 邮件的主题，也可以说是标题
 
       
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)
        # connet
        try:
            smtp.connect(app.config['MAIL_SERVER'], 587)
        except:
            print 'CONNECT ERROR ****'
        # gmail uses ssl
        smtp.starttls()
        # login with username & password
        # smtp = smtplib.SMTP_SSL(app.config['MAIL_SERVER'],465)
        try:
            smtp.login(my_sender, my_pass)
        except:
            print 'LOGIN ERROR ****'

       
        # server=smtplib.SMTP_SSL("smtp.gmail.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        # server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        smtp.sendmail(my_sender, to_list, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        smtp.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
