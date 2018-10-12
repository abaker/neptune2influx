`neptune2influx` uses a software defined radio ([Amazon.com](https://www.amazon.com/s/?field-keywords=rtl-sdr)) and [rtlamr](https://github.com/bemasher/rtlamr) to insert Neptune R900 water meter readings into InfluxDB

Your SDR must be connected to your PC

### Prerequisites

* macOS with [Homebrew](https://brew.sh):
```
$ brew install python2 rtl-sdr go influxdb
$ brew services start influxdb
```
* Debian/Ubuntu:
```
$ sudo apt install python-pip rtl-sdr golang influxdb
```

### Setup
```
$ git clone https://github.com/abaker/neptune2influx
$ cd neptune2influx
$ pip install -r requirements.txt
$ GOPATH=$(pwd) go get github.com/bemasher/rtlamr
```

### Run
Start an `rtl_tcp` server
```
$ rtl_tcp &
```
Then start recording data
```
$ bin/rtlamr -msgtype=r900 -format=json -filterid=<your_meter_id> | python neptune2influx.py
```

By default `neptune2influx` will connect to a local InfluxDB install, use the default credentials, and store data in a table named `neptune`

```
usage: neptune2influx.py [-h] [--debug] [--host HOST] [--port PORT]
                         [--username USERNAME] [--password PASSWORD] [--db DB]

optional arguments:
  -h, --help           show this help message and exit
  --debug              enable debug logging
  --host HOST          influx host
  --port PORT          influx port
  --username USERNAME  influx username
  --password PASSWORD  influx password
  --db DB              influx database name
```