import RPi.GPIO as GPIO
import os 
import subprocess
import time
import socket
from subprocess import Popen, PIPE, STDOUT

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) 

p = GPIO.PWM(22, 100)
GPIO.output(22, True)

#GPIO.setmode(GPIO.BOARD)
TRIG = 18 
ECHO = 23
print "Distance Measurement In Progress"
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)
counter = 0


def sensor():
	global counter
	# sense if hands form clay with distance sensor
	try:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		while GPIO.input(ECHO)==0:
				pulse_start = time.time()
		while GPIO.input(ECHO)==1:
				pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)
		print "Distance:",distance,"cm"
		#take image and get quote when hands are taken out
		if distance < 11:
			time.sleep(1)
			counter +=1
			print "hands in"
			print counter	
		if distance > 11 and counter > 1:
			print "hands out"
			counter = 0
			#take image of clay, send it off to server for analysis and quote generation
			# get the quote and save it to file
			
			# empty quote
			open('clay1.txt', 'w').close()
			# timer triggers webcam to take image
			os.system('fswebcam --no-banner -S 20 claycam.jpg')
			# send image
			s = socket.socket()
			host = "TO DO: insert external ip-address of remote server here!"
			port = 12345
			s.connect((host, port))
			time.sleep (2)
			f=open ("claycam.jpg", "rb") 
			l = f.read(2048)
			while (l):
				s.send(l)
				l = f.read(2048)
			s.send("end")
			time.sleep(2)
			print "image sent"   
			s.close() 
			# wait for densecap & torch-rnn to write quote
			print "done"
			time.sleep(6)
			s = socket.socket()
			host = "TO DO: insert external ip-address of remote server here!"
			port = 12345        
			s.connect((host, port))
			print " get quote"
			l = s.recv(1024)
			clay = open("clay1.txt", "w")
			clay.write(l)
			clay.close()			
			s.send("file received")
			s.close()
	except RuntimeError:
		pass

try:

  while True:

    sensor()
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()


