#!/usr/bin/python3

import time
import serial

ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

while 1:
	x=ser.read()
	data=x.decode()
	data=data.rstrip()
	print(data,end="")
