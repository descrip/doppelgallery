# DoppelGallery

A web app that takes a picture of your face, and looks through thousands of historical paintings for people that look like you. Built with AWS and CockroachDB.

Hack the North 2017 winner! https://devpost.com/software/doppel-gallery

## Installation

First, you'll need to create a Docker container for [Openface](https://cmusatyalab.github.io/openface/):
```
docker pull bamos/openface
docker run --name DoppelGallery -p 9000:9000 -p 8000:8000 -t -i bamos/openface /bin/bash
```
Then, clone this git repo into your Docker container:
```
cd ~
git clone https://github.com/descrip/doppelgallery.git
```
Install some Python packages that we'll need
```
sudo pip install tornado psycopg2 
```

## Authors

Alex Rutar (@alexrutar)
Anthony Weston (@aeweston98)
Jack Zhang (@fakesquid)
Jeffrey Zhao (@descrip)
