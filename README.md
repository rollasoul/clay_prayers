![alt tag](https://github.com/rollasoul/clay_prayers/blob/master/16265646_243260219456703_1608198604390170781_n.jpg)

# clay_prayers
Densecap and torch-rnn create little prayers and metaphysical quotes out of clay. Client is raspberry pi (or any other machine running python)

# server setup

All of the files above for running the server are included in the docker image, no need to git clone them.

- install docker on remote server (ubuntu 16.04)
```
sudo apt-get install docker.io
```

- run docker image (will start download and image)
```
docker run -it -p 12345:12345 rollasoul/clay_phil
```

- run python script (loops clay.py to continuously listen for incoming data from client, analyses image with densecap, seeds haiku-captions to torch-rnn, generates quote, sends it back to client)
```
python clay-run.py
```

# raspberry pi setup:

Git clone the repository to get all the files.

- install fswebcam for external usb-camera
```
install fswebcam
```
- run python script (starts processing sketch, waits for light sensor to detect light change, takes image of clay, sends it to server, gets quote, displays it in sketch)
```
python clay_run_pi.py
```
