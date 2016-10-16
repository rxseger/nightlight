#!/usr/bin/python

# buzz.py - test magnetic transducer for nightlight

import time
import math
import pigpio
import sys

pi = pigpio.pi() # sudo pigpiod

# magnetic transducer
BUZZER_BCM = 19 # board pin #35
#BUZZER_FREQUENCY = 2000 # Hz, try: 8000, 4000, 2000 (rated), 1000, 800, 500, 200, 100, 80, 50, 10
BUZZER_FREQUENCY = 10 # Hz
BUZZER_DUTYCYCLE = 255*0.50
BUZZER_DURATION = 0.1 # seconds

def set_buzzer(on):
	if on:
		pi.set_PWM_frequency(BUZZER_BCM, BUZZER_FREQUENCY)
		pi.set_PWM_dutycycle(BUZZER_BCM, BUZZER_DUTYCYCLE)
	else:
		pi.set_PWM_frequency(BUZZER_BCM, 0)
		pi.set_PWM_dutycycle(BUZZER_BCM, 0)

if len(sys.argv) > 1:
	print "turning off"
	set_buzzer(False)
	raise SystemExit

print "buzzing"
on = True
while True:
	set_buzzer(on)
	on = not on

	time.sleep(0.1)
