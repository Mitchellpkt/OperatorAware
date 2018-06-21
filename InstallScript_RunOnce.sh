#!/bin/bash

echo pip incoming...
#sudo apt-get install python-pip
sudo apt-get install python3-pip




######
# Do we need a virtual environment?
# echo virtualenv incoming...
# sudo apt-get install virtualenv
# virtualenv Insight
# something something activate

pip3 install conda

echo flask incoming...
sudo apt install python3-flask

echo snag net-tools
sudo apt install net-tools # for ifconfig

echo gcloud stuff
pip3 install --upgrade google-cloud #?
pip3 install --upgrade google-cloud-speech
pip3 install --upgrade gcloud
pip3 install --upgrade google-api-python-client

