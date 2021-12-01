# Linear Interpolation Method
def linear(time_of_interest, data_set_low, data_set_high):
    """
    Find the CO2, temperature, and humidity values between two data points.
    
    Given two data points and a time of interest between them,
    use linear interpolation to find the values at the given time
    and returns them in a dict.
    """
    given_time2 = data_set_high['seconds']
    given_time1 = data_set_low['seconds']
    temp_high, temp_low = data_set_high['temp'], data_set_low['temp']
    humidity_high = data_set_high['humidity']
    humidity_low = data_set_low['humidity']
    co2_high, co2_low = data_set_high['co2'], data_set_low['co2']
    # Difference between the time of two measurements
    time_difference = given_time2 - given_time1
    #First determine the slope of the path between the two times.
    # This is the slope of the line known as a linear interpolant.
    # The slope of a line where the horizontal axis is time,
    # and the vertical axis is the value to interpolate, is the
    # rate of change in the value per unit time.
    change_rate_temp = (temp_high - temp_low) / time_difference
    change_rate_humidity = (humidity_high - humidity_low) / time_difference
    change_rate_c02 = (co2_high - co2_low) / time_difference

    # Difference between the time of interest and the fistTime
    time_difference = time_of_interest - given_time1
    # The interpolated data value is the early value plus the time difference
    # multiplied by the slope (change rate)
    interpolated_temp = temp_low + change_rate_temp*time_difference
    interpolated_humidity = humidity_low + change_rate_humidity*time_difference
    interpolated_co2 = co2_low + change_rate_c02*time_difference
    # The interpolated value is returned out of this function.
    return dict(seconds=time_of_interest, co2=interpolated_co2,
                temp=interpolated_temp,
                humidity=interpolated_humidity)
