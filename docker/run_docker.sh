#! /bin/bash

docker build -t namarrr .

PORT=docker inspect --format='{{(index (index .HostConfig.PortBindings "8000/tcp") 0).HostPort}}' namarrr

echo "Site is running on http://localhost:$PORT"

docker run -t -p 8000 namarrr
