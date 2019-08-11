#!/bin/sh

bin/rtlamr -msgtype=r900 -format=json -filterid=${filterid} -server=${server} | python neptune2influx.py $@
