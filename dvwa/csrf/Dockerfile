FROM ubuntu:16.04

ADD . /app/

RUN apt update && apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

EXPOSE 5000
CMD python3 /app/main.py 0.0.0.0:5000 &
