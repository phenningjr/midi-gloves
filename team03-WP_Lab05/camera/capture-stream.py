#! /usr/bin/python
# TEAM 3 WP - Pablo & Wei

import io
import time
import picamera

#Create an in-memory stream
my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
	camera.start_preview()
	#Camera warm-up time
	time.sleep(2)
	camera.capture(my_stream, 'jpeg')
	
