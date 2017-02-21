<img src="https://github.com/rollasoul/clay_prayers/blob/master/16265646_243260219456703_1608198604390170781_n.jpg" width="400">

# clay_prayers
Densecap and torch-rnn create philosophical quotes out of clay. Client is raspberry pi (or any other machine running python).
Prototype on vimeo: https://vimeo.com/202647741/ce96d7d976  

# server setup

All of the files above for running the server are included in the docker image, no need to git clone them.

- install docker on remote server (ubuntu 16.04, minimum 6GB RAM)
```
sudo apt-get install docker.io
```

- run docker image (will start download and image)
```
docker run -it -p 12345:12345 rollasoul/meta_clay
```
- run python script (loops clay.py to continuously listen for incoming data from client, analyses image with densecap, seeds haiku-captions to torch-rnn, generates quote, sends it back to client)
```
python clay_script.py
```

# raspberry pi setup:
Tested on raspberry pi 3 running raspbian jessie (2017-01-11).
- connect USB-webcam and light-sensor to raspberry pi
- git clone the repository to get all the files, change server address in clay_pi.py
- install fswebcam for external usb-camera
```
sudo apt-get install fswebcam
```
- enter the external ip-address of your remote server in clay_pi.py lines 19 and 37
- run processing script "clay.pde" - will ask if it should create folder for .pde, click "yes"
- run python script (starts processing sketch, waits for light sensor to detect light change, takes image of clay, sends it to server, gets quote, displays it in sketch)
```
sudo python clay_pi.py
```
- if you have a distance sensor like the HC-RS04, run this script instead
```
sudo python clay_senses.py
```

# mac setup:
(in case you have no raspberry pi and no light-sensor)
- using built-in camera
- git clone the repository to get all the files, change server address in clay_mac.py.
- install cv2/openCV via homebrew for built-in camera access with this tutorial: http://seeb0h.github.io/howto/howto-install-homebrew-python-opencv-osx-el-capitan/
- enter the external ip-address of your remote server in clay_mac.py lines 21 and 39

- run processing script "clay.pde" - will ask if it should create folder for .pde, click "yes"
- run python script continuously from inside your git-folder(starts processing sketch, takes image of clay, sends it to server, gets quote, displays it in sketch)
```
sudo python clay_mac.py
```
