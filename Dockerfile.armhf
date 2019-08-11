FROM alpine:latest

RUN \
 apk add curl && \
 curl -L https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz | tar --strip=1 -zxvf -

FROM arm32v7/golang:1.12.7-buster

COPY --from=0 /qemu-arm-static /usr/bin

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

