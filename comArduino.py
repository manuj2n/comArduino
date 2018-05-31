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
		self.heureDebutVeille = ""
		self.minDeDebutVeille = ""
		self.heureFinVeille = ""
		self.minFinVeille = ""

	def calculVeille(self):
		heureDV = (int(self.heureDebutVeille) * 3600) + (int(self.minDeDebutVeille) * 60)
		heureFV = (int(self.heureFinVeille) * 3600) + (int(self.minFinVeille) * 60)
		duree = heureFV - heureDV
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
				self.heureDebutVeille = chaine[1:3]
				self.minDeDebutVeille = chaine[4:6]
				self.heureFinVeille = chaine[7:9]
				self.minFinVeille = chaine[10:12]
				hNow = datetime.datetime.now()
				hPV = datetime.datetime(hNow.year, hNow.month, hNow.day, int(self.heureDebutVeille), int(self.minDeDebutVeille),0,0)
				if hPV < hNow:
					print("heure courante < hPV on va voir l'heure suivante")
				else:
					f.close()
					return hPV

hCourante = datetime.datetime.now()
print("heure Courante", hCourante)
mesConsigne = Consigne()
heureVeille = mesConsigne.OuvreAgenda()
print("heure PV", heureVeille)
dureeVeille = mesConsigne.calculVeille()
print("duree veille",dureeVeille)

if (heureVeille == None):
	time.sleep(5)
	# a voir, plus d'heure de veille avant le lendemain

while True:
	hCourante = datetime.datetime.now()
	if hCourante < heureVeille:
		print("heure courant", hCourante)
		print("heure de veille", heureVeille)
		print("attend l'heure de veille")
		time.sleep(8)
	else:  		
		print
		print("transmission vers l'arduino")
		print("duree de la veille",heureVeille)
		time.sleep(8)
		exit
		# si heureCourante > heure
		# ProchaineVeille
		#	transmettre duree de veille
		#	shutdown
		#
		#ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
		#line = "bonjour"
		#ser.write(line)
		#ser.close()
