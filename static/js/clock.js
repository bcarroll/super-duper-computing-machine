function startClock(interval) {
    if (!interval){ interval = 500; }
    return setInterval(function(){ getTime(12); }, interval);
}

/**
 * @param {integer} clock_hours 12 or 24
 * @param {string} format Format of the returned time string
 *      month            Month number 1-12
 *      day
 *      year
 *      hour
 *      minute
 *      second
 *      time_of_day      am/pm
 *  Example: "month/day/year hour:minute:second time_of_day" (This is the default format)
 * @param {boolean} return_time Indicates if the current time should be returned.  If false, or not specified HTML element with id="clock" is updated.
 */
function getTime(clock_hours, format, return_time){
    // set default clock_hours if not specified
    if (!clock_hours){
        clock_hours = 12;
    } else if (clock_hours > 12){
        // set clock_hours to 24 if specified as greater than 12
        clock_hours = 24;
    } else {
        // set clock_hours to 12 if specified as 12 or less
        clock_hours = 12;
    }

    // set default format if not specified
    if (!format){
        format = "month/day/year hour:minute:second time_of_day";
    }

    var today = new Date();
    var current_time = {
        "month": today.getMonth()+1,
        "day": today.getDate(),
        "year": today.getFullYear(),
        "hour": today.getHours(),
        "minute": checkTime(today.getMinutes()),
        "second": checkTime(today.getSeconds()),
        "time_of_day": "am",
        "clock_hours": clock_hours
    }

    if (current_time['clock_hours'] >= 12){
        if (current_time['clock_hours'] > 12){
            current_time['hour'] = current_time['hour'] - 12;
        }
        current_time['time_of_day'] = 'pm';
    }

    if (return_time){
        return getFormatFromString(format);
    }
    document.getElementById('clock').innerHTML = current_time['month'] + '/' + current_time['day'] + '/' + current_time['year'] + ' ' + current_time['hour'] + ":" + current_time['minute'] + ":" + current_time['second'] + ' ' + current_time['time_of_day'];
}

function getFormatFromString(formatString){
    console.log(formatString);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}