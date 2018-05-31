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
		self.hPV = datetime.datetime.now() #heure prochaine veille
		self.hNow = datetime.datetime.now() #heure actuelle
		self.duree = 0 # duree en secondes

	def calculVeille(self,heures, minutes):
		self.duree = (int(heures) * 3600) + (int(minutes) * 60)
		
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
				heureDureeVeille = chaine[7:9]
				minDureeVeille = chaine[10:12]
				self.calculVeille(heureDureeVeille,minDureeVeille)
				self.hNow = datetime.datetime.now()
				self.hPV = datetime.datetime(self.hNow.year, self.hNow.month, self.hNow.day, int(heure), int(min))
				f.close()



hC = datetime.datetime.now()
print("heure Courante", hC)
mesConsigne = Consigne()
print("heure Now", mesConsigne.hNow)
print("heure PV", mesConsigne.hPV)
print("duree veille",mesConsigne.duree)
pass
if (mesConsigne.hPV == None):
	time.sleep(5)
	# a voir, plus d'heure de veille avant le lendemain
print("heure Prochaine Veille", mesConsigne.hPV)
while True:
	hC = datetime.datetime.now()
	if hC < mesConsigne.hPV:
		print("heure courant", hC)
		print("heure de veille", mesConsigne.hPV)
		time.sleep(5)
	else:  		
		print
		print("transmission vers l'arduino")
		print("duree de la veille",mesConsigne.duree)
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
