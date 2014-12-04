#! /usr/bin/python

import pygame
import serial
import time

pygame.mixer.init()
ch = []

for x in range(8):
	ch.append(pygame.mixer.Channel(x))

ser = serial.Serial('/dev/ttyACM0', 9600)
print "Initializing MIDI Glove"
time.sleep(1)
print "..."
time.sleep(1)
print "Ready!"

volume = 50
gun_ready = False
soundPlayed = False
notePlayed = [False, False, False, False]
C5 = pygame.mixer.Sound("C5.wav")
D5 = pygame.mixer.Sound("D5.wav")
E5 = pygame.mixer.Sound("E5.wav")
F5 = pygame.mixer.Sound("F5.wav")
G5 = pygame.mixer.Sound("G5.wav")
A5 = pygame.mixer.Sound("A5.wav")
B5 = pygame.mixer.Sound("B5.wav")
C6 = pygame.mixer.Sound("C6.wav")
CelloBb3 = pygame.mixer.Sound("CelloBb3.wav")
CelloC4 = pygame.mixer.Sound("CelloC4.wav")
CelloD4 = pygame.mixer.Sound("CelloD4.wav")
CelloE4 = pygame.mixer.Sound("CelloE4.wav")
CelloEb4 = pygame.mixer.Sound("CelloEb4.wav")
CelloF4 = pygame.mixer.Sound("CelloF4.wav")
CelloG3 = pygame.mixer.Sound("CelloG3.wav")
CelloG4 = pygame.mixer.Sound("CelloG4.wav")

vol = pygame.mixer.Sound("Volume.wav")

M1 = pygame.mixer.Sound("mario_itsme.wav")
M2 = pygame.mixer.Sound("mario_haha.wav")
M3 = pygame.mixer.Sound("mario_jump2.wav")
M4 = pygame.mixer.Sound("mario_powerup.wav")

previousThumb = 1

######################################
# Values note 			     #
######################################
# 0 = index finger		     #
# 1 = middle finger		     #
# 2 = ring finger		     #
# 3 = pinky			     #
# 4 = thumb			     #
# 5 = thumb curled		     #
# 6 = current note playing (1 to 4)  #
# 7 = mode (0, 1, or 2)		     #
# 8 = mode just changed (0 or 1)     #
# 9 = accelerometer x		     #
# 10 = accelerometer y  	     #
# 11 = accelerometer z		     #
# 12 = gyro x                        #
# 13 = gyro y                        #
# 14 = gyro z                        #
######################################	

def checkThresholds(list):
	counter = 0
	thresholds = [300,618,280,625,370]
	threshMet = [True,True,True,True,True]
	for x in list:
		if counter < 5:
			if x < thresholds[counter]:
				threshMet[counter] = True
			else:
				threshMet[counter] = False
			counter = counter + 1
	return threshMet



while True:
	line =  ser.readline()
	if len(line) > 45 and len(line) < 70:
		values = line.split()
		counter = 0
		for x in values:
			values[counter] = int(x)
			counter = counter + 1
		threshMet = checkThresholds(values)

		if values[8] == 1 and soundPlayed == False:
			if values[7] == 0:
				modeSound = pygame.mixer.Sound("Piano Mode.wav")			
			elif values[7] == 1:
				modeSound = pygame.mixer.Sound("Mario Mode.wav")	
			elif values[7] == 2:
				modeSound = pygame.mixer.Sound("Sound Effect Mode.wav")
			elif values[7] == 3:
				modeSound = pygame.mixer.Sound("Game of Thrones Mode.wav")
			elif values[7] == 4:
				modeSound = pygame.mixer.Sound("Volume Mode.wav")
			if soundPlayed == False:
				pygame.mixer.music.stop()
				modeSound.play()
				soundPlayed = True
		elif values[8] == 0:
			soundPlayed = False
		#PIANO MODE
		if values[7] == 0 and values[8] == 0:
			vol.stop()
			print "Piano Mode"
			if values[5] == 0:
				if values[6] == 1 and notePlayed[0] == False:
					ch[0].play(C5)
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					ch[1].play(D5)
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					ch[2].play(E5)
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					ch[3].play(F5)
					notePlayed[3] = True
			elif values[5] == 1:
				if values[6] == 1 and notePlayed[0] == False:
					ch[4].play(G5)
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					ch[5].play(A5)
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					ch[6].play(B5)
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					ch[7].play(C6)
					notePlayed[3] = True
			for x in range(0,4):
				if threshMet[x] == False:
					notePlayed[x] = False

		#MARIO MODE
		elif values[7] == 1 and values[8] == 0:	
			print "Mario Mode"
			if values[5] == 0 and previousThumb == 1:
				pygame.mixer.music.stop()
				pygame.mixer.music.load("mario_tsong.wav")
				pygame.mixer.music.set_volume(ch[0].get_volume())
				pygame.mixer.music.play(-1,0)
			elif values[5] == 1 and previousThumb == 0:
				pygame.mixer.music.stop()
				pygame.mixer.music.load("mario_starsong.wav")
				pygame.mixer.music.set_volume(ch[0].get_volume())
				pygame.mixer.music.play(-1,0)
			if values[6] == 1 and notePlayed[0] == False:
				ch[0].play(M1)
				notePlayed[0] = True
			if values[6] == 2 and notePlayed[1] == False:
				ch[1].play(M2)
				notePlayed[1] = True
			if values[6] == 3 and notePlayed[2] == False:
				ch[2].play(M3)
				notePlayed[2] = True
			if values[6] == 4 and notePlayed[3] == False:
				ch[3].play(M4)
				notePlayed[3] = True

			for x in range(0,4):
				if threshMet[x] == False:
					notePlayed[x] = False

			previousThumb = values[5]


		#SOUND EFFECT MODE
		elif values[7] == 2 and values[8] == 0:
			print "Sound Effect"
			if gun_ready == True and threshMet[2] and threshMet[3] and threshMet[1] and values[8] == 0:
				print("AHHHH")
				gun_ready = False
				gun = pygame.mixer.Sound("gun.wav")
				ch[1].play(gun)
			if threshMet[1] == False:
				gun_ready = True
		
		#GAME OF THRONES MODE
		elif values[7] == 3 and values[8] == 0:
			print"Game of Thrones"
			if values[5] == 0:
				if values[6] == 1 and notePlayed[0] == False:
					ch[0].play(CelloG4)
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					ch[1].play(CelloF4)
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					ch[2].play(CelloEb4)
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					ch[3].play(CelloC4)
					notePlayed[3] = True
			elif values[5] == 1:
				if values[6] == 1 and notePlayed[0] == False:
					ch[0].play(CelloD4)
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					ch[1].play(CelloBb3)
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					ch[2].play(CelloE4)
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					ch[3].play(CelloG3)
					notePlayed[3] = True
			for x in range(0,4):
				if threshMet[x] == False:
					notePlayed[x] = False
					ch[x].stop()
		#VOLUME MODE
		elif values[7] == 4 and values[8] == 0:
			print "Volume Mode"
			vol.play()
			if values[10] > 20000:
				volLevel = 0
			else:
				volLevel = (abs(values[10]-3000.0)) / 13000.0
			if volLevel > 1:
				volLevel = 1
			
			for x in ch:
				x.set_volume(volLevel)


			
	
