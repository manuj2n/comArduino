#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# comArduino

import datetime
import time
#import serial

class Consigne:

	def __init__(self):
		self.fichier = 'agenda.txt'
		self.heureDureeVeille = ""
		self.minDureeVeille = ""

	def calculVeille(self):
		duree = (int(self.heureDureeVeille) * 3600) + (int(self.minDureeVeille) * 60)
		return duree
		
	def OuvreAgenda(self):
		f = open(self.fichier, 'r')
		while True:
			chaine = f.readline()
			#print(chaine)
			if (chaine == ""):
				f.close()
				break
			if (chaine[0] == "V"):
				heure = chaine[1:3]
				min = chaine[4:6]
				self.heureDureeVeille = chaine[7:9]
				self.minDureeVeille = chaine[10:12]
				hNow = datetime.datetime.now()
				hPV = datetime.datetime(hNow.year, hNow.month, hNow.day, int(heure), int(min),0)
				f.close()
				return hPV



hC = datetime.datetime.now()
print("heure Courante", hC)
mesConsigne = Consigne()
heureVeille = mesConsigne.OuvreAgenda()
print("heure PV", heureVeille)
dureeVeille = mesConsigne.calculVeille()
print("duree veille",dureeVeille)
pass
if (heureVeille == None):
	time.sleep(5)
	# a voir, plus d'heure de veille avant le lendemain

while True:
	hC = datetime.datetime.now()
	if hC < heureVeille:
		print("heure courant", hC)
		print("heure de veille", heureVeille)
		time.sleep(5)
	else:  		
		print
		print("transmission vers l'arduino")
		print("duree de la veille",heureVeille)
		time.sleep(5)
		# si heureCourante > heure
		# ProchaineVeille
		#	transmettre duree de veille
		#	shutdown
		#
		#ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
		#line = "bonjour"
		#ser.write(line)
		#ser.close()
