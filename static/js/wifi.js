setInterval(update_wifi_status, 3000);
function update_wifi_status(){
    $.ajax({url: "/api/v1/wifi"}).done(function( data ) {
        var wifi_status = data.status;
        if (wifi_status == 'not connected'){
	    // Wifi not connected
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x pulsate"></i></i>');
        } else {
	    // Wifi connected
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x"></i></i>');
        }
    });
}
