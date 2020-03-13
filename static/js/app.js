let content_width  = $('#content').width();
let content_height = $('#content').height();
let content_top    = $('#content').css('top');
let content_left    = $('#content').css('left');

$('#settings-button').click(function (e){
	e.preventDefault();
	$('#content').attr("src", "/settings");
});

$('#audio-button').click(function (e){
	e.preventDefault();
	$('#content').attr("src", "/audio");
});

$('#video-button').click(function (e){
	e.preventDefault();
	$('#content').attr("src", "/video");
});

$('#image-button').click(function (e){
	e.preventDefault();
	$('#content').attr("src", "/image");
});

function to_human_readable(val){
	if (val > 1024*1024*1024){
		return (val/1024/1024/1024).toFixed(2) + " GB";
	} else if (val > 1024*1024){
		return (val/1024/1024).toFixed(2) + " MB";
	} else if (val > 1024){
		return (val/1024).toFixed(2) + " KB";
	} else {
		return val.toFixed(2) + " B"
	}
}

function linearGauge(element, title){
	var gauge = new LinearGauge({
		renderTo: element,
		title: title,
		height: 100,
		width: 600,
		minValue: 0,
		maxValue:100,
		value: 0,
		strokeTicks: false,
		highlights: [
			{ from: 0, to: 60, color: 'rgba(0,255,0,.15)' },
			{ from: 60, to: 80, color: 'rgba(255,255,0,.15)' },
			{ from: 80, to: 100, color: 'rgba(255,0,0,.2)' }
		],
		valueInt: 3,
		valueDec: 0,
		borderRadius: 20,
		borderInnerWidth: 2,
		borderMiddleWidth: 0,
		borderOuterWidth: 1,
		borderShadowWidth: 2,
		colorBorderInner: 'rgba(32,128,128, .25)',
		colorBorderOuter: 'rgba(32,128,128, .5)',
		colorBorderShadow: 'rgba(32,128,128, 1)',
		colorNeedleShadowUp: 'rgba(32,128,128, .5)',
		colorNeedleShadowDown: 'rgba(32,128,128, 1)',
		needleShadow: true,
		colorPlate: '#000',
		colorMajorTicks: 'rgba(32,128,128, 1)',
		colorMinorTicks: 'rgba(128,128,128, 1)',
		colorUnits: 'rgba(128,128,128, 1)',
		colorNumbers: 'rgba(128,128,128, 1)',
		colorNeedle: 'rgba(32,128,128, .5)',
		colorNeedleEnd: 'rgba(32,128,128, 1)',
		needleSide: 'right',
		numberSide: 'right',
		tickSide: 'right',
		barBeginCircle: 0,
		valueBox: false,
		animation: true,
		animationRule: 'linear',
		animationDuration: 800,
		highDpiSupport: true
	});
	return gauge;
}