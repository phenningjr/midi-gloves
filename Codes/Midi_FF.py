#! /usr/bin/python

import pygame
import serial
import time

pygame.mixer.init()
ch1 = pygame.mixer.Channel()

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

M1 = pygame.mixer.Sound("mario_itsme.wav")
M2 = pygame.mixer.Sound("mario_haha.wav")
M3 = pygame.mixer.Sound("mario_jump2.wav")
M4 = pygame.mixer.Sound("mario_powerup.wav")

previousThumb = 0

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
	thresholds = [350,350,330,370,400]
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
	if len(line) > 27 and len(line) < 32:
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
				modeSound.play()
				soundPlayed = True
		elif values[8] == 0:
			soundPlayed = False

		#PIANO MODE
		if values[7] == 0 and values[8] == 0:
			pygame.mixer.music.stop()
			if values[5] == 0:
				if values[6] == 1 and notePlayed[0] == False:
					C5.play()
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					D5.play()
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					E5.play()
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					F5.play()
					notePlayed[3] = True
			elif values[5] == 1:
				if values[6] == 1 and notePlayed[0] == False:
					G5.play()
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					A5.play()
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					B5.play()
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					C6.play()
					notePlayed[3] = True
			for x in range(0,4):
				if threshMet[x] == False:
					notePlayed[x] = False

		#MARIO MODE
		elif values[7] == 1 and values[8] == 0:
			
			if values[5] == 0 and previousThumb == 1:
				pygame.mixer.music.stop()
				pygame.mixer.music.load("mario_song.wav")
				pygame.mixer.music.play(-1,0)
				
			elif values[5] == 1 and previousThumb == 0:
				pygame.mixer.music.stop()
				pygame.mixer.music.load("mario_starsong.wav")
				pygame.mixer.music.play(-1,0)

			if values[6] == 1 and notePlayed[0] == False:
					M1.play()
					notePlayed[0] = True
				if values[6] == 2 and notePlayed[1] == False:
					M2.play()
					notePlayed[1] = True
				if values[6] == 3 and notePlayed[2] == False:
					M3.play()
					notePlayed[2] = True
				if values[6] == 4 and notePlayed[3] == False:
					M4.play()
					notePlayed[3] = True

			for x in range(0,4):
				if threshMet[x] == False:
					notePlayed[x] = False

			previousThumb = values[5]


		#SOUND EFFECT MODE
		elif values[7] == 2 and values[8] == 0:
			pygame.mixer.music.stop()
			if gun_ready == True and threshMet[2] and threshMet[3] and threshMet[1] and values[8] == 0:
				print("AHHHH")
				gun_ready = False
				pygame.mixer.music.load("gun.wav")
				pygame.mixer.music.play()
			if threshMet[1] == False:
				gun_ready = True
		
		#GAME OF THRONES MODE
		elif values[7] == 3 and values[8] == 0:

		#VOLUME MODE
		elif values[7] == 4 and values[8] == 0:
			pygame.mixer.music.stop()
			pygame.music.load("Volume.wav")
			pygame.music.play(-1,0)
			
			volLevel = (abs(values[10]-3000)) / 13000
			if volLevel > 1:
				volLevel = 1

			channel.set_volume(volLevel)
			print volLevel

		#MARACA(S) MODE

			
	
