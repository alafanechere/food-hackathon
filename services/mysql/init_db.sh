#!/bin/bash

docker rm -f social-media-2
docker build -t bnpmysql2 .

docker run -d -p 3306:3306 --name social-media-2 bnpmysql2
