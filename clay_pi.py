import socket
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time

import RPi.GPIO as GPIO

# timer triggers webcam to take image
#time.sleep (60)
os.system('fswebcam --no-banner -S 20 claycam.jpg')

# save record of image
#time2 = time.time()
#filename = "/Users/rollasoul/densecap/imgs/saved/%sa-image.jpg"%time2
#cv2.imwrite(filename, image)

# send image
s = socket.socket()
host = "147.75.101.37"
port = 12345
s.connect((host, port))
time.sleep (2)
f=open ("claycam.jpg", "rb") 
l = f.read(4096)
while (l):
      s.send(l)
      l = f.read(4096)
time.sleep(3)
print "image sent"   
s.close()                # Close the connection

    # wait for densecap & torch-rnn to write quote
print "done"
time.sleep(6)
s = socket.socket()
host = "147.75.101.37"
port = 12345

s.connect((host, port))
print s.recv(1024)
while True:
        i=1
        f = open('clay'+ str(i)+".txt",'wb')
        i=i+1
        while (True):
        # receive and write file
                l = s.recv(1024)
                while (l):
                        f.write(l)
                        l = s.recv(1024)
                        print "file received"
                        s.send('file received')
                s.close()
                f.close()
