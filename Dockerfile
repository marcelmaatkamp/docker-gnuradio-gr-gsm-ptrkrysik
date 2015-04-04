FROM ubuntu

RUN apt-get update
RUN mkdir -p /var/run/sshd /root/.ssh
RUN apt-get install -y openssh-server
RUN locale-gen en_US en_US.UTF-8

RUN mkdir /project
WORKDIR project

RUN apt-get update
RUN apt-get install -y git python-dev
RUN git clone https://github.com/pybombs/pybombs.git
WORKDIR pybombs

RUN printf "\n\n/usr/local\n\n\n\n\n\n\n\n\n\n" | ./pybombs config forcebuild ' '
ADD airprobe_rtlsdr_nogui.py /usr/local/bin/airprobe_rtlsdr_nogui.py

EXPOSE 4729/udp

RUN ./pybombs install gr-gsm

#  ["airprobe_rtlsdr_nogui.py", "-p", "70", "-g", "50", "-f", "9.462e+08"]
