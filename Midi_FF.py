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

while True:
	line =  ser.readline()
	if len(line) > 27 and len(line) < 32:
		values = line.split()
		counter = 0
		for x in values:
			values[counter] = int(x)
			counter = counter + 1
		threshMet = checkThresholds(values)
		if gun_ready == True and threshMet[2] and threshMet[3] and threshMet[1] and values[7] == 1 and values[8] == 0:
			print("AHHHH")
			gun_ready = False
			pygame.mixer.music.load("gun.wav")
			pygame.mixer.music.play()
		if threshMet[1] == False:
			gun_ready = True
	



