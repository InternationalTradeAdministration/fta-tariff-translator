#!/usr/bin/env bash

flake8
cd TariffRatesBlobTrigger
python3 unit_tests.py
cd ..
