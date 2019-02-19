FROM    ubuntu:cosmic
RUN     apt-get update -y

RUN apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN export DEBIAN_FRONTEND=noninteractive

ENV DEBIAN_FRONTEND="noninteractive"
ENV XKBMODEL="pc105"
ENV XKBLAYOUT="us"
ENV XKBVARIANT=""
ENV XKBOPTIONS=""
ENV BACKSPACE="guess"
# Install vnc, xvfb in order to create a 'fake' display and firefox
#RUN     apt-get install -y x11vnc xvfb firefox
#RUN     mkdir ~/.vnc
# Setup a password

RUN apt install xfce4 xfce4-goodies firefox -y
RUN apt install tightvncserver python supervisor -y
RUN apt install x11vnc -y

#RUN     x11vnc -storepasswd 1234 ~/.vnc/passwd
RUN     bash -c 'echo "firefox" >> /.bashrc'
ENV HOME=/root \
    SHELL=/bin/bash
#USER root
ENV USER=root
RUN su - root
RUN mkdir ~/.vnc; chmod 777 ~/
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
#RUN useradd kopet
#USER kopet

#RUN apt update -y && apt install -y python supervisor openssh-client

WORKDIR /home
COPY ./ /home
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#USER 100
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
