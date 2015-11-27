###Night time Photo Capture- created by TeCoEd 2015###

import time
import os
import sys
import picamera
import subprocess
import RPi.GPIO as GPIO

time_of_photo = time.asctime( time.localtime(time.time()) )
print time_of_photo

GPIO.setmode(GPIO.BCM)
###Set up the PIR
PIR = 7
GPIO.setup(PIR, GPIO.IN)
###Set up the LISPARIO
GPIO.setup(10, GPIO.OUT) 
###Grabs the current time and day to add to the Tweet###
time_of_picture = time.asctime( time.localtime(time.time()) )
global File_Number ###number if photo
global file_name ###name of photo
File_Number = 1
  
def Nature_selfie(): ###Takes a picture of the wee Beastie###
    global File_Number
    global file_name
    GPIO.output(10, GPIO.HIGH)
    with picamera.PiCamera() as camera:
            #camera.start_preview()
            time.sleep(0.5)
            camera.annotate_text = time_of_photo	
            camera.capture("Nature" + str(File_Number) + ".jpg")
            file_name = "Nature" + str(File_Number) + ".jpg"
            print file_name
            File_Number = File_Number + 1
            GPIO.output(10, GPIO.LOW)  ###Turn off LISPARIO

def Motion_Sensing(PIR): ###Response to movement###
    print "We see you"
    Nature_selfie()
                
###Code to respond to a movement of the wee Beastie###            
print "Ready to find you"
time.sleep(2)

try:
    GPIO.add_event_detect(PIR, GPIO.RISING, callback=Motion_Sensing)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()




