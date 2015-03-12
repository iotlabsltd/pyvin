import unittest

from pyvin import VINDecoder


class TestISO(unittest.TestCase):
    def test_valids(self):
        expects = {"SCCFE33C9VHF65358": {"Region": "Europe",
                                         "Country": "United Kingdom",
                                         "Manufacturer": "Lotus",
                                         "Model": "Unknown",
                                         "Check": True,  # valid
                                         "Year": 1997,
                                         "Assembly plant": "H",
                                         "Serial": "F65358"}}
        decoder = VINDecoder()
        for vin, e in expects.items():
            result = decoder.decode(vin)
            for k, v in result.items():
                self.assertEqual(v, e[k], msg=k)
