#!/bin/bash

conda create -y -n prosodic_env python=2.7 nltk
source activate prosodic_env
pip install prosodic
python tools/get_nltk.py
