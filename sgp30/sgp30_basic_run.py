import time
import board
import busio
import adafruit_sgp30



def sensor_init():
	# Frequency 100,000 is per adafruit example
	i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
	sensor = adafruit_sgp30.Adafruit_SGP30(i2c)
	sensor.iaq_init()
	sensor.set_iaq_baseline(0x8973, 0x8AEE) # Numbers from adafruit example
	# sensor.set_iaq_humidity(self, gramsPM3) Humidity can be set
	return sensor


def tick_Conversion_Ethanol(signal_output):
    """ Gets raw ticks and converts to ppm """
# Assumes calibration ethanol was 14.85 ppm which is typical but not measured
    return 0.4*2.71828**((20997-signal_output)/512)

def tick_Conversion_H2(signal_output):
    """ Gets raw ticks and converts to ppm """
# Assumes calibration H2 was 1.25 ppm which is typical but not measured
    return 0.5*2.71828**((14296-signal_output)/512)


def sensor_loop(sensor):
    print(f"SGP30 serial numbers {sensor.serial} is in use") # Convert serial to hex for support purposes
    # Baseline can be set with sensor.set_iaq_baseline(c02eq_base, tvoc_base)
    print(f"c02eq baseline {sensor.baseline_eCO2} ")
    print(f"TVOC baseline {sensor.baseline_TVOC} ")
    count = 0;
    while True:
        if count > 20: #First 10-20 readings are not valid while sensor warms up
            H2_raw = sensor.H2
            Ethanol_raw = sensor.Ethanol
            H2 = tick_Conversion_H2 (H2_raw)
            Ethanol = tick_Conversion_Ethanol ( Ethanol_raw )
            print("------------------------")
            print(f"eCO2: {sensor.eCO2} ppm") # While warming up, always reports 400. ECO2 skyrockets above whiskey
            print(f"TVOC: {sensor.TVOC} ppb") # While warming up, always reports 0. TVOC skyrockets above whiskey
            print(f"H2: {H2_raw} Raw Ticks") #  Drops from 12000 to 9000 a few cm above whiskey
            print(f"Ethanol: {Ethanol_raw} Raw Ticks") # This number seems to be 17000 away from whiskey and 14000 above the surface. 
            print(f"H2: {H2} ppm")  # Shoots up from around 1.25 to 350 ppm over whisky!
            print(f"Ethanol: {Ethanol} ppm")  # shoots up from 14.85 ppm to 2250 ppm over whisky!
            print("------------------------")
        time.sleep(1)
        count += 1;
	

sensor = sensor_init()
sensor_loop(sensor)
