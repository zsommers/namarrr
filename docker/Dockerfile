# Dockerfile to run Namarrr

FROM ubuntu
MAINTAINER Zach Sommers, zsommers@gmail.com

# Update repos
RUN apt-get update

# General dependencies
RUN apt-get install -y git python3-pip

# Download repo
RUN git clone https://github.com/zsommers/namarrr/
WORKDIR /namarrr
RUN git checkout demo

# Django requirements
RUN pip3 install -r requirements/demo.txt

# Setup Namarrr env variables
ENV NAMARRR_KEY "notforproduction"
ENV DJANGO_SETTINGS_MODULE django_namarrr.settings.demo

WORKDIR /namarrr/django_namarrr

# Load initial data
RUN python3 manage.py migrate
RUN python3 manage.py loaddata ../docker/init_data.json

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000
#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["python3", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]
