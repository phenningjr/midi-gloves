#! /usr/bin/python
# TEAM 3 WP - Pablo & Wei

import time
import picamera
import datetime

ts = time.time()

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	# Camera warm-up time
	time.sleep(2)

	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	camera.capture(st+'.jpg')
