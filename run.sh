#!/bin/bash

source /.victhorious/conf/shell/envvars
python3 manage.py runserver --settings=bracketeer.settings.production
