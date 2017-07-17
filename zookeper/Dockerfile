FROM python:2.7
RUN apt-get update
RUN apt-get install -y dnsutils 
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
