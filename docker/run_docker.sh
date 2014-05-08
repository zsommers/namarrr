#! /bin/bash

docker build -t namarrr .

PORT=$(docker ps -l | sed -n 's/.*:\(.*\)-.*/\1/p')

echo "Site is running on http://localhost:$PORT"

docker run -t -p 8000 namarrr
