EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L +5V #PWR?
U 1 1 57E9FF72
P 2950 1900
F 0 "#PWR?" H 2950 1750 50  0001 C CNN
F 1 "+5V" H 2950 2040 50  0000 C CNN
F 2 "" H 2950 1900 50  0000 C CNN
F 3 "" H 2950 1900 50  0000 C CNN
	1    2950 1900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 57E9FF86
P 2950 3050
F 0 "#PWR?" H 2950 2800 50  0001 C CNN
F 1 "GND" H 2950 2900 50  0000 C CNN
F 2 "" H 2950 3050 50  0000 C CNN
F 3 "" H 2950 3050 50  0000 C CNN
	1    2950 3050
	1    0    0    -1  
$EndComp
$Comp
L Q_NPN_EBC Q?
U 1 1 57E9FFAB
P 3500 2750
F 0 "Q1" H 3800 2800 50  0000 R CNN
F 1 "D1786R" H 4000 2700 50  0000 R CNN
F 2 "" H 3700 2850 50  0000 C CNN
F 3 "" H 3500 2750 50  0000 C CNN
	1    3500 2750
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57E9FFDC
P 3150 2750
F 0 "R1" V 3230 2750 50  0000 C CNN
F 1 "2k" V 3150 2750 50  0000 C CNN
F 2 "" V 3080 2750 50  0000 C CNN
F 3 "" H 3150 2750 50  0000 C CNN
	1    3150 2750
	0    1    1    0   
$EndComp
Wire Wire Line
	3600 3050 3600 2950
Wire Wire Line
	2950 3050 3600 3050
Text GLabel 2950 2750 0    60   Input ~ 0
G19
Wire Wire Line
	2950 2750 3000 2750
$Comp
L INDUCTOR L?
U 1 1 57EA0268
P 4000 2250
F 0 "L1" V 3950 2250 50  0000 C CNN
F 1 "Magnetic transducer" V 4100 2250 50  0000 C CNN
F 2 "" H 4000 2250 50  0000 C CNN
F 3 "" H 4000 2250 50  0000 C CNN
	1    4000 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4000 2550 3600 2550
Wire Wire Line
	2950 1950 4000 1950
Wire Wire Line
	2950 1950 2950 1900
Connection ~ 3600 1950
Wire Wire Line
	3600 2550 3600 2400
$Comp
L D D?
U 1 1 57EA0089
P 3600 2250
F 0 "D1" H 3600 2350 50  0000 C CNN
F 1 "1N4148" H 3600 2150 50  0000 C CNN
F 2 "" H 3600 2250 50  0000 C CNN
F 3 "" H 3600 2250 50  0000 C CNN
	1    3600 2250
	0    1    1    0   
$EndComp
Wire Wire Line
	3600 2100 3600 1950
$EndSCHEMATC
