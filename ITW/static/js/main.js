function show_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	$(tag).show();
}

function hide_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	$(tag).hide();
}

function showRadio(tag) {
	$(tag).slideDown();
	if(tag === "#tutorial-list") {
		updateMoney(1);
	}
}

function hideRadio(tag) {
	$(tag).slideUp();
	if(tag === "#tutorial-list") {
		updateMoney(0);
	}
}

function showMoney() {
	var selected = $("#register-money").val();
	var money = [4130,4690,5390,1680,2030,2380,1848,1148,1498,798,700];
	var total = money[selected];
	if($("#register-tutorial").prop("checked")) {
		total = money[selected] + 560;
	}
	$("#register-totalFee").val(total);
}

function updateMoney(flag) {
	var selected = $("#register-money").val();
	var money = [4130,4690,5390,1680,2030,2380,1848,1148,1498,798,700];
	var curr = parseInt($("#register-totalFee").val());
	var total = curr;
	if(flag) {
		total += 560;
	}
	else {
	$("#register-totalFee").val(money[selected]);
		if(curr != money[selected]) {
			total -= 560;
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
			let total_fee = $("#register-totalFee").val();
			$("#total-fee-before").text("您的总费用为：￥ ");
			$("#total-fee").text(total_fee);
			$("#total-fee-after").text("，确认提交？");
		}
		else {
			if($("#register-ename").val() == '') {
				alert_modal("Please input your name！");
				return;
			}
			else if($("#register-pid").val() == '') {
				alert_modal("Please input your passport/ID card number！");
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
				alert_modal("Please input your e-mail！");
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
			let total_fee = $("#register-totalFee").val();
			$("#total-fee-before").text("Your total fee is：￥ ");
			$("#total-fee").text(total_fee);
			$("#total-fee-after").text(", Confirm to submit.");
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
					let curr_id = data.curr_id;
					let new_html;
					if(is_mainland == 'yes') {
						new_html = '<h3>提交成功! 您的编号为： ' + curr_id + '</h3>\
										<p>请将注册费转到以下账号：</p>\
										<p>户名 ：中山大学</p>\
										<p>开户行：中国工商银行广州中山大学支行 </p>\
										<p>账号：3602864809100002723</p>\
										<p>备注：编号_ITW2018，例如，AA001_ITW2018</p><hr>\
										<p style="color:red;"><strong>注意：</strong></p>\
										<p style="text-indent:2;"><strong>请务必在银行转账的备注处填写“编号_ITW2018”，以便我们确认您是否缴费成功。若没有注明上示备注，我们将无法确认您是否缴费，后果请自负。在确认您缴费成功后，我们将会在7个工作日内给您发送缴费成功邮件。</strong></p>'
						$("#registration-mainland").html(new_html);
					}
					else {
						new_html = '<h3>Submit successffully! Your number is ' + curr_id + '</h3>\
										<p>Please transfer the registration fee to the following account：</p>\
										<p>Account：Sun Yat-sen University</p>\
										<p>Swift Code：ICBKCNBJGDG</p>\
										<p>Bank：Industrial and Commercial bank of China, Guang Dong branch, sub-branch of Sun Yat-sen University</p>\
										<p>Address：No. 135 Xin Gang Xi Road Guang Zhou P.R China</p>\
										<p>Note: Number_ITW2018, e.g., AA001_ITW2018</p><hr>\
										<p style="color:red;"><strong>Notice：</strong></p>\
										<p style="text-indent:2;"><strong>Please make sure that you write down “number _ITW2018” as the note of your transaction while transferring your registration fee. Your payment can only be traced with a proper note. Without a proper note, your transaction may be lost and we are not responsible for it. After your payment being confirmed, we will notify you via email within 7 working days.</strong></p>'
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
});

