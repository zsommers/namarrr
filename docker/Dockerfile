# Dockerfile to run Namarrr

FROM ubuntu
MAINTAINER Zach Sommers, zsommers@gmail.com

# Update repos
RUN apt-get update

# General dependencies
RUN apt-get install -y git python3-pip

# psycopg2 dependencies
RUN apt-get install -y python3-dev libpq-dev

# Download repo
RUN git clone https://github.com/zsommers/namarrr.git

WORKDIR /namarrr

# Django requirements
# RUN pip3 install -r namarrr/requirements/production.txt

ENTRYPOINT ["/bin/bash"]
