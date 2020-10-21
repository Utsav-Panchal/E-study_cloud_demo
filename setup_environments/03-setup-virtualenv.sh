#!/usr/bin/env bash
ENV_DIR=venv

sudo apt-get -y install python-virtualenv
virtualenv ${ENV_DIR} --python=`which python3.7`
source ${ENV_DIR}/bin/activate

pip install -r requirements/local.txt
pip install -r requirements/production.txt
