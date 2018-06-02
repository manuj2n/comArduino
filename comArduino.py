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
		self.ligneVeille = []
		self.tableauVeille = []
		self.indexTableau = 0
		
	def OuvreAgenda(self):
		f = open(self.fichier, 'r')
		while True:
			chaine = f.readline()
			#print(chaine)
			if (chaine == ""):
				f.close()					
				return
			if (chaine[0] == "V"):
				hDV = chaine[1:3]
				mDV = chaine[4:6]
				hFV = chaine[7:9]
				mFV = chaine[10:12]
				heureDebutV = (int(hDV) * 3600) + (int(mDV) * 60)
				heureFinV = (int(hFV) * 3600) + (int(mFV) * 60)
				duree = heureFinV - heureDebutV
				self.ligneVeille = (heureDebutV, heureFinV, duree)
				self.tableauVeille.append(self.ligneVeille)
				self.indexTableau += 1

				#hNow = datetime.datetime.now()
				#hPV = datetime.datetime(hNow.year, hNow.month, hNow.day, int(hDV), int(mDV),0,0)


hC = datetime.datetime.now()
print("heure Courante", hC)
heureCourante = int(hC.hour * 3600) + int(hC.minute * 60) + int(hC.second)
print("heure Courante Secondes", heureCourante)
mesConsigne = Consigne()
heureVeille = mesConsigne.OuvreAgenda()
print("index", mesConsigne.indexTableau)
print(mesConsigne.tableauVeille)

''' print("heure PV", heureVeille)
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
		print("heure de la veille",heureVeille)
		print("duree de la veille",dureeVeille)
		time.sleep(8)
		exit '''
		# si heureCourante > heure
		# ProchaineVeille
		#	transmettre duree de veille
		#	shutdown
		#
		#ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
		#line = "bonjour"
		#ser.write(line)
		#ser.close()
