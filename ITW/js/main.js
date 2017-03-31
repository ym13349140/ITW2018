function show_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	icon.removeClass("fa-caret-right");
	icon.addClass("fa-caret-down");
	$(tag).show();
}

function hide_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	icon.removeClass("fa-caret-down");
	icon.addClass("fa-caret-right");
	$(tag).hide();
}

$(document).ready(function () {
	$('.overflow-ellipsis').tooltip();

	/*tab*/
	$(".navbar-nav li > a").click(function () {
		$(".navbar-nav li").removeClass("active");
		$(this).parent().addClass("active");
	});

	$(".navbar-nav .dropdown-menu a").click(function () {
		$(".navbar-nav li").removeClass("active");
		$(this).parent().parent().parent().addClass("active");
	});

});