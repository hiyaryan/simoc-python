This script is a stripped down version of the sensor reading script with no bells
or whistles, so that developers can test try and get the sensor working in the
containers with the least hassle possible.

To run the docker container:
docker build - < Dockerfile
docker-compose up --remove-orphans

If you change the Docker file or the docker compose file, make sure to run
docker stop CONTAINER_NUMBER
docker rm CONTAINER_NUMBER

This version uses privileged mode and host mode. Instead of using privileged
mode, there is a way by modifying cgroup. There are also probably a few extra
unneeded dependecies to be simplified away in the Dockerfile.

A reset delay is added that delays the script start due to the use of native
Linux driver for the MCP2221. 
