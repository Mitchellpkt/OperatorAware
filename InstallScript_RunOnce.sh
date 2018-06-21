#!/bin/bash

#####################
## OPERATOR AWARE 
## MitchellPKT@pm.me
## Run this once
#####################


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
cd ~/anaconda3/bin
./conda update anaconda # may need to adjust the path
echo If conda not recognized, add anaconda bin to path
echo ... learned hard way: append not replace. *cough*
echo you may be able to skip this. 
## Export path if needed
# e.g. export path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/pwn_me_user/anaconda3/bin"
conda create -n insight python=3
source activate insight
conda install numpy scipy pandas matplotlib flask scikit-learn jupyter

#####################
# Install anaconda
# echo flask incoming...
# sudo apt install python3-flask

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
# Decrypt API keys (symmetric PGP)
# contact MPKT for password
cd ~/OperatorAware # Navigate back to Operator Aware path 
echo decrypting keys
gpg -d --output OperatorAware-5f653aaf3399.json OperatorAware-5f653aaf3399.json.gpg 

#####################
# make .gitignore
cp IgnoreThese.gitignore .gitignore

#####################
# Create supervisor password
echo DefaultPassword>SupervisorPassword.txt


