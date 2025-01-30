#!/bin/bash

clear

export flask_app="src/server.py"
export flask_debug=true

python3 -m src.server