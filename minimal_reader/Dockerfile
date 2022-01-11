FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-pip \
    python3-setuptools \
    libusb-1.0.0-dev \
    libudev-dev \
    libusb-1.0 \
    libhidapi-dev \
    net-tools

RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install adafruit-circuitpython-scd30 hidapi
