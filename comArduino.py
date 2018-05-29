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

def OuvreAgenda():
	f = open(fichier, 'r')
	while True :
		chaine = f.readline()
		print(chaine)
		if ("" == chaine):
                        print("fin de fichier")
                        f.close()
                        break
		if (chaine[0] == "V"):
			print(chaine[1:5])
			heureVeilleProchaine = time.strptime(chaine[1:5], '%H%M')
			print(heureVeilleProchaine.tm_hour, heureVeilleProchaine.tm_min)


#heureActuel = datetime.time.now()
print(heureActuel)
OuvreAgenda()
# chercher heureProchaineVeille
# 
# si heureCourante < heureProchaineVeille
# 	ne rien faire
# si heureCourante > heureProchaineVeille
#	transmettre duree de veille
#	shutdown
#
ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
line = 'bonjour\n'
ser.write(line)
ser.close()

