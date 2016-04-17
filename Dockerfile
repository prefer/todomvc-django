FROM ubuntu:15.10
RUN apt-get update
RUN apt-get install -y python-pip
ADD REQUIREMENTS /tmp/REQUIREMENTS
RUN pip install -r /tmp/REQUIREMENTS

VOLUME /data/back
VOLUME /data/todomvc-backbone
WORKDIR /data/back

EXPOSE 8000
CMD []