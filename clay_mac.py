import socket
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time
import cv2

while True:
	# capture image from webcam, change directory to (densecap)pics folder, write image to folder
	vidcap = cv2.VideoCapture()
	vidcap.open(0) 		# 1 for external 0 for internal cam
	retval, image = vidcap.retrieve()
	vidcap.release()

	face_file_name = "claycam.jpg"
	os.chdir('/Users/rollasoul/clay_prayers')
	cv2.imwrite(face_file_name, image)

	# send image
	s = socket.socket()
	host = "TO DO: enter remote server ip"
	port = 12345
	s.connect((host, port))
	time.sleep (2)
	f=open ("claycam.jpg", "rb") 
	l = f.read(4096)
	while (l):
				s.send(l)
				l = f.read(4096)
	s.send("end")
	time.sleep(2)
	print "image sent"   
	s.close()                # Close the connection

		# wait for densecap & torch-rnn to write quote
	print "done"
	time.sleep(6)
	s = socket.socket()
	host = "TO DO: enter remote server ip"
	port = 12345
	        
	s.connect((host, port))
	l = s.recv(1024)
	clay = open("clay1.txt", "w")
	clay.write(l)
	clay.close()			
	s.send("file received")
	s.close()
	
