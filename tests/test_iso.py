import unittest

from pyvin import VINDecoder


class TestISO(unittest.TestCase):
    def test_valids(self):
        expects = {"SCCFE33C9VHF65358": {"region": "Europe",
                                         "country": "United Kingdom",
                                         "manufacturer": "Lotus",
                                         "model": "Unknown",
                                         "check": True,  # valid
                                         "year": 1997,
                                         "assembly plant": "H",
                                         "serial": "F65358"}}
        decoder = VINDecoder()
        for vin, e in expects.items():
            result = decoder.decode(vin)
            for k, v in result.items():
                self.assertEqual(v, e[k], msg=k)
