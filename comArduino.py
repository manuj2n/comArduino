#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino.py


import serial

fichier='/home/pi/agenda.txt'
listVeille=[]

def OuvreAgenda():
	f = open(fichier, 'r')
	chaine = f.readline()
	print(chaine)
	f.close()

OuvreAgenda()
ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
line = 'bonjour\n'
ser.write(line)
ser.close()
