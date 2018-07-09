#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="/home/pwn_me_user/operatoraware/OperatorAware-5f653aaf3399.json"

export FLASK_APP=OperatorAwareFlaskTop.py

export FLASK_ENV=development

flask run --host 0.0.0.0 --port 2600
