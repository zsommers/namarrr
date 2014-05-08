#! /bin/bash

docker build -t namarrr .

docker run -t -d -p 8000 namarrr

PORT=$(docker ps | grep namarrr | sed -n 's/.*:\(.*\)-.*/\1/p')

echo "Site is running on http://localhost:$PORT"
