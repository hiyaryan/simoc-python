To install the SGP30:

First be sure that you have enabled I2C on the Raspberry Pi. See the readme.md for the bme288 for more information.

To install the adafruit library:
`pip3 install adafruit-circuitpython-sgp30`

This sensor reports Hydrogen gas and Ethanol readings in "Raw Ticks" that seem to be inversly proportional to the gas content a centimeter above whiskey.
It also reports eCO2 and TVOC in ppm and ppb respectively, an estimate of CO2 from the other gases, and total volatile organic compounds.