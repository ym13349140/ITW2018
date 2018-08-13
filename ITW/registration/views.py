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
# reload(sys)
# sys.setdefaultencoding('utf-8')


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
        title = request.form.get('title')
        pid = request.form.get('pid')
        affiliation = request.form.get('work-unit')
        edas1 = request.form.get('edas1')
        edas2 = request.form.get('edas2')
        edas3 = request.form.get('edas3')
        receipt = request.form.get('receipt')
        if receipt == 'Yes':
            receipt = u'是'
        else:
            receipt = u'否'
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
        if tutorial == 'Yes':
            tutorial = u'是'
        else:
            tutorial = u'否'
        tutorialItem = request.form.get('tutorialItem')
        needInvite = request.form.get('needInvite')
        if needInvite == 'Yes':
            needInvite = u'是'
        else:
            needInvite = u'否'
        travel = request.form.getlist('travel')
        excursion = u'否'        
        if len(travel) > 0:
            excursion = u''
        for t in travel:
            if t == '0':
                excursion = u'珠江夜游（11月26号晚）'
                if len(travel) == 2:
                    excursion += '/ '
            elif t == '1':
                excursion += u'登白云山（11月28号下午）'
        foodPreference = request.form.get('foodPreference')
        # print "Chinese ", '中文中文中文'.decode('utf-8').encode(sys_encoding) 
        if foodPreference == '0':
            foodPreference = u'素食'
        elif foodPreference =='1':
            foodPreference = u'清真'
        else:
            foodPreference = u'无'
        gotoTalk = request.form.get('gotoTalk')
        if gotoTalk == 'Yes':
            gotoTalk = u'是'
        else:
           gotoTalk = u'否'
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
        curr_user = Users(random_id=random_id, cname=cname, ename=ename, title=title, pid=pid, affiliation=affiliation,
                    edas1=edas1, edas2=edas2, edas3=edas3, receipt=receipt, receipt_title=receipt_title,
                    receipt_id=receipt_id, email=email, vip_num=vipNum, reg_type=regType, tutorial=tutorial,
                    tutorial_item=tutorialItem, need_invite=needInvite, excursion=excursion, food_preference=foodPreference,
                    goto_talk=gotoTalk, total_fee=totalFee)
        template = u'<p style="font-size: 20px;font-weight: 600">提交成功! 您的转账备注为：<span style="color:red;">' + random_id + u'ITW2018</span></p>\
                    <p style="font-size: 20px;font-weight: 600">请将<span style="color:red;"> CNY ' + str(totalFee) + u'</span> 于三个工作日内转入以下账号: </p>\
										<p>户名 ：中山大学</p>\
										<p>开户行：中国工商银行广州中山大学支行 </p>\
										<p>账号：3602864809100002723</p>\
                                        <p>备注：' + random_id + u'ITW2018</p><hr>\
										<p style="color:red;"><strong>注意：</strong></p>\
										<ol>\
											<li>请务必在银行转账的备注处填写系统提供的转账备注，以便我们确认您是否缴费成功。否则，我们将无法确认您的缴费，后果需自负。在确认缴费成功后，我们会在7个工作日内给您发邮件确认。</li>\
											<li>邀请函将会随同注册确认信一同寄给您。</li>\
										</ol><hr>\
                                        <p><strong>您的注册信息总览:</strong></p>\
										<p>姓名：' + cname + u'</p>\
                                        <p>称谓：' + title + u'</p>\
		 								<p>身份证号：' + pid + u'</p>\
		 								<p>工作单位：' + affiliation + u'</p>\
		 								<p>文章编号：'
        edas = u'无'
        if edas1:
            edas = u'' + edas1
        if edas2:
            edas = edas + u', '
            edas = edas + edas2
        if edas3:
            edas = edas + u', '
            edas = edas + edas3
        template = template + edas + u'</p>'
        if receipt == 'Yes':
            template = template + u'<p>发票抬头：' + receipt_title + u'</p>\
									<p>纳税人识别号：' + receipt_id + u'</p>'
        if vipNum:
            template = template + u'<p>IEEE 会员号：' + vipNum + u'</p>'
        template = template + u'<p>注册类型：' + regType + u'</p>'
        if tutorial == 'Yes':
            template = template + u'<p>Tutorial：' + tutorialItem + u'</p>'
        else:
            template = template + u'<p>Tutorial：无</p>'
        template = template + u'<p>是否需要会议通知和邀请函：' + needInvite + u'</p>\
                                <p>是否参加外出游览: ' + excursion + u'</p>\
                                <p>注册费用：CNY ' + str(totalFee) + u'</p>\
                                <p>转账备注：' + random_id + u'ITW2018</p>\
                                <p>饮食偏好：' + foodPreference + u'</p>\
                                <p>是否参加11月30日举办的中山大学编码与信息理论研讨会: ' + gotoTalk + u'</p>'
        subject = u'ITW 2018 - Registration Step 1 Succeeds'
        ret = send_email(email, ename, template, subject)
        if ret:
            db.session.add(curr_user)
            db.session.commit()
            return jsonify(status='success',
                            random_id=random_id,
                            cname=cname,
                            title=title,
                            pid=pid,
                            affiliation=affiliation,
                            edas1=edas1,
                            edas2=edas2,
                            edas3=edas3,
                            receipt=receipt,
                            receipt_title=receipt_title,
                            receipt_id=receipt_id,
                            vip_num=vipNum,
                            reg_type=regType,
                            tutorial_item=tutorialItem,
                            food_preference=foodPreference,
                            total_fee=totalFee,
                            need_invite=needInvite,
                            excursion=excursion,
                            goto_talk=gotoTalk)
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
        title = request.form.get('title')
        pid = request.form.get('pid')
        if pid == '':
            pid = u'None'
        country = request.form.get('country')
        affiliation = request.form.get('work-unit')
        edas1 = request.form.get('edas1')
        edas2 = request.form.get('edas2')
        edas3 = request.form.get('edas3')
        email = request.form.get('email')
        vipNum = request.form.get('vipNum')
        regType = request.form.get('money')
        if regType == '0':
            regType = u'Full Registration (IT soc)'
        elif regType == '1':
            regType = u'Full Registration (IEEE non IT soc)'
        elif regType == '2':
            regType = u'Full Registration (Non IEEE)'
        elif regType == '3':
            regType = u'Student IT soc/IEEE Life member'
        elif regType == '4':
            regType = u'Student (IEEE non IT soc)'
        elif regType == '5':
            regType = u'Student (Non IEEE)'
        elif regType == '6':
            regType = u'One Day Registration (With banquet)'
        elif regType == '7':
            regType = u'One Day Registration (Without banquet)'
        elif regType == '8':
            regType = u'Student One Day Registration (With banquet)'
        elif regType == '9':
            regType = u'Student One Day Registration (Without banquet)'
        elif regType == '10':
            regType = u'Banquet Only'
        tutorial = request.form.get('tutorial')
        tutorialItem = request.form.get('tutorialItem')
        needInvite = request.form.get('needInvite')
        travel = request.form.getlist('travel')
        excursion = u'No'        
        if len(travel) > 0:
            excursion = u''
        gender = ''
        birthday = ''
        for t in travel:
            if t == '0':
                excursion += u'Pearl river night cruise (Night, Nov. 26)'
                gender = request.form.get('gender')
                birthday = request.form.get('birthday')
                if len(travel) == 2:
                    excursion += '/ '
            elif t == '1':
                excursion += u'Baiyun mountain walk (Afternoon, Nov. 28)'
        foodPreference = request.form.get('foodPreference')
        # print "Chinese ", '中文中文中文'.decode('utf-8').encode(sys_encoding) 
        if foodPreference == '0':
            foodPreference = u'Vegetarian'
        elif foodPreference =='1':
            foodPreference = u'Halal'
        else:
            foodPreference = u'None'
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
        curr_user = Users(random_id=random_id, ename=ename, title=title, pid=pid, country=country, affiliation=affiliation,
                    edas1=edas1, edas2=edas2, edas3=edas3, email=email, vip_num=vipNum, reg_type=regType, tutorial=tutorial,
                    tutorial_item=tutorialItem, need_invite=needInvite, excursion=excursion, food_preference=foodPreference,
                    goto_talk=gotoTalk, total_fee=totalFee)
        template = u'<p style="font-size: 20px;font-weight: 600">Your information has been submitted. Your transaction note is: <span style="color:red;">' + random_id + u'ITW2018</span><p>\
                    <p style="font-size: 20px;font-weight: 600">Please transfer <span style="color:red;">USD ' + str(totalFee) + u'</span> to the following account within THREE working days.</p>\
										<p>Account Name：Sun Yat-sen University</p>\
										<p>Account Number：3602864809100002723</p>\
										<p>Swift Code：ICBKCNBJGDG</p>\
										<p>Bank：Industrial and Commercial bank of China, Guang Dong branch, sub-branch of Sun Yat-sen University</p>\
										<p>Address：No. 135 Xin Gang Xi Road Guang Zhou P.R China</p>\
										<p>Transaction Note：' + random_id + u'ITW2018</p><hr>\
										<p style="color:red;"><strong>Caution: </strong></p>\
										<ol>\
                                            <li>While transferring the registration fee, you MUST write the given transaction note. Your payment can only be traced with the note. Otherwise, your transaction may be lost and we are not responsible for it. After your payment has been confirmed, we will notify you via email within 7 working days.</li>\
                                            <li>Your invitation letter will be included in the transaction confirmation email.</li>\
                                        </ol><hr>\
                                        <p><strong>Your registration information:</strong></p>\
										<p>Name：' + ename + u'</p>\
                                        <p>Title: ' + title + u'</p>\
		 								<p>Passport/ID card number：' + pid + u'</p>\
                                        <p>Country: ' + country + u'</p>\
		 								<p>Affiliation: ' + affiliation + u'</p>\
		 								<p>Paper EDAS Number：'
        edas = u'None'
        if edas1:
            edas = u'' + edas1
        if edas2:
            edas = edas + u', '
            edas = edas + edas2
        if edas3:
            edas = edas + u', '
            edas = edas + edas3
        template = template + edas + u'</p>'
        if vipNum:
            template = template + u'<p>IEEE Membership Number：' + vipNum + u'</p>'
        template = template + u'<p>Register Type: ' + regType + u'</p>'
        if tutorial == 'Yes':
            template = template + u'<p>Tutorial：' + tutorialItem + u'</p>'
        else:
            template = template + u'<p>Tutorial：None</p>'
        template = template + u'<p>Do You Need an Invitation Letter：' + needInvite + u'</p>\
                                <p>Will You Join the Excursions: ' + excursion + u'</p>\
                                <p>Total Register Fee：USD ' + str(totalFee) + u'</p>\
                                <p>Transaction Note：' + random_id + u'ITW2018</p>\
                                <p>Dietary Preference：' + foodPreference + u'</p>\
                                <p>Will You Participate the SYSU Coding and Information Theory Workshop on Nov. 30: ' + gotoTalk + u'</p>'
        subject = u'ITW 2018 - Registration Step 1 Succeeds'
        ret = send_email(email, ename, template, subject)
        if ret:
            db.session.add(curr_user)
            db.session.commit()
            if gender:
                curr_user.gender = gender
                curr_user.birthday = birthday
                db.session.commit()
            return jsonify(status='success',
                            random_id=random_id,
                            ename=ename,
                            title=title,
                            country=country,
                            pid=pid,
                            affiliation=affiliation,
                            edas1=edas1,
                            edas2=edas2,
                            edas3=edas3,
                            vip_num=vipNum,
                            reg_type=regType,
                            tutorial_item=tutorialItem,
                            food_preference=foodPreference,
                            total_fee=totalFee,
                            need_invite=needInvite,
                            excursion=excursion,
                            goto_talk=gotoTalk)
        else:
            return jsonify(status='failed')