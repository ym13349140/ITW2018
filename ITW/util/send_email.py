#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from flask import current_app


def send_email(receiver, user_name, curr_id, is_mainland, **kwargs):
    ret=True
    try:
        app = current_app._get_current_object()
        my_sender = app.config['MAIL_USERNAME']
        my_pass = app.config['MAIL_PASSWORD']
        if is_mainland == 'yes':
            template = '<p style="font-size: 20px;font-weight: 600">提交成功! 您的编号为： ' + curr_id + '</p>\
										<p>请将注册费转到以下账号：</p>\
										<p>户名 ：中山大学</p>\
										<p>开户行：中国工商银行广州中山大学支行 </p>\
										<p>账号：3602864809100002723</p>\
										<p>备注：编号_ITW2018，例如，AA001_ITW2018</p><hr>\
										<p style="color:red;"><strong>注意：</strong></p>\
										<p style="text-indent:2;"><strong>请务必在银行转账的备注处填写“编号_ITW2018”，以便我们确认您是否缴费成功。若没有注明上示备注，我们将无法确认您是否缴费，后果请自负。在确认您缴费成功后，我们将会在7个工作日内给您发送缴费成功邮件。</strong></p>'
        else:
            template = '<p style="font-size: 20px;font-weight: 600">Submit successffully! Your number is ' + curr_id + '</p>\
										<p>Please transfer the registration fee to the following account：</p>\
										<p>Account：Sun Yat-sen University</p>\
										<p>Swift Code：ICBKCNBJGDG</p>\
										<p>Bank：Industrial and Commercial bank of China, Guang Dong branch, sub-branch of Sun Yat-sen University</p>\
										<p>Address：No. 135 Xin Gang Xi Road Guang Zhou P.R China</p>\
										<p>Note: Number_ITW2018, e.g., AA001_ITW2018</p><hr>\
										<p style="color:red;"><strong>Notice：</strong></p>\
										<p style="text-indent:2;"><strong>Please make sure that you write down “number _ITW2018” as the note of your transaction while transferring your registration fee. Your payment can only be traced with a proper note. Without a proper note, your transaction may be lost and we are not responsible for it. After your payment being confirmed, we will notify you via email within 7 working days.</strong></p>'
        msg=MIMEText(template,'html','utf-8')
        msg['From']=formataddr(["ITW2018", my_sender])          # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr([user_name, receiver])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']= app.config['MAIL_SUBJECT_PREFIX']                # 邮件的主题，也可以说是标题
 
       
        smtp = smtplib.SMTP()
        # show the debug log
        smtp.set_debuglevel(1)
        
        # connet
        try:
            smtp.connect(app.config['MAIL_SERVER'],587)
        except:
            print 'CONNECT ERROR ****'
        # gmail uses ssl
        smtp.starttls()
        # login with username & password
        try:
            smtp.login(my_sender, my_pass)
        except:
            print 'LOGIN ERROR ****'

       
        # server=smtplib.SMTP_SSL("smtp.gmail.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        # server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        smtp.sendmail(my_sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        smtp.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
