import unittest
import neptune2influx

class Emu2InfluxTest(unittest.TestCase):
    def test_consumption(self):
        reading = '{"Time":"2018-10-11T17:10:45.999515724Z","Offset":0,"Length":0,"Message":{"ID":1548280054,"Unkn1":163,"NoUse":32,"BackFlow":0,"Consumption":377933,"Unkn3":0,"Leak":0,"LeakNow":0}}'
        measurement = neptune2influx.parse(reading)
        self.assertEqual(37793.3, measurement[0]['fields']['consumption'])
