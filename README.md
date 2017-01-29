# clay_prayers
densecap and torch-rnn create little prayers and metaphysical quotes out of clay


# server setup

- install docker on remote server (ubuntu 16.04)
```
sudo apt-get install docker.io
```

- run docker image (will start download and image)
```
docker run -it -p 12345:12345 rollasoul/clay_phil
```

- run python script
```
python clay.py
```

# raspberry pi setup:

- install fswebcam for external usb-camera
```
install fswebcam
```
- run python script
```
python clay_pi.py
```
-- still experimental, processing sketch not tested yet on pi --
