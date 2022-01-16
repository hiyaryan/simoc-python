This script is a stripped down version of the sensor reading script with no bells
or whistles, so that developers can test try and get the sensor working in the
containers with the least hassle possible.

To run the docker container:
docker build - < Dockerfile
docker-compose up --remove-orphans

If you change the Docker file or the docker compose file, make sure to run
docker stop CONTAINER_NUMBER
docker rm CONTAINER_NUMBER
docker image rm IMAGE_NUMBER --force

This version uses privileged mode and host mode. Instead of using privileged
mode, there is a way by modifying cgroup in the docker-compose file.

If there are issues with the native Linux driver for the MCP2221, the reset delay 
set to 20 should fix that, but running this containe on an Ubuntu 20 machine with the
driver overridden seems to work without the reset delay.

The current version of the docker-compose file may be redundant to have the
/dev/ttyACM0 as wel ass /dev:/dev if the sensor always shows up on ttyACM0

The network_mode: host and the /run/udev/control volume may be necessary
to recognize if the sensor is disconnected and reconnected but further testing
may be necessary to verify this.
