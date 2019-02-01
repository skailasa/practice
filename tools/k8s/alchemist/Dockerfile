FROM ubuntu:18.10

MAINTAINER Srinath Kailasa "<srinathkailasa@gmail.com>"

RUN apt-get update
RUN apt-get install -y \
        python3 \
        python3-dev \
        python3-pip \
        build-essential

COPY . /alchemist
WORKDIR /alchemist

RUN echo $WORKDIR
RUN python3 setup.py install


EXPOSE 5000

CMD abracadabra
