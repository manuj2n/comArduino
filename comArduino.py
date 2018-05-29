#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino.py

import time
import serial

#heureTmp = datetime.time(0, 0, 0)
fichier='agenda.txt'
heureVeilleProchaine =  time.strptime("00:00:00", "%H:%M:%S")

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
			print(chaine[1:3])
			heureVeilleProchaine = time.strptime(chaine[1:5], '%H%M')


heureActuel = time.localtime()
print("heureA",heureActuel)
OuvreAgenda()
print("heureVP",heureVeilleProchaine)
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

