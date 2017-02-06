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
docker run -it -p 12345:12345 rollasoul/clay_phil
```

- run python script (loops clay.py to continuously listen for incoming data from client, analyses image with densecap, seeds haiku-captions to torch-rnn, generates quote, sends it back to client)
```
python clay_script.py
```

# raspberry pi setup:
Tested on Raspbian Jessie (2017-01-11).
Git clone the repository to get all the files, change server address in clay_pi.py fi.
- install fswebcam for external usb-camera
```
sudo apt-get install fswebcam
```
- run processing script "clay.pde" - will ask if it should create folder for .pde, click "yes"
- run python script (starts processing sketch, waits for light sensor to detect light change, takes image of clay, sends it to server, gets quote, displays it in sketch)
```
python clay_pi.py
```
