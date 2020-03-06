
setInterval(update_power_health, 3000);
function update_power_health(){
    $.ajax({url: "/api/v1/power"}).done(function( data ) {
        var pwrLow = data.power_low;
        if (pwrLow){
	    // Power source dropped below 4.63 volts
            $('#power_health').html('<i class="fas fa-battery-full fa-stack-2x"></i><i class="fas fa-bolt fa-stack-1x fa-inverse pulsate" style="color:yellow;"></i>');
        } else {
	    // Power source is good
            $('#power_health').html('<i class="fas fa-battery-full fa-stack-2x"></i></i>');
        }
    });
}
