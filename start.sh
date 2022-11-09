#!/bin/bash

python3 -m pip install -r requirements3.txt \
 & git clone https://github.com/GiovanH/mdexts.git \
 & git clone https://github.com/GiovanH/peliplugins.git
 
wait

python3 server.py
