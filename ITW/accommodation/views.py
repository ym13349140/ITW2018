#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import accommodation
from flask import render_template, jsonify, request
from ..models import Reservations, Rooms
from ..util.send_email import send_email
from .. import db
import sys
import time, random, string


@accommodation.route('/')
def index():
    return render_template("accommodation/main.html", tab='accommodation', tag='index')


@accommodation.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'GET':
        type1 = Rooms.query.filter_by(type_num=1, in_date=24).first()
        type2 = Rooms.query.filter_by(type_num=2, in_date=24).first()
        type3 = Rooms.query.filter_by(type_num=3, in_date=24).first()
        type4 = Rooms.query.filter_by(type_num=4, in_date=24).first()
        type5 = Rooms.query.filter_by(type_num=5, in_date=24).first()
        type6 = Rooms.query.filter_by(type_num=6, in_date=24).first()
        if type1:
            num1 = type1.available_num
        else:
            num1 = 0
        if type2:
            num2 = type2.available_num
        else:
            num2 = 0
        if type3:
            num3 = type3.available_num
        else:
            num3 = 0
        if type4:
            num4 = type4.available_num
        else:
            num4 = 0
        if type5:
            num5 = type5.available_num
        else:
            num5 = 0
        if type6:
            num6 = type6.available_num
        else:
            num6 = 0
        print num1,num2,num3,num4,num5,num6
        return render_template("accommodation/main.html",
                                tab='accommodation',
                                tag='reservation',
                                num1=num1,
                                num2=num2,
                                num3=num3,
                                num4=num4,
                                num5=num5,
                                num6=num6)
    elif request.method =='POST':
        if request.form.get('op') == 'get_num':
            in_date = request.form.get('in_date')
            in_date = int(in_date) + 24
            type1 = Rooms.query.filter(Rooms.type_num==1, Rooms.in_date<=in_date).all()
            type2 = Rooms.query.filter(Rooms.type_num==2, Rooms.in_date<=in_date).all()
            type3 = Rooms.query.filter(Rooms.type_num==3, Rooms.in_date<=in_date).all()
            type4 = Rooms.query.filter(Rooms.type_num==4, Rooms.in_date<=in_date).all()
            type5 = Rooms.query.filter(Rooms.type_num==5, Rooms.in_date<=in_date).all()
            type6 = Rooms.query.filter(Rooms.type_num==6, Rooms.in_date<=in_date).all()
            num1 = 0
            num2 = 0
            num3 = 0
            num4 = 0
            num5 = 0
            num6 = 0
            for room in type1:
                num1 = num1 + room.available_num
            for room in type2:
                num2 = num2 + room.available_num
            for room in type3:
                num3 = num3 + room.available_num
            for room in type4:
                num4 = num4 + room.available_num
            for room in type5:
                num5 = num5 + room.available_num
            for room in type6:
                num6 = num6 + room.available_num
            return jsonify(status='success',
                            num1=num1,
                            num2=num2,
                            num3=num3,
                            num4=num4,
                            num5=num5,
                            num6=num6)
        else:
            date_dict = {
                '0':'11/24',
                '1':'11/25',
                '2':'11/26',
                '3':'11/27',
                '4':'11/28',
                '5':'11/29',
                '6':'11/30',
                '7':'12/01'
            }
            room_dict = {
                1: 'City View Room(One Queen bed)',
                2: 'City View Room(Two Single beds)',
                3: 'River View Room(One Queen bed)',
                4: 'River View Room(Two Single beds)',
                5: 'Bisuness Suit',
                6: 'River View Suit',
            }
            name = request.form.get('name')
            affiliation = request.form.get('affiliation')
            in_date_num = request.form.get('in-date')
            in_date = date_dict[in_date_num]
            out_date = request.form.get('out-date')
            uid = request.form.get('uid')
            email = request.form.get('email')
            room_type = request.form.get('room-type')
            # print name,affiliation,in_date,out_date,uid,email,room_type
            if room_type == '2' or room_type == '5':
                curr_room = Rooms.query.filter_by(type_num=room_type, in_date=24).first_or_404()
                if curr_room.available_num > 0:
                    curr_room.available_num = curr_room.available_num - 1
                else:
                    curr_room = Rooms.query.filter_by(type_num=room_type, in_date=25).first_or_404()
                    if curr_room.available_num > 0:
                        curr_room.available_num = curr_room.available_num - 1
                    else:
                        return jsonify(status='no rooms')
            elif room_type == '6':
                if int(in_date_num) < 2: 
                    curr_room = Rooms.query.filter_by(type_num=room_type, in_date=24).first_or_404()
                    if curr_room.available_num > 0:
                        curr_room.available_num = curr_room.available_num - 1
                    else:
                        return jsonify(status='no rooms')
                else:
                    curr_room = Rooms.query.filter_by(type_num=room_type, in_date=24).first_or_404()
                    if curr_room.available_num > 0:
                        curr_room.available_num = curr_room.available_num - 1
                    curr_room = Rooms.query.filter_by(type_num=room_type, in_date=26).first_or_404()
                    if curr_room.available_num > 0:
                        curr_room.available_num = curr_room.available_num - 1
                    else:
                        return jsonify(status='no rooms')
            elif room_type == '1':
                curr_room = Rooms.query.filter_by(type_num=room_type).first_or_404()
                if curr_room.available_num > 0:
                    curr_room.available_num = curr_room.available_num - 1
                else:
                    return jsonify(status='no rooms')
            else:
                if int(in_date_num) == 0: 
                    return jsonify(status='no rooms')
                curr_room = Rooms.query.filter_by(type_num=room_type).first_or_404()
                if curr_room.available_num > 0:
                    curr_room.available_num = curr_room.available_num - 1
                else:
                    return jsonify(status='no rooms')
            
            curr_reservation = Reservations(name=name,
                                            affiliation=affiliation,
                                            checkin_date=in_date,
                                            checkout_date=out_date,
                                            identity_num=uid,
                                            email=email,
                                            room_type=room_dict[curr_room.type_num])
            template = '<p style="font-size: 20px;font-weight: 600">Reserved Successfully!</p>\
						<p>Your check-in date：' + str(in_date) + '</p>\
						<p>Your check-out date：' + str(out_date) + '</p>\
						<p>Your room type is：' + str(room_dict[curr_room.type_num]) + '</p>\
						<p>The price is: ￥' + str(curr_room.price) + ' / day</p><hr>\
                        <p><strong>Note:</strong> The listed price contains only one breakfast. You can pay for the extra breakfast at check-in if needed.</p>\
                        <p>Sent by ITW2018 Organizing Committee</p>'
            subject = 'ITW2018-Reservation Successfully'
            ret = send_email(email, name, template, subject)
            if ret:
                db.session.add(curr_reservation)
                db.session.commit()
                return jsonify(status='success',
                                in_date=in_date,
                                out_date=out_date,
                                room_type=room_dict[curr_room.type_num],
                                price=curr_room.price)
            else:
                return jsonify(status='failed')