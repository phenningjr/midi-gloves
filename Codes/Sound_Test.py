#! /usr/bin/python

import pygame
import serial
import time

pygame.mixer.init()
time.sleep(2)
pygame.mixer.music.load("gun.wav")
time.sleep(1)
pygame.mixer.music.play()
time.sleep(1)
while pygame.mixer.get_busy():
	continue	



