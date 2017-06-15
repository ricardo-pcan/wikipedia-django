#!/bin/bash
pip install -r requirements/$1
chown -R $USER:$USER .
python manage.py runserver_plus 0.0.0.0:8000
