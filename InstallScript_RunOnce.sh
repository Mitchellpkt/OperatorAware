#!/bin/bash

echo pip incoming...
sudo apt-get install python-pip

######
# Do we need a virtual environment?
# echo virtualenv incoming...
# sudo apt-get install virtualenv
# virtualenv Insight
# something something activate

pip install conda

echo flask incoming...
sudo apt install python3-flask

echo snag net-tools
sudo apt install net-tools # for ifconfig

echo gcloud stuff
pip install google-cloud #?
pip install --upgrade gcloud
pip install --upgrade google-api-python-client
