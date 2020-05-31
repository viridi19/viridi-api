FROM python:alpine3.7
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY viridi ./viridi
EXPOSE 8080
ENTRYPOINT python -m viridi.app
