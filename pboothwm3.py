def start_photobooth(): 
	################################# Begin Step 1 ################################# 
	print "Get Ready" 
	camera = picamera.PiCamera()
	camera.resolution = (500, 375) #use a smaller size to process faster, and tumblr will only take up to 500 pixels wide for animated gifs
	camera.vflip = True
	camera.hflip = True
	camera.saturation = -100
	camera.start_preview()
	i=1 #iterate the blink of the light in prep, also gives a little time for the camera to warm up
	while i < prep_delay :
	  GPIO.output(led1_pin,True); sleep(.5) 
	  GPIO.output(led1_pin,False); sleep(.5); i+=1
	################################# Begin Step 2 #################################
	print "Taking pics" 
	now = time.strftime("%Y%m%d%H%M%S") #get the current date and time for the start of the filename
	try: #take the photos
		for i, filename in enumerate(camera.capture_continuous(file_path + now + '-' + '{counter:02d}.jpg')):
	    ib=1 #iterate the blink of the light in prep, also gives a little time for the camera to warm up
	    while ib < prep_delay :
	      GPIO.output(led1_pin,True); sleep(.5) 
	      GPIO.output(led1_pin,False); sleep(.5); ib+=1
			GPIO.output(led2_pin,True) #turn on the LED
			print(filename)
			#sleep(1) #pause the LED on for just a bit
			GPIO.output(led2_pin,False) #turn off the LED
			#sleep(capture_delay) # pause in-between shots
			if i == total_pics-1:
				break
	finally:
		camera.stop_preview()
		camera.close()
