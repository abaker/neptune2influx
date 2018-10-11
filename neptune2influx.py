import argparse
import json
import logging
import sys

from influxdb import InfluxDBClient


def parse(line):
    j = json.loads(line)
    message = j['Message']
    return [
        {
            "measurement": "reading",
            "time": j['Time'],
            "tags": {
                "id": message['ID']
            },
            "fields": {
                "consumption": message['Consumption'] / 10.0,
                "backflow": message['BackFlow'],
                "nouse": message['NoUse'],
                "unkn1": message['Unkn1'],
                "unkn3": message['Unkn3'],
                "leak": message['Leak'],
                "leaknow": message['LeakNow']
            }
        }
    ]


def main(db):
    for line in iter(sys.stdin.readline, b''):
        logging.debug(line)
        measurement = parse(line)
        logging.debug(measurement)
        db.write_points(measurement)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true', help="enable debug logging", required=False)
    parser.add_argument("--host", help="influx host", required=False, default='localhost')
    parser.add_argument("--port", help="influx port", required=False, default=8086)
    parser.add_argument("--username", help="influx username", required=False, default='root')
    parser.add_argument("--password", help="influx password", required=False, default='root')
    parser.add_argument("--db", help="influx database name", required=False, default='neptune')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    logging.basicConfig(level=('DEBUG' if args.debug else 'WARN'),
                        format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    influx = InfluxDBClient(database=args.db, host=args.host, port=args.port, username=args.username,
                            password=args.password)
    influx.create_database(args.db)
    main(db=influx)
