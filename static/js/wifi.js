setInterval(update_wifi_status, 3000);
function update_wifi_status(){
    $.ajax({url: "/api/v1/wifi"}).done(function( data ) {
        var wifi_status = data.status;
        if (wifi_status == 'DISCONNECTED'){
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x disconnected"></i></i>');
        } else if (wifi_status == 'CONNECTED'){
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x"></i></i>');
        } else if (wifi_status == 'SCANNING'){
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x scanning"></i></i>');
        } else if (wifi_status == 'INACTIVE'){
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x inactive"></i></i>');
        } else if (wifi_status == 'CONNECTING'){
            $('#wifi_status').html('<i class="fas fa-wifi fa-stack-2x connecting"></i></i>');
        }
    });
}