#!/bin/bash

#####################
# Install pip
echo pip incoming...
#sudo apt-get install python-pip
sudo apt-get install python3-pip

#####################
# Install anaconda
wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
chmod +777 Anaconda3-5.2.0-Linux-x86_64.sh
bash Anaconda3-5.2.0-Linux-x86_64.sh
## go through the install
cd ~/anaconda3/bin # may need to adjust the path
echo IF THERE IS AN ERROR NEXT, ADD PATH TO ENV VARS
## NEED A LINE HERE TO EXPORT PATH
./conda update anaconda
conda create -n insight python=3
source activate insight
conda install numpy scipy pandas matplotlib flask scikit-learn jupyter

#####################
# Install anaconda
echo flask incoming...
sudo apt install python3-flask

#####################
# Install gcloud, etc
echo gcloud stuff
pip3 install --upgrade google-cloud #?
pip3 install --upgrade google-cloud-speech
pip3 install --upgrade gcloud
pip3 install --upgrade google-api-python-client

#####################
# Install net-tools 
echo snag net-tools
sudo apt install net-tools # for ifconfig

#####################
# DecryptKeys
# contact MPKT for password
echo decrypting keys
gpg -d --output OperatorAware-5f653aaf3399.json OperatorAware-5f653aaf3399.json.gpg 

#####################
# make .gitignore
cp IgnoreThese.gitignore .gitignore

#####################
# Create supervisor password
echo DefaultPassword>SupervisorPassword.txt


