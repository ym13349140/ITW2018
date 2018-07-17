function show_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	$(tag).show();
}

function hide_sub_menu(tag) {
	var icon = $(tag).prev().find("i");
	$(tag).hide();
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
});

