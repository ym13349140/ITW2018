$(document).ready(function () {
	$('.overflow-ellipsis').tooltip();
	$(".list-title").click(function() {
		var icon = $(this).find("i");
		if (icon.hasClass("fa-chevron-down")) {
			icon.removeClass("fa-chevron-down");
			icon.addClass("fa-chevron-right");
		}
		else {
			icon.removeClass("fa-chevron-right");
			icon.addClass("fa-chevron-down");
		}
		$(this).next().toggle();
	});

	$(".sub-menu li").click(function () {
		$(".sub-menu li").removeClass("active");
		$(this).addClass("active");
		$(".nav .list-group-item").removeClass("active");
		$(this).parent().parent().addClass("active");
	});
});