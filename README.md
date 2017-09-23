# DoppelGallery

A web app that takes a picture of your face, and looks through thousands of historical paintings for people that look like you. Built with AWS, CockroachDB, and Tornado, using Python 2.7.

Hack the North 2017 winner! https://devpost.com/software/doppel-gallery

## Installation

You'll need about 80 GB of free space.

### Web Server

First, you'll need to create a Docker container for [Openface](https://cmusatyalab.github.io/openface/):
```
docker pull bamos/openface
docker run --name DoppelGallery -p 9000:9000 -p 8000:8000 -t -i bamos/openface /bin/bash
```
Then, clone this git repo into `~` on your Docker container:
```
cd ~
git clone https://github.com/descrip/doppelgallery.git
```
Install some Python packages that we'll need, and see if the web server works:
```
pip install tornado psycopg2
cd ~/doppelgallery
python server/app.py
```
Visit `localhost:8000`. If a webpage shows up, the web server is working! However, we still need some data.

### Gathering Data

DoppelGallery runs on paintings gathered from WikiArt. Kaggle provides a dataset, but you'll need to create a Kaggle account and accept the Terms of Service of the [Painter by Nubmers](https://www.kaggle.com/c/painter-by-numbers) competition. Afterwards, we'll download the Kaggle datasets onto the Docker container:
```
cd ~
pip install kaggle-cli
kg download -u username -p password -c painter-by-numbers -f train.zip
```
Where `username` and `password` are your Kaggle login credentials. `train.zip` is a 40 GB zip file that becomes around 80 GB when unzipped.

TODO

## Authors

Alex Rutar (@alexrutar)
Anthony Weston (@aeweston98)
Jack Zhang (@fakesquid)
Jeffrey Zhao (@descrip)
