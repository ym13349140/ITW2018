function show_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	$(tag).show();
}

function hide_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	$(tag).hide();
}

function showRadio(tag, is_mainland) {
	$(tag).slideDown();
	if(tag === "#tutorial-list") {
		updateMoney(1, is_mainland);
	}
}

function hideRadio(tag, is_mainland) {
	$(tag).slideUp();
	if(tag === "#tutorial-list") {
		updateMoney(0, is_mainland);
	}
}

function showMoney(is_mainland) {
	var selected = $("#register-money").val();
	var money;
	if(is_mainland) {
		money = [4130,4690,5390,2310,2660,3010,1848,1148,1498,798,700];
	} 
	else {
		money = [590,670,770,330,380,430,264,164,214,114,100];
	}
	var total = money[selected];
	var isChecked = $('input:radio[name="tutorial"]:checked').val();
	if(isChecked == 'Yes') {
		if(is_mainland) {
			total = money[selected] + 560;
		} 
		else {
			total = money[selected] + 80;
		}
	}
	$("#register-totalFee").val(total);
}

function updateMoney(flag, is_mainland) {
	var selected = $("#register-money").val();
	var money;
	if(is_mainland) {
		money = [4130,4690,5390,2310,2660,3010,1848,1148,1498,798,700];
	} 
	else {
		money = [590,670,770,330,380,430,264,164,214,114,100];
	}
	var curr = parseInt($("#register-totalFee").val());
	var total = curr;
	if(flag) {
		if(is_mainland) {
			total += 560;
		} 
		else {
			total += 80;
		}
	}
	else {
		$("#register-totalFee").val(money[selected]);
		if(curr != money[selected]) {
			if(is_mainland) {
				total -= 560;
			} 
			else {
				total -= 80;
			}
		}
	}
	$("#register-totalFee").val(total);
}

function alert_modal(content, isHtml) {
    var obj = $("#modal-alert");
    if (isHtml) {
        obj.find(".modal-body").html(content);
    }
    else {
        obj.find(".modal-body").text(content);
    }
    obj.modal('show');
}

function toggleGender() {
	let checked1 = $("#zhujiang").prop("checked");
	let checked2 = $("#baiyunshan").prop("checked");
	let need = $("#register-needInvit1").prop("checked");
	if(need) {
		$("#passport-id").slideDown();
		$("#birthday-box").slideDown();
		if(checked1 || checked2) {
			$("#gender-list").slideDown();
		}
		else {
			$("#gender-list").slideUp();
		}
	}
	else {
		$("#passport-id").slideUp();
		if(checked1 || checked2) {
			$("#gender-list").slideDown();
			$("#birthday-box").slideDown();
		}
		else {
			$("#gender-list").slideUp();
			$("#birthday-box").slideUp();
		}
	}
}

function checkIcon(ele, is_mainland) {
	let value = ele.currentTarget.value;
	if(value.indexOf(',')!=-1 || value.indexOf(';')!=-1 || value.indexOf('，')!=-1 || value.indexOf('；')!=-1) {
		if(is_mainland) {
			alert_modal("请注意：请避免输入分号 “；” 与逗号 “，”");
        }
        else {
			alert_modal("Attention: Do Not Include Characters Semicolon ';' or Comma ',' .");
		}
	}
}

$(document).ready(function () {
	$('.overflow-ellipsis').tooltip();
	$('.read-more').click(function() {
		$(this).parent().parent().hide();
		$(this).parent().parent().next().show();
	});
	$('.read-less').click(function() {
		$(this).parent().parent().hide();
		$(this).parent().parent().prev().show();
	});

	$("#registerSubmit").click(function() {
		let is_mainland = $("#is-mainland").val();
		if(is_mainland == 'yes') {
			if($("#register-cname").val() == '') {
				alert_modal("请输入您的姓名！");
				return;
			}
			else if($("#register-ename").val() == '') {
				alert_modal("请输入您的英文名！");
				return;
			}
			else if($("#register-title").val() == '') {
				alert_modal("请输入您的称谓！");
				return;
			}
			else if($("#register-pid").val() == '') {
				alert_modal("请输入您的身份证号！");
				return;
			}
			else if($("#register-work-unit").val() == '') {
				alert_modal("请输入您的工作单位！");
				return;
			}
			else if(!($("#register-receipt1").prop("checked") || $("#register-receipt2").prop("checked"))) {
				alert_modal("请选择是否需要发票！");
				return;
			}
			else if($("#register-email").val() == '') {
				alert_modal("请输入您的邮箱用于接收注册信息！");
				return;
			}
			else if($("#register-email1").val() == '') {
				alert_modal("请再次输入您的邮箱！");
				return;
			}
			else if($("#register-email").val() != $("#register-email1").val()) {
				alert_modal("您两次输入的邮箱不符，请重新输入！");
				return;
			}
			else if(!($("#register-tutorial1").prop("checked") || $("#register-tutorial2").prop("checked"))) {
				alert_modal("请选择是否参加tutorial！");
				return;
			}
			else if(!($("#register-needInvit1").prop("checked") || $("#register-needInvit2").prop("checked"))) {
				alert_modal("请选择是否需要会议通知和邀请函！");
				return;
			}
			else if(!($("#register-foodPreference1").prop("checked") || $("#register-foodPreference2").prop("checked") || $("#register-foodPreference3").prop("checked"))) {
				alert_modal("请选择您的饮食偏好！");
				return;
			}
			else if(!($("#register-gotoTalk1").prop("checked") || $("#register-gotoTalk2").prop("checked"))) {
				alert_modal("请选择是否参加11月30日举办的中山大学编码与信息理论研讨会！");
				return;
			}
			if($("#register-receipt1").prop("checked")) {
				if($("#register-receipt-title").val() == '') {
					alert_modal("请输入发票抬头信息！");
					return;
				}
				else if($("#register-receipt-id").val() == '') {
					alert_modal("请输入纳税人识别号信息！");
					return;
				}
			}
			if($("#register-tutorial1").prop("checked")) {
				if(!($("#register-tutorial1-1").prop("checked") || $("#register-tutorial2-1").prop("checked"))) {
					alert_modal("请选择一个tutorial！");
					return;
				}
			}
			let type_num = parseInt($("#register-money").val());
			if((type_num >= 3 && type_num <= 5) || (type_num >= 8 && type_num <= 9)) {
				if($("#register-edas2").val() != '' || $("#register-edas3").val() != '') {
					alert_modal("学生用户仅能填写一项论文EDAS编号！");
					return;
				}
			}
			let total_fee = $("#register-totalFee").val();
			$("#total-fee-before").text("您的注册费用为：CNY ");
			$("#total-fee").text(total_fee);
			$("#total-fee-after").text("，确认提交？");
		}
		else {
			if($("#register-ename").val() == '') {
				alert_modal("Please input your name！");
				return;
			}
			else if($("#register-title").val() == '') {
				alert_modal("Please input your title！");
				return;
			}
			else if($("#register-country").val() == '') {
				alert_modal("Please input your country！");
				return;
			}
			else if($("#register-work-unit").val() == '') {
				alert_modal("Please input your affiliation！");
				return;
			}
			else if($("#register-email").val() == '') {
				alert_modal("Please input your e-mail address！");
				return;
			}
			else if($("#register-email1").val() == '') {
				alert_modal("Please input your e-mail address again！");
				return;
			}
			else if($("#register-email").val() != $("#register-email1").val()) {
				alert_modal("E-mail addresses do not match！");
				return;
			}
			else if(!($("#register-tutorial1").prop("checked") || $("#register-tutorial2").prop("checked"))) {
				alert_modal("Please choose weather you will participate a tutorial on Nov. 25！");
				return;
			}
			else if(!($("#register-needInvit1").prop("checked") || $("#register-needInvit2").prop("checked"))) {
				alert_modal("Please choose weather you need an invitation letter！");
				return;
			}
			else if(!($("#register-foodPreference1").prop("checked") || $("#register-foodPreference2").prop("checked") || $("#register-foodPreference3").prop("checked"))) {
				alert_modal("Please choose your dietary preference！");
				return;
			}
			else if(!($("#register-gotoTalk1").prop("checked") || $("#register-gotoTalk2").prop("checked"))) {
				alert_modal("Please choose weather you will participate the SYSU Information and Coding Theory Workshop on Nov. 30");
				return;
			}
			if($("#register-tutorial1").prop("checked")) {
				if(!($("#register-tutorial1-1").prop("checked") || $("#register-tutorial2-1").prop("checked"))) {
					alert_modal(" Please choose a tutorial！");
					return;
				}
			}
			let type_num = parseInt($("#register-money").val());
			if((type_num >= 3 && type_num <= 5) || (type_num >= 8 && type_num <= 9)) {
				if($("#register-edas2").val() != '' || $("#register-edas3").val() != '') {
					alert_modal("Student members can only have one paper EDAS number！");
					return;
				}
			}
			if ($("#register-needInvit1").prop("checked")) {
				if($("#register-pid").val() == '') {
					alert_modal("Please input your passport/ID card number！");
					return;
				}
				if($("#register-birthday").val() == '') {
					alert_modal("Please input your birthday for insurance！");
					return;
				}
				if($("#zhujiang").prop("checked") || $("#baiyunshan").prop("checked")) {
					if(!($("#register-gender1").prop("checked") || $("#register-gender2").prop("checked"))) {
						alert_modal("Please choose your gender！");
						return;
					}
				}
			}
			if ($("#register-needInvit2").prop("checked")) {
				if($("#zhujiang").prop("checked") || $("#baiyunshan").prop("checked")) {
					if($("#register-birthday").val() == '') {
						alert_modal("Please input your birthday！");
						return;
					}
					if(!($("#register-gender1").prop("checked") || $("#register-gender2").prop("checked"))) {
						alert_modal("Please choose your gender！");
						return;
					}
				}
			}
			let total_fee = $("#register-totalFee").val();
			$("#total-fee-before").text("Your total registration fee is：USD ");
			$("#total-fee").text(total_fee);
			$("#total-fee-after").text(".");
			$("#next-line-content").text("Please confirm then submit.");
		}
		$("#submit-comfirm-modal").modal("show");
	});

	$("#user-submit-comfirm").click(function(e) {
		// console.log()
		let is_mainland = $("#is-mainland").val();
		$.ajax({
			type: "post",
            url: location.href,
            data: new FormData($('#user-register-form')[0]),
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
				$("#submit-comfirm-modal").modal("hide");
				if(data.status == "success"){
					// alert("OKOK");
					let new_html;
					if(is_mainland == 'yes') {
						new_html = '<h3>提交成功! 您的转账备注为： <span style="color:red;">' + data.random_id + 'ITW2018</span></h3>\
										<h3>请将<span style="color:red;">CNY ' + data.total_fee + '</span>于三个工作日内转入以下账号:</h3>\
										<p>户名 ：中山大学</p>\
										<p>开户行：中国工商银行广州中山大学支行 </p>\
										<p>账号：3602864809100002723</p>\
										<p>备注：' + data.random_id + 'ITW2018</p><hr>\
										<p style="color:red;"><strong>注意：</strong></p>\
										<ol>\
											<li>请务必在银行转账的备注处填写系统提供的转账备注，以便我们确认您是否缴费成功。否则，我们将无法确认您的缴费，后果需自负。在确认缴费成功后，我们会在7个工作日内给您发邮件确认。</li>\
											<li>邀请函将会随同注册确认信一同寄给您。</li>\
										</ol><hr>\
										<p><strong>您的注册信息总览:</strong></p>\
										<p>姓名：' + data.cname + '</p>\
                                        <p>称谓：' + data.title + '</p>\
										<p>身份证号：' + data.pid + '</p>\
										<p>工作单位：' + data.affiliation + '</p>\
										<p>文章编号：';
						let edas = '无';
						if(data.edas1) {
							edas = data.edas1;
						}
						if(data.edas2) {
							edas += '; ';
							edas += data.edas2;
						}
						if(data.edas3) {
							edas += ', ';
							edas += data.edas3;
						}
						new_html += edas + '</p>';
						if(data.receipt == 'Yes') {
							new_html += '<p>发票抬头：' + data.receipt_title + '</p>\
										<p>纳税人识别号：' + data.receipt_id + '</p>';
						}
						if(data.vip_num) {
							new_html += '<p>IEEE 会员号：' + data.vip_num + '</p>';
						}
						new_html += '<p>注册类型：' + data.reg_type + '</p>';
						if(data.tutorial_item) {
							new_html += '<p>Tutorial：' + data.tutorial_item + '</p>';
						}
						else {
							new_html += '<p>Tutorial：无</p>';
						}
						new_html += '<p>是否需要会议通知和邀请函：' + data.need_invite + '</p>\
									<p>是否参加外出游览：' + data.excursion + '</p>\
									<p>注册费用：CNY ' + data.total_fee + '</p>\
									<p>转账备注：' + data.random_id + 'ITW2018</p>\
									<p>饮食偏好：' + data.food_preference + '</p>\
									<p>是否参加11月30日举办的中山大学编码与信息理论研讨会: ' + data.goto_talk + '</p>';
						$("#registration-mainland").html(new_html);
					}
					else {
						new_html = '<h3>Your information has been submitted. Your transaction note is:  <span style="color:red;">' + data.random_id + 'ITW2018</span></h3>\
									<h3>Please transfer <span style="color:red;">USD ' + data.total_fee + ' </span>to the following account within THREE working days.</h3>\
										<p>Account Name：Sun Yat-sen University</p>\
										<p>Account Number：3602864809100002723</p>\
										<p>Swift Code：ICBKCNBJGDG</p>\
										<p>Bank：Industrial and Commercial bank of China, Guang Dong branch, sub-branch of Sun Yat-sen University</p>\
										<p>Address：No. 135 Xin Gang Xi Road Guang Zhou P.R China</p>\
										<p>Transaction Note：' + data.random_id + 'ITW2018</p><hr>\
										<p style="color:red;"><strong>Caution: </strong></p>\
										<ol>\
                                            <li>While transferring the registration fee, you MUST write the given transaction note. Your payment can only be traced with the note. Otherwise, your transaction may be lost and we are not responsible for it. After your payment has been confirmed, we will notify you via email within 7 working days.</li>\
                                            <li>Your invitation letter will be included in the transaction confirmation email.</li>\
                                        </ol><hr>\
                                        <p><strong>Your registration information:</strong></p>\
										<p>Name：' + data.ename + '</p>\
                                        <p>Title: ' + data.title + '</p>\
		 								<p>Passport/ID card number：' + data.pid + '</p>\
                                        <p>Country: ' + data.country + '</p>\
		 								<p>Affiliation：' + data.affiliation + '</p>\
		 								<p>Paper EDAS Number：';
						let edas = 'None';
						if(data.edas1) {
							edas = data.edas1;
						}
						if(data.edas2) {
							edas += '; ';
							edas += data.edas2;
						}
						if(data.edas3) {
							edas += ', ';
							edas += data.edas3;
						}
						new_html += edas + '</p>';
						if(data.vip_num) {
							new_html += '<p>IEEE Membership Number：' + data.vip_num + '</p>';
						}
						new_html += '<p>Registration Type：' + data.reg_type + '</p>';
						if(data.tutorial_item) {
							new_html += '<p>Tutorial：' + data.tutorial_item + '</p>';
						}
						else {
							new_html += '<p>Tutorial：None</p>';
						}
						new_html += '<p>Do You Need an Invitation Letter：' + data.need_invite + '</p>\
									<p>Will You Join the Excursions：' + data.excursion + '</p>\
									<p>Total Registration Fee：USD ' + data.total_fee + '</p>\
                                	<p>Transaction Note：' + data.random_id + 'ITW2018</p>\
                                	<p>Dietary Preference：' + data.food_preference + '</p>\
                                	<p>Will You Participate the SYSU Information and Coding Theory Workshop on Nov. 30: ' + data.goto_talk + '</p>'
						$("#registration-outside").html(new_html);
					}
				}
				else {
					if(is_mainland == 'yes') {
						alert_modal("系统提交失败，请刷新后重试！");
					}
					else {
						alert_modal("The System Submit failed，please try again later!");
					}
				}
			}
		});
	});

	$("#register-in-date").change(function() {
		let in_date = $("#register-in-date").val();
		$.ajax({
			type: "post",
			url: location.href,
			data: {
				op: 'get_num',
				in_date: in_date,
			},
			async: false,
			success: function (data) {
				if (data["status"] == "success") {
					$("#register-room-type").find("option").each(function() {
						$(this).attr("disabled", false);
					});
					if(data['num1'] == 0) {
						$("#register-room-type option[value='1']").attr('disabled', true);
					}
					if(data['num2'] == 0) {
						$("#register-room-type option[value='2']").attr('disabled', true);
					}
					if(data['num3'] == 0) {
						$("#register-room-type option[value='3']").attr('disabled', true);
					}
					if(data['num4'] == 0) {
						$("#register-room-type option[value='4']").attr('disabled', true);
					}
					if(data['num5'] == 0) {
						$("#register-room-type option[value='5']").attr('disabled', true);
					}
					if(data['num6'] == 0) {
						$("#register-room-type option[value='6']").attr('disabled', true);
					}
					// console.log(data['num1'], data['num2'], data['num3'], data['num4'], data['num5'], data['num6']);
				}
			}
		});
	});

	$("#reservationSubmit").click(function() {
		if($("#register-name").val() == '') {
			alert_modal("Please input your name！");
			return;
		}
		else if($("#register-affiliation").val() == '') {
			alert_modal("Please input your affiliation！");
			return;
		}
		else if($("#register-uid").val() == '') {
			alert_modal("Please input your Passport/Identity No！");
			return;
		}
		else if($("#register-email").val() == '') {
			alert_modal("Please input your e-mail！");
			return;
		}
		else if($("#register-room-type").val() == '') {
			alert_modal("Please select a room type！");
			return;
		}
		else {
			$.ajax({
				type: "post",
				url: location.href,
				data: new FormData($('#user-reservation-form')[0]),
				cache: false,
				processData: false,
				contentType: false,
				success: function (data) {
					if(data.status == "success"){
						new_html = '<p style="font-size: 20px;font-weight: 600">Reserved Successfully!</p><hr>\
									<p>Your name is：' + data.name + '</p>\
									<p>Your check-in date：' + data.in_date + '</p>\
									<p>Your check-out date：' + data.out_date + '</p>\
									<p>Your room type is：' + data.room_type + '</p>\
									<p>The price is: ￥' + data.price + ' / day</p><hr>\
									<p><strong>Note:</strong> The listed price contains only one breakfast. You can pay for the extra breakfast at check-in if needed.</p>';
						// alert_modal(new_html);
						$("#accommodation-reservation .row").html(new_html);
					}
					else if(data.status == "no rooms") {
						alert_modal("There is not enough room left for current type. Please choose another room type!");
					}
					else {
						alert_modal("Submit Failed!");
					}
				}
			});
		}
	});
});

