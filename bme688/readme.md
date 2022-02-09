This folder contains a basic script to run the BME688 on the Raspberry Pi using the qwiic shim.

First make sure that the i2c is enabled.
1. Use `raspi-config`
2. Choose option 3, Interface Options
3. Go to I5 I2C Enable/disable loading of i2c
4. Would you like the ARM I2C interface to be enabled? Yes
5. Choose Finish

To install the adafruit python driver:
`pip3 install adafruit-circuitpython-bme680`

Then the script should run easily.
`python3 bme688_basic_run.py`


Hardware usesage note:
# Due to the nature of the Metal Oxide sensor, the sensor should be run for 48 hours from new to
# burn-in the device.  It should also be run for 30 minutes straight before trusting readings.

It is recommended to calibrate the BME688 against known sources.