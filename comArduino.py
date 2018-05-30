#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino

import datetime
import time
#import serial

hT = datetime.time(0, 0, 0)
hPV = datetime.time(0,0,0)
fichier='agenda.txt'

def OuvreAgenda():
	f = open(fichier, 'r')
	while True :
		chaine = f.readline()
		#print(chaine)
		if (chaine == ""):
			f.close()
			print("fin de fichier")
			break
		if (chaine[0] == "V"):
			heure = chaine[1:3]
			min = chaine[4:6]
			#print(heure, min)
			hT = datetime.datetime(hC.year, hC.month, hC.day, int(heure), int(min))
			print("heure Tempo",hT)
			if (hT > hC):
				return hT

hC = datetime.datetime.now()
print("heureA",hC)
hPV = OuvreAgenda()
print("heurePV",hPV)
# chercher heureProchaineVeille
#
# si heureCourante < heureProchaineVeille
# 	ne rien faire
# si heureCourante > heureProchaineVeille
#	transmettre duree de veille
#	shutdown
#
#ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
line = 'bonjour\n'
#ser.write(line)
#ser.close()
