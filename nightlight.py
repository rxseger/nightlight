#!/usr/bin/python
# nightlight.py - toggle LED on Raspberry Pi GPIO on/off given MCP3304 ADC to OPT101 ambient light reading

import spidev
import time
import math
import RPi.GPIO as GPIO
import pigpio

pi = pigpio.pi() # sudo pigpiod

# /dev/spidev(bus).(dev)
SPI_BUS = 0
# CE0 = 0, CE1=1
SPI_DEV = 0
# MCP3304 channel number, 0 to 7
ADC_CHANNEL = 7

# voltages if greater than or less than, recognize as light or dark (in between, no change)
V_LIGHT = 0.7  # turn off when light out
V_DARK = 0.6   # turn on when it is dark

# GPIO port for nightlight
#LED_Y = 32 # G12
LED_Y_BCM = 12 # board pin #32

# magnetic transducer
BUZZER_BCM = 19 # board pin #35
#BUZZER_FREQUENCY = 2000 # Hz, try: 8000, 4000, 2000 (rated), 1000, 800, 500, 200, 100, 80, 50, 10
BUZZER_FREQUENCY = 10 # Hz
BUZZER_DUTYCYCLE = 255*0.50
BUZZER_DURATION = 0.1 # seconds

GPIO.setmode(GPIO.BOARD) # TODO: switch to pigpio for SPI?
GPIO.setwarnings(False)

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEV)

# based on http://www.havnemark.dk/?p=54 and http://jeremyblythe.blogspot.ca/2012/09/raspberry-pi-hardware-spi-analog-inp
def readadc(adcnum):
	# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
	if adcnum > 7 or adcnum < 0:
		return -1

	# Frame format: 0000 1SCC | C000 000 | 000 000
	r = spi.xfer2([((adcnum & 6) >> 1)+12 , (adcnum & 1) << 7, 0])
	adcout = ((r[1] & 15) << 8) + r[2]

	# Read from ADC channels and convert the bits read into the voltage
	# Divisor changed from 1023 to 4095, due to 4 more bits
	return (adcout * 3.3) / 4095

# brightness: 0.0 (dark) - 1.0 (light)
def set_light(brightness):
	#print "set_light",brightness
	# 0-255 PWM duty cycle = 0 to 100%
	# 1- since LED is wired active-low
	n = 255 * (1 - brightness)
	if n < 0: n = 0
	if n > 255: n = 255
	pi.set_PWM_dutycycle(LED_Y_BCM, n)

def set_buzzer(on):
	if on:
		pi.set_PWM_frequency(BUZZER_BCM, BUZZER_FREQUENCY)
		pi.set_PWM_dutycycle(BUZZER_BCM, BUZZER_DUTYCYCLE)
	else:
		pi.set_PWM_frequency(BUZZER_BCM, 0)
		pi.set_PWM_dutycycle(BUZZER_BCM, 0)

is_light = True
counter = 0.0
direction = math.pi / 100
buzzer_started = None
while True:
	v = readadc(7)
	#print v
	was_light = is_light
	if v > V_LIGHT:
		is_light = True
	elif v < V_DARK:
		is_light = False

	if is_light != was_light:
		if is_light:
			set_light(0.0)
			counter = 0.0
		else:
			set_light(1.0)
		buzzer_started = time.time()
		set_buzzer(True)

	if buzzer_started and time.time() - buzzer_started > BUZZER_DURATION:
		set_buzzer(False)
		buzzer_stated = None


	if not is_light:
		counter += direction
		brightness = (math.sin(counter * math.pi * 1.5) / 2) + 0.5
		set_light(brightness)

	time.sleep(0.1)
