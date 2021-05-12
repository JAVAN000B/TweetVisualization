FROM python:3
MAINTAINER "simon<simon@simon.simon>"
WORKDIR /projects

ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au


COPY app.py app.py
COPY couchdbUtils.py couchdbUtils.py
COPY couchdbView.py couchdbView.py
COPY requirements.txt requirements.txt
COPY gun.conf gun.conf

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn  -c gun.conf app:app