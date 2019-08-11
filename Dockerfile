FROM golang:1.12.7-buster

WORKDIR /app
COPY . /app

RUN \
  apt-get update && \
  apt-get install -y python-pip && \
  pip install --trusted-host pypi.python.org -r requirements.txt

RUN GOPATH=$(pwd) go get github.com/bemasher/rtlamr

ENV filterid ""
ENV server "127.0.0.1:1234"

ENTRYPOINT ["./entrypoint.sh"]

