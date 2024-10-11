FROM ubuntu

RUN apt-get update
RUN apt install python3-pip python3-venv
RUN python3 -m venv venv
RUN . ./venv/bin/activate
RUN  pip install django
RUN  pip install pillow
RUN  pip install -r requirements.txt





