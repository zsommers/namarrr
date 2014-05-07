# Dockerfile to run Namarrr

FROM ubuntu
MAINTAINER Zach Sommers, zsommers@gmail.com

# Update repos
RUN apt-get update

# General dependencies
RUN apt-get install -y git

# Django dependencies
RUN apt-get install -y python3-dev
RUN apt-get install -y libpq-dev

# Download repo
RUN git clone https://github.com/zsommers/namarrr.git

# Django requirements
# RUN python3 -m pip install -r namarrr/requirements/production.txt

ENTRYPOINT ["/bin/bash"]
