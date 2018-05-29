#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino 

import time
import serial

#heureTmp = datetime.time(0, 0, 0)
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
			print(chaine[1:3])
			#heureVeilleProchaine.replace(hour=int(chaine[1:3]))
			#heureVeilleProchaine = datetime.strptime(chaine[1:5], '%H:%M')


heureActuel = time.localtime()
heureVeilleProchaine.clock_settime(CLOCK_REALTIME,time(23,01,01))
print("heureA",heureActuel)
#OuvreAgenda()
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

