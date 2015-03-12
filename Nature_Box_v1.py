###Nature_Box - created by TeCoEd###

import time
import os
import sys
import picamera
import subprocess
import tweepy
import RPi.GPIO as GPIO

# == OAuth Authentication ==###############
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'dsdfsfsdfgsdgdgd'
consumer_secret= 'gddgddgdgdgdg'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= '2dgfdgdgdgddsgdsgdggdfgdfg7'
access_token_secret= 'dgdsfgdfgdgfdgfdfgd'
#
#
###########################################

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

GPIO.setmode(GPIO.BCM)
PIR = 7
GPIO.setup(PIR, GPIO.IN)
###Grabs the current time and day to add to the Tweet###
time_of_tweet = time.asctime( time.localtime(time.time()) )
global File_Number ###number if photo
global file_name ###name of photo
File_Number = 1
  
def tweet_the_picture(): ###Code for the Picture added to the Tweet and sent###      
    global file_name
    api = tweepy.API(auth)
    photo_path = "/home/pi/Nature_Box/" + file_name ###will need to change name after test
    text = "Nature Box Photo taken @: " + time_of_tweet
    try:
        api.update_with_media(photo_path, text)
    except:
        print "Picture not sent"

def Nature_selfie(): ###Takes a picture of the wee Beastie###
    global File_Number
    global file_name
    with picamera.PiCamera() as camera:
            #camera.start_preview()
            time.sleep(0.5)
            camera.capture("Nature" + str(File_Number) + ".jpg")
            file_name = "Nature" + str(File_Number) + ".jpg"
            print file_name
            File_Number = File_Number + 1

def Motion_Sensing(PIR): ###Response to movement###
    print "We see you"
    Nature_selfie()
    #tweet_the_picture()
            
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


