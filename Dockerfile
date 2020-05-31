FROM python:3.7

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y librabbitmq-dev libmemcached-dev libxml2-dev libxmlsec1-dev libxmlsec1-openssl

RUN apt autoclean
RUN apt clean

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install gunicorn==19.9.0
RUN pip install watchdog==0.9.0

COPY README.md README.md

COPY viridi viridi
COPY main.py main.py
COPY setup.py setup.py

RUN python setup.py install

RUN pip install -r requirements.txt

CMD gunicorn -w 1 -b 0.0.0.0:5000 main:app --timeout=1200  --log-level=debug