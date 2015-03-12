import unittest

from pyvin.data import WMIDatabase, get_country, get_region


class TestData(unittest.TestCase):
    def test_region(self):
        expects = {"S": "Europe"}

        for k, v in expects.items():
            e = get_region(k)
            self.assertEqual(v, e)

    def test_country(self):
        expects = {"SC": "United Kingdom"}

        for k, v in expects.items():
            e = get_country(k)
            self.assertEqual(v, e)

    def test_wmidb(self):
        wmi_db = WMIDatabase("wmi_vinquery.csv")
        expects = {"SCC": "Lotus"}

        for k, v in expects.items():
            e = wmi_db.get(k)
            self.assertEqual(v, e)
