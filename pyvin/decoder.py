from .data import WMIDatabase, get_region, get_country, get_year


class InvalidVINException(Exception):
    pass


class VINDecoder(object):
    def __init__(self):
        self.wmi_db = WMIDatabase("wmi_vinquery.csv")

    def parse_wmi(self, vin):
        region_code = vin[0]
        country_code = vin[0:2]
        wmi = vin[0:3]
        region = get_region(region_code)
        country = get_country(country_code)
        manufacturer = self.wmi_db.get(wmi)
        return region, country, manufacturer

    def parse_vds(self, vin, region, manufacturer):
        vds = vin[3:8]
        check = True
        return "Unknown", check

    def parse_vis(self, vin, region, manufacturer):
        vis = vin[9:]
        # XXX determine make and based on that get 1 or 2 character year code
        # from position 7 and 10 accordingly
        year_code = vis[0]
        year = get_year(year_code)
        plant = vis[1]
        serial = vis[2:]
        return year, plant, serial

    def decode(self, vin):
        if len(vin) != 17:
            raise InvalidVINException()
        region, country, manufacturer = self.parse_wmi(vin)
        model, check = self.parse_vds(vin, region, manufacturer)
        year, plant, serial = self.parse_vis(vin, region, manufacturer)
        return {"region": region,
                "country": country,
                "manufacturer": manufacturer,
                "model": model,
                "check": check,
                "year": year,
                "assembly plant": plant,
                "serial": serial}
