#!/bin/bash

clear

export flask_app="src/server.py"
export FLASK_ENV=dev
export FLASK_DEBUG=true

python3 -m src.server