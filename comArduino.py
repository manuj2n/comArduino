#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino

import datetime
import time
#import serial

hT = datetime.time(0, 0, 0)
hPV = datetime.time(0, 0, 0)
dureeVeille = 0
fichier = 'agenda.txt'


def OuvreAgenda():
	f = open(fichier, 'r')
	while True:
		chaine = f.readline()
		#print(chaine)
		if (chaine == ""):
			f.close()
			break
		if (chaine[0] == "V"):
			heure = chaine[1:3]
			min = chaine[4:6]
			#print(heure, min)
			heureDureeVeille = chaine[7:9]
			minDureeVeille = chaine[10:12]
			dureeVeille = (int(heureDureeVeille) * 3600) + (int(minDureeVeille) * 60)
			print("hDV et mDV en secondes", heureDureeVeille, minDureeVeille, dureeVeille)
			hT = datetime.datetime(hC.year, hC.month, hC.day, int(heure), int(min))
			print("heure Tempo", hT)
			print("Temps d'attente pour ma veille", hT - hC)
			if (hT > hC):
				f.close()
				return hT

hC = datetime.datetime.now()
print("heure Courante", hC)
hPV = OuvreAgenda()
if (hPV == None):
	time.sleep(5)
	# a voir, plus d'heure de veille avant le lendemain
print("heure Prochaine Veille", hPV)
while True:
	hC = datetime.datetime.now()
	if hC < hPV:
		print("heure courant", hC)
		print("heure de veille", hPV)
		time.sleep(5)
	else:  		
		time.sleep(5)
		print("transmission vers l'arduino")
		# si heureCourante > heure
		# ProchaineVeille
		#	transmettre duree de veille
		#	shutdown
		#
		#ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
		#line = "bonjour"
		#ser.write(line)
		#ser.close()
