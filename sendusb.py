#!/usr/bin/python3

import serial
from serial import *
from time import sleep

#ser = serial.Serial('/dev/ttyUSB0')  # open serial port
ser=serial.Serial('/dev/ttyUSB0',9600)

print(ser.name)         # check which port was really used
#   ser.write(b'hello\n')     # write a string
#   ser.write(str.encode('bye\n'))
#   ser.write(str.encode('53:02.0,41.86573608,-87.60680976,2022-04-30T18:53:02.000Z,187.835,0.043,-0.014,73.3248,2.987,4.953,0.4,nan,15.1\n'))
with open('../GPSLog/GPSLog08.csv') as f1:
#with open('../PresIMULog/PresIMULog08.csv') as f2:
  for lines in f1:

     #lines = f1.read()
     ser.write(str.encode(lines))
     sleep(1) 
  ser.write(b'done')     # write a string


ser.close()             # close port


