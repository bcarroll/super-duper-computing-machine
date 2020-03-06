let content_width  = $('#content').width();
let content_height = $('#content').height();
let content_top    = $('#content').css('top');
let content_left    = $('#content').css('left');

$('#settings-button').click(function (){
    $.ajax({url: "/settings"}).done(function( response ) {
	$('#content').html(response);
    });
});

function fullscreen(){
	$('#top').fadeOut();
	$('#left').fadeOut();
	$('#content').height('100%');
	$('#content').width('100%');
	$('#content').css('left', 0);
	$('#content').css('top', 0);
}

function restoreScreen(){
	$('#top').fadeIn();
	$('#left').fadeIn();
	$('#content').height(content_height);
	$('#content').width(content_width);
	$('#content').css('left', content_left);
	$('#content').css('top', content_top);
}