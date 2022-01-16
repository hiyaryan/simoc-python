FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip

RUN python3 -m pip install adafruit-circuitpython-scd30 hidapi
