#!/bin/sh
cd /code/cat-food-dispenser;
/usr/bin/python dispenser.py 21:00 >> ./logs.txt 2>&1 &
