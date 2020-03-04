
setInterval(update_power_health, 3000);
function update_power_health(element){
    $.ajax({url: "/api/v1/power"}).done(function( data ) {
        var pwrLow = data.power_low;
        if (pwrLow){
            $('#power_health').html('<i class="fas fa-bolt"></i>');
        } else {
            $('#power_health').html('<i class="fas fa-battery-full"></i>');
        }
    });
}