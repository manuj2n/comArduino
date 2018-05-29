#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino.py

import time
import datetime
import serial

heureActuel = datetime.time(0, 0, 0)
heureVeilleProchaine = datetime.time(0, 0 ,0)
heureTmp = datetime.time(0, 0, 0)
fichier='agenda.txt'
listVeille=[]

def StringToHeure(chaineHeure):
	print(chaineHeure)

def OuvreAgenda():
	f = open(fichier, 'r')
	while True :
		chaine = f.readline()
		listVeille.append(chaine)
		if ("" == chaine):
			print("fin de fichier")
			f.close()
			break
		print(chaine)


OuvreAgenda()
ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
line = 'bonjour\n'
ser.write(line)
ser.close()
print(listVeille)

