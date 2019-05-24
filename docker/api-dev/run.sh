#!/bin/bash

dockerize -wait tcp://db:5432 -timeout 20s

# Apply database migrations
echo "Database launched finish"
/usr/local/bin/python3 /home/main.py