#!/bin/bash

echo pip incoming...
sudo apt-get install python-pip

echo flask incoming...
sudo apt install python3-flask

sudo apt install net-tools # for ifconfig

pip install --upgrade gcloud
pip install --upgrade google-api-python-client
