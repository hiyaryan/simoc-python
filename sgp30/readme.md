To install the SGP30:

First be sure that you have enabled I2C on the Raspberry Pi. See the readme.md
for the bme288 for more information.

To install the adafruit library:
`pip3 install adafruit-circuitpython-sgp30`

This sensor reports Hydrogen gas and Ethanol readings in "Raw Ticks" that 
seem to be inversly proportional to the gas content a centimeter above whiskey.
It also reports eCO2 and TVOC in ppm and ppb respectively, an estimate of CO2
from the other gases, and total volatile organic compounds.

According to documentation found for the sensor, Raw ticks can be converted into 
concentrations by the following equation:

concentration = concentration_reference*e^((signal_reference-signal_output)/512)
where signal_reference is the signal given by the sensors at 0.5 ppm Hydrogen Gas.
signal_output is for raw ticks, and the concentration_reference
is 0.5 ppm for Hydrogen gas and 0.4 ppm for Ethanol.  Unfortunately, there is no
known source for signal_reference that I can find without calibrating against
a known concentration. It can maybe be inferred by making eCO2 match the output
of SCD-30 CO2 somehow.

0.3 to 30 ppm is typical ethanol concentration
0.5 to 3 ppm is typical H2 concentration

The range of the sensor is 0 to 1000 ppm.
I get a 5 digit readings like 13827 with a change in the ones place
So if variation is 1/10,000 there must be enough bits to hold at least 10,000. (14)
I speculate 16 bits are used (65,536 steps?)

For Hydrogen where I am getting 13827 now
Based on this speculation ~0.5-3 = 0.5*e^(( sref - 13827) / 512)
Assume h2 ppm is in the middle or ~ 1.25
Solve for sref 1.25 = 0.5*e^(( sref - 13827) / 512)
sref would be ~ 14296.1 based on this assumed concentration of 1.25 ppm

For Ethanol where I am getting 19146 now
Based on this speculation ~0.3-30 = 0.4*e^(( sref - 19146) / 512)
Assume ethanol ppm is in the middle or ~ 14.85
Solve for sref 14.85 = 0.4*e^(( sref - 19146) / 512)
sref would be ~ 20996.5 based on this assumed concentration of 14.85 ppm


Until further calibration I propose:

concentration = 0.5*e^((14296-signal_output)/512)  for h2
concentration = 0.4*e^((20997-signal_output)/512)  for ethanol