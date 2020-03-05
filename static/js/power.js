
setInterval(update_power_health, 3000);
function update_power_health(){
    $.ajax({url: "/api/v1/power"}).done(function( data ) {
        var pwrLow = data.power_low;
        if (pwrLow){
            $('#power_health').html('<i class="fas fa-bolt fa-2x"></i>');
        } else {
            $('#power_health').html('<i class="fas fa-battery-full fa-2x"></i>');
        }
    });
}