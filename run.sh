#!/bin/sh

exec docker run --name najasci_run \
  -v "$PWD":/usr/src/app \
  -w /usr/src/app \
  --rm -it python:3 python index.py