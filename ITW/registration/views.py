#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import registration
from flask import render_template, jsonify, request
from ..models import Users
from ..util.send_email import send_email
from .. import db
import sys
import time, random, string

sys_encoding = sys.getfilesystemencoding()


@registration.route('/registration')
def registrations():
    return render_template(
        "registration/main.html",
        tab="registration",
        tag="registration")


@registration.route('/student_travel_grant')
def student_travel_grant():
    return render_template(
        "registration/main.html",
        tab="registration",
        tag="student_travel_grant")


@registration.route('/choose_to_register')
def choose_to_register():
    return render_template(
        "registration/main.html",
        tab="registration",
        tag="choose_to_register")


@registration.route('/register_mainland', methods=['GET', 'POST'])
def register_mainland():
    if request.method == 'GET' :
        return render_template(
            "registration/main.html",
            tab="registration",
            tag="register_mainland")
    elif request.method == 'POST':
        cname = request.form.get('cname')
        ename = request.form.get('ename')
        pid = request.form.get('pid')
        affiliation = request.form.get('work-unit')
        edas1 = request.form.get('edas1')
        edas2 = request.form.get('edas2')
        edas3 = request.form.get('edas3')
        receipt = request.form.get('receipt')
        receipt_title = request.form.get('receipt-title')
        receipt_id = request.form.get('receipt-id')
        email = request.form.get('email')
        vipNum = request.form.get('vipNum')
        regType = request.form.get('money')
        if regType == '0':
            regType = 'Full Registration (IT soc)'
        elif regType == '1':
            regType = 'Full Registration (IEEE non IT soc)'
        elif regType == '2':
            regType = 'Full Registration (Non IEEE)'
        elif regType == '3':
            regType = 'Student IT soc/IEEE Life member'
        elif regType == '4':
            regType = 'Student (IEEE non IT soc)'
        elif regType == '5':
            regType = 'Student (Non IEEE)'
        elif regType == '6':
            regType = 'One Day Registration (With banquet)'
        elif regType == '7':
            regType = 'One Day Registration (Without banquet)'
        elif regType == '8':
            regType = 'Student One Day Registration (With banquet)'
        elif regType == '9':
            regType = 'Student One Day Registration (Without banquet)'
        elif regType == '10':
            regType = 'Banquet Only'
        tutorial = request.form.get('tutorial')
        tutorialItem = request.form.get('tutorialItem')
        needInvite = request.form.get('needInvite')
        travel = request.form.getlist('travel')
        excursion = ''
        for t in travel:
            if t == '0':
                excursion += '珠江夜游，11月26号晚'
                if len(travel) == 2:
                    excursion += ', '
            elif t == '1':
                excursion += '登白云山，11月28号下午'
        foodPreference = request.form.get('foodPreference')
        # print "Chinese ", '中文中文中文'.decode('utf-8').encode(sys_encoding) 
        if foodPreference == '0':
            foodPreference = '素食'
        elif foodPreference =='1':
            foodPreference = '清真'
        else:
            foodPreference = '无'
        gotoTalk = request.form.get('gotoTalk')
        totalFee = request.form.get('totalFee')

        s1 = ''.join(random.choice(string.ascii_letters) for _ in range(2))
        s2 = ''.join(random.choice(string.digits) for _ in range(3))
        random_id = s1 + s2
        existed = Users.query.filter_by(random_id=random_id).first()
        while existed:
            s1 = ''.join(random.choice(string.ascii_letters) for _ in range(2))
            s2 = ''.join(random.choice(string.digits) for _ in range(3))
            random_id = s1 + s2
            existed = Users.query.filter_by(random_id=random_id).first()
        curr_user = Users(random_id=random_id, cname=cname, ename=ename, pid=pid, affiliation=affiliation,
                    edas1=edas1, edas2=edas2, edas3=edas3, receipt=receipt, receipt_title=receipt_title,
                    receipt_id=receipt_id, email=email, vip_num=vipNum, reg_type=regType, tutorial=tutorial,
                    tutorial_item=tutorialItem, need_invite=needInvite, excursion=excursion, food_preference=foodPreference,
                    goto_talk=gotoTalk, total_fee=totalFee)
        template = '<p style="font-size: 20px;font-weight: 600">提交成功! 您的编号为：<span style="color:red;">' + random_id + '</span>; 您的总注册费用为：<span style="color:red;">￥ ' + str(totalFee) + '</span></p>\
										<p>请将注册费转到以下账号：</p>\
										<p>户名 ：中山大学</p>\
										<p>开户行：中国工商银行广州中山大学支行 </p>\
										<p>账号：3602864809100002723</p>\
										<p>备注：编号_ITW2018，例如，AA001_ITW2018</p><hr>\
										<p style="color:red;"><strong>注意：</strong></p>\
										<p style="text-indent:2;"><strong>请务必在银行转账的备注处填写“编号_ITW2018”，以便我们确认您是否缴费成功。若没有注明上示备注，我们将无法确认您是否缴费，后果请自负。在确认您缴费成功后，我们将会在7个工作日内给您发送缴费成功邮件。</strong></p>'  
        subject = 'ITW2018-Registration Successfully'
        ret = send_email(email, ename, template, subject)
        if ret:
            db.session.add(curr_user)
            db.session.commit()
            return jsonify(status='success', curr_id=random_id, total_fee=totalFee)
        else:
            return jsonify(status='failed')


@registration.route('/register_outside', methods=['GET', 'POST'])
def register_outside():
    if request.method == 'GET' :
        return render_template(
            "registration/main.html",
            tab="registration",
            tag="register_outside")
    elif request.method == 'POST':
        ename = request.form.get('ename')
        pid = request.form.get('pid')
        country = request.form.get('country')
        affiliation = request.form.get('work-unit')
        edas1 = request.form.get('edas1')
        edas2 = request.form.get('edas2')
        edas3 = request.form.get('edas3')
        email = request.form.get('email')
        vipNum = request.form.get('vipNum')
        regType = request.form.get('money')
        if regType == '0':
            regType = 'Full Registration (IT soc)'
        elif regType == '1':
            regType = 'Full Registration (IEEE non IT soc)'
        elif regType == '2':
            regType = 'Full Registration (Non IEEE)'
        elif regType == '3':
            regType = 'Student IT soc/IEEE Life member'
        elif regType == '4':
            regType = 'Student (IEEE non IT soc)'
        elif regType == '5':
            regType = 'Student (Non IEEE)'
        elif regType == '6':
            regType = 'One Day Registration (With banquet)'
        elif regType == '7':
            regType = 'One Day Registration (Without banquet)'
        elif regType == '8':
            regType = 'Student One Day Registration (With banquet)'
        elif regType == '9':
            regType = 'Student One Day Registration (Without banquet)'
        elif regType == '10':
            regType = 'Banquet Only'
        tutorial = request.form.get('tutorial')
        tutorialItem = request.form.get('tutorialItem')
        needInvite = request.form.get('needInvite')
        travel = request.form.getlist('travel')
        excursion = ''
        for t in travel:
            if t == '0':
                excursion += '珠江夜游，11月26号晚'
                if len(travel) == 2:
                    excursion += ', '
            elif t == '1':
                excursion += '登白云山，11月28号下午'
        foodPreference = request.form.get('foodPreference')
        # print "Chinese ", '中文中文中文'.decode('utf-8').encode(sys_encoding) 
        if foodPreference == '0':
            foodPreference = '素食'
        elif foodPreference =='1':
            foodPreference = '清真'
        else:
            foodPreference = '无'
        gotoTalk = request.form.get('gotoTalk')
        totalFee = request.form.get('totalFee')

        s1 = ''.join(random.choice(string.ascii_letters) for _ in range(2))
        s2 = ''.join(random.choice(string.digits) for _ in range(3))
        random_id = s1 + s2
        existed = Users.query.filter_by(random_id=random_id).first()
        while existed:
            s1 = ''.join(random.choice(string.ascii_letters) for _ in range(2))
            s2 = ''.join(random.choice(string.digits) for _ in range(3))
            random_id = s1 + s2
            existed = Users.query.filter_by(random_id=random_id).first()
        curr_user = Users(random_id=random_id, ename=ename, pid=pid, country=country, affiliation=affiliation,
                    edas1=edas1, edas2=edas2, edas3=edas3, email=email, vip_num=vipNum, reg_type=regType, tutorial=tutorial,
                    tutorial_item=tutorialItem, need_invite=needInvite, excursion=excursion, food_preference=foodPreference,
                    goto_talk=gotoTalk, total_fee=totalFee)
        template = '<p style="font-size: 20px;font-weight: 600">Submit successffully! Your number is: <span style="color:red;">' + random_id + '</span>; your total fee is：<span style="color:red;">$ ' + str(totalFee) + '</span></p>\
										<p>Please transfer the registration fee to the following account：</p>\
										<p>Account：Sun Yat-sen University</p>\
										<p>Swift Code：ICBKCNBJGDG</p>\
										<p>Bank：Industrial and Commercial bank of China, Guang Dong branch, sub-branch of Sun Yat-sen University</p>\
										<p>Address：No. 135 Xin Gang Xi Road Guang Zhou P.R China</p>\
										<p>Note: Number_ITW2018, e.g., AA001_ITW2018</p><hr>\
										<p style="color:red;"><strong>Notice：</strong></p>\
										<p style="text-indent:2;"><strong>While you are transferring the registration fee, you MUST write “NUMBER _ITW2018” as the note of your transaction. Your payment can only be traced with the note. Otherwise, your transaction may be lost and we are not responsible for it. After your payment has been confirmed, we will notify you via email within 7 working days.</strong></p>'
        subject = 'ITW2018-Registration Successfully'
        ret = send_email(email, ename, template, subject)
        if ret:
            db.session.add(curr_user)
            db.session.commit()
            return jsonify(status='success', curr_id=random_id, total_fee=totalFee)
        else:
            return jsonify(status='failed')