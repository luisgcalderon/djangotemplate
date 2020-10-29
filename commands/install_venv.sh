#!/bin/bash
python3 -m pip install --user virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r src/django_myproject/requirements/dev.txt