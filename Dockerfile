FROM ubuntu

RUN mkdir /project
WORKDIR project

RUN apt-get update
RUN apt-get install -y git python-dev
RUN git clone https://github.com/pybombs/pybombs.git
WORKDIR pybombs

RUN printf "\n\n/usr/local\n\n\n\n\n\n\n\n\n\n" | ./pybombs config forcebuild ' '
RUN ./pybombs install gr-gsm
