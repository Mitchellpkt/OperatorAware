#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="/home/pwn_me_user/OperatorAware/OperatorAware-5f653aaf3399.json"

export FLASK_APP=OperatorAwareFlaskTop.py

flask run --host 0.0.0.0 --port 2600
