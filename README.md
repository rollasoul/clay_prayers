# clay_prayers
Densecap and torch-rnn create little prayers and metaphysical quotes out of clay. Client is raspberry pi (or any other machine running python)


# server setup

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

- install fswebcam for external usb-camera
```
install fswebcam
```
- run processing sketch (waits for incoming quotes): clay.pde
- run python script (waits for light sensor to detect light change, takes image of clay, sends it to server, gets quote)
```
python clay_pi.py
```
