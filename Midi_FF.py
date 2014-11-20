#! /usr/bin/python

import pygame
import serial
import time

pygame.mixer.init()

ser = serial.Serial('/dev/ttyACM0', 9600)
print "Initializing MIDI Glove"
time.sleep(1)
print "..."
time.sleep(1)
print "Ready!"

gun_ready = False

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

soundPlayed = False
notePlayed = [False, False, False, False]

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
			if soundPlayed == False:
				modeSound.play()
				soundPlayed = True
		elif values[8] == 0:
			soundPlayed = False

		if values[7] == 0 and values[8] == 0:
			
			if values[5] == 0:
				if values[6] == 1 and notePlayed == False:
					pygame.mixer.music.load("C5.wav")
					pygame.mixer.music.play()
					notePlayed[0] = True
				if values[6] == 2 and notePlayed == False:
					pygame.mixer.music.load("D5.wav")
					pygame.mixer.music.play()
					notePlayed[1] = True
				if values[6] == 3 and notePlayed == False:
					pygame.mixer.music.load("E5.wav")
					pygame.mixer.music.play()
					notePlayed[2] = True
				if values[6] == 4 and notePlayed == False:
					pygame.mixer.music.load("F5.wav")
					pygame.mixer.music.play()
					notePlayed[3] = True
			elif values[5] == 1:
				if values[6] == 1 and notePlayed == False:
					pygame.mixer.music.load("G5.wav")
					pygame.mixer.music.play()
					notePlayed[0] = True
				if values[6] == 2 and notePlayed == False:
					pygame.mixer.music.load("A5.wav")
					pygame.mixer.music.play()
					notePlayed[1] = True
				if values[6] == 3 and notePlayed == False:
					pygame.mixer.music.load("B5.wav")
					pygame.mixer.music.play()
					notePlayed[2] = True
				if values[6] == 4 and notePlayed == False:
					pygame.mixer.music.load("C6.wav")
					pygame.mixer.music.play()
					notePlayed[3] = True
			for x in range(0:3):
				if threshMet[x] == False:
					notePlayed[x] = False

		
		elif values[7] == 2:
			if gun_ready == True and threshMet[2] and threshMet[3] and threshMet[1] and values[8] == 0:
				print("AHHHH")
				gun_ready = False
				pygame.mixer.music.load("gun.wav")
				pygame.mixer.music.play()
			if threshMet[1] == False:
				gun_ready = True
	



