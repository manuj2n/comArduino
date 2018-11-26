#! /usr/bin/env python
# -*- coding: utf-8 -*-
# manuj2n
# comArduino

import datetime
import time
import sys
import serial
import os

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
			if (chaine[0] == "D"):
				tempsDepartDiffere = chaine[1:3]
				departDiffSecondes = int(tempsDepartDiffere) * 3600
				t = open('tmp.txt','w')
				while True:
					chaine = f.readline()
					if (chaine == ""):
						f.close()
						t.close()
						os.remove('agenda.txt')
						os.rename('tmp.txt','agenda.txt')
						print("Transmet le temps de veille : ",departDiffSecondes)
						print(departDiffSecondes)
						# Transmet le temps de veille a Arduino
						TransRS232(departDiffSecondes)
						# Shutdown
						os.system("sudo shutdown -h now")
						exit(0)
					t.write(chaine)

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

def TransRS232(commande):
	line = "STOP:" + str(commande) + '\n'
	print(line)
 	ser = serial.Serial('/dev/ttyS0', 9600, dsrdtr=0)
	ser.write(line)
	ser.close()

def HeureCouranteSeconde():
	hC = datetime.datetime.now()
	#print("heure Courante", hC)
	heureCourante = int(hC.hour * 3600) + int(hC.minute * 60) + int(hC.second)
	return heureCourante

# debut du programme
# test si le fichier agenda.txt existe.
try:
	f = open('agenda.txt', 'r')
	f.close()
except:
	print("erreur de fichier")
	print("quitte le programme")
	sys.exit(0)

print("heure Courante Secondes", HeureCouranteSeconde())
mesConsigne = Consigne()
heureVeille = mesConsigne.OuvreAgenda()
print("index", mesConsigne.indexTableau)
print(mesConsigne.tableauVeille)

i = 0
while i < mesConsigne.indexTableau:
	print(mesConsigne.tableauVeille[i][0])
	# l'heure courante tombe dans un creneau de veille
	if (HeureCouranteSeconde() > mesConsigne.tableauVeille[i][0]) and (HeureCouranteSeconde() < mesConsigne.tableauVeille[i][1]):
		print("heureCourante dans le range :",mesConsigne.tableauVeille[i][0:2])
		print("heureCourante :",HeureCouranteSeconde())
		tempsRestantVeille = mesConsigne.tableauVeille[i][1] - HeureCouranteSeconde()
		print("temps de veille restant :", tempsRestantVeille)
		#
		# transmission du temps de veille restant a l'arduino
		TransRS232(tempsRestantVeille)
		# command "shutdown"
		os.system("sudo shutdown -h now")
		# on quitte le programme le programme
		sys.exit(0)
	if (HeureCouranteSeconde() < mesConsigne.tableauVeille[i][0]) and (HeureCouranteSeconde() < mesConsigne.tableauVeille[i][1]):
		print("heureCourante dans une phase de reveil :",mesConsigne.tableauVeille[i][0])
		print("heureCourante :",HeureCouranteSeconde())
		tempsRestantReveille = mesConsigne.tableauVeille[i][0] - HeureCouranteSeconde()
		print("temps de reveil restant :", tempsRestantReveille)
		while (HeureCouranteSeconde() < mesConsigne.tableauVeille[i][0]):
    		# on est dans un creneau de fonctionnement, on cherche la prochaine heure de veille
			time.sleep(1)
			pass
		print("Cest la fin de la phase de reveil :",mesConsigne.tableauVeille[i][0])
		print("heureCourante :",HeureCouranteSeconde())
 		tempsRestantVeille = mesConsigne.tableauVeille[i][1] - HeureCouranteSeconde()
		print("temps de veille a venir :", tempsRestantVeille)
		#
		# transmission du temps de veille restant a l'arduino
		TransRS232(tempsRestantVeille)
		# command "shutdown"
		os.system("sudo shutdown -h now")  	
		# et on attend que l'heure arrive pour passer en veille
		sys.exit(0)
	i += 1


