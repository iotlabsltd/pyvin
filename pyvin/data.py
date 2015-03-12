import os

VIN_CHARS = "ABCDEFGHIJKLMNOPRSTUVWXYZ1234567890"

VIN_REGIONS = [("A", "H", "Africa"),
               ("J", "R", "Asia"),
               ("S", "Z", "Europe"),
               ("1", "5", "North America"),
               ("6", "7", "Oceania"),
               ("8", "9", "South America")]

VIN_COUNTRIES = [("AA", "AH", "South Africa"),
                 ("AJ", "AN", "Ivory Coast"),
                 ("BA", "BE", "Angola"),
                 ("BF", "BK", "Kenya"),
                 ("BL", "BR", "Tanzania"),
                 ("CA", "CE", "Benin"),
                 ("CF", "CK", "Madagascar"),
                 ("CL", "CR", "Tunisia"),
                 ("DA", "DE", "Egypt"),
                 ("DF", "DK", "Morocco"),
                 ("DL", "DR", "Zambia"),
                 ("EA", "EE", "Ethiopia"),
                 ("EF", "EK", "Mozambique"),
                 ("FA", "FE", "Ghana"),
                 ("FF", "FK", "Nigeria"),
                 ("JA", "J0", "Japan"),
                 ("KA", "KE", "Sri Lanka"),
                 ("KF", "KK", "Israel"),
                 ("KL", "KR", "Korea (South)"),
                 ("KS", "K0", "Kazakhstan"),
                 ("LA", "L0", "China"),
                 ("MA", "ME", "India"),
                 ("MF", "MK", "Indonesia"),
                 ("ML", "MR", "Thailand"),
                 ("NA", "NE", "Iran"),
                 ("NF", "NK", "Pakistan"),
                 ("NL", "NR", "Turkey"),
                 ("PA", "PE", "Philippines"),
                 ("PF", "PK", "Singapore"),
                 ("PL", "PR", "Malaysia"),
                 ("RA", "RE", "United Arab Emirates"),
                 ("RF", "RK", "Taiwan"),
                 ("RL", "RR", "Vietnam"),
                 ("RS", "R0", "Saudi Arabia"),
                 ("SA", "SM", "United Kingdom"),
                 ("SN", "ST", "Germany"),
                 ("SU", "SZ", "Poland"),
                 ("S1", "S4", "Latvia"),
                 ("TA", "TH", "Switzerland"),
                 ("TJ", "TP", "Czech Republic"),
                 ("TR", "TV", "Hungary"),
                 ("TW", "T1", "Portugal"),
                 ("UH", "UM", "Denmark"),
                 ("UN", "UT", "Ireland"),
                 ("UU", "UZ", "Romania"),
                 ("U5", "U7", "Slovakia"),
                 ("VA", "VE", "Austria"),
                 ("VF", "VR", "France"),
                 ("VS", "VW", "Spain"),
                 ("VX", "V2", "Serbia"),
                 ("V3", "V5", "Croatia"),
                 ("V6", "V0", "Estonia"),
                 ("WA", "W0", "Germany"),
                 ("XA", "XE", "Bulgaria"),
                 ("XF", "XK", "Greece"),
                 ("XL", "XR", "Netherlands"),
                 ("XS", "XW", "Russia"),
                 ("XX", "X2", "Luxembourg"),
                 ("X3", "X0", "Russia"),
                 ("YA", "YE", "Belgium"),
                 ("YF", "YK", "Finland"),
                 ("YL", "YR", "Malta"),
                 ("YS", "YW", "Sweden"),
                 ("YX", "Y2", "Norway"),
                 ("Y3", "Y5", "Belarus"),
                 ("Y6", "Y0", "Ukraine"),
                 ("ZA", "ZR", "Italy"),
                 ("ZX", "Z2", "Slovenia"),
                 ("Z3", "Z5", "Lithuania"),
                 ("1A", "10", "United States"),
                 ("2A", "20", "Canada"),
                 ("3A", "37", "Mexico"),
                 ("38", "30", "Cayman Islands"),
                 ("4A", "40", "United States"),
                 ("5A", "50", "United States"),
                 ("6A", "6W", "Australia"),
                 ("7A", "7E", "New Zealand"),
                 ("8A", "8E", "Argentina"),
                 ("8F", "8K", "Chile"),
                 ("8L", "8R", "Ecuador"),
                 ("8S", "8W", "Peru"),
                 ("8X", "82", "Venezuela"),
                 ("9A", "9E", "Brazil"),
                 ("9F", "9K", "Colombia"),
                 ("9L", "9R", "Paraguay"),
                 ("9S", "9W", "Uruguay"),
                 ("9X", "92", "Trinidad & Tobago"),
                 ("93", "99", "Brazil")]

YEARS = {
    "A": 1980,
    "B": 1981,
    "C": 1982,
    "D": 1983,
    "E": 1984,
    "F": 1985,
    "G": 1986,
    "H": 1987,
    "J": 1988,
    "K": 1989,
    "L": 1990,
    "M": 1991,
    "N": 1992,
    "P": 1993,
    "R": 1994,
    "S": 1995,
    "T": 1996,
    "V": 1997,
    "W": 1998,
    "X": 1999,
    "Y": 2000,
    "1": 2001,
    "2": 2002,
    "3": 2003,
    "4": 2004,
    "5": 2005,
    "6": 2006,
    "7": 2007,
    "8": 2008,
    "9": 2009,
}

def get_region(r):
    qi = VIN_CHARS.index(r)
    for region in VIN_REGIONS:
        i = VIN_CHARS.index(region[0])
        j = VIN_CHARS.index(region[1])
        if qi >= i and qi <= j:
            return region[2]
    return "Unknown"


def get_index(s):
    return VIN_CHARS.index(s[0])*len(VIN_CHARS)+VIN_CHARS.index(s[1])


def get_country(c):
    qi = get_index(c)
    for country in VIN_COUNTRIES:
        i = get_index(country[0])
        j = get_index(country[1])
        if qi >= i and qi <= j:
            return country[2]
    return "Not assigned"


def get_year(c):
    if len(c) == 1:
        return YEARS[c]
    elif len(c) == 2:
        if c[0].isdigit():
            return YEARS[c[1]]
        else:
            return YEARS[c[1]]+20
    return 1979


class WMIDatabase(object):
    def __init__(self, name):
        path = os.path.join(os.path.dirname(
                            os.path.dirname(
                                os.path.abspath(__file__))),
                            "data", name)
        print path, os.path.abspath(__file__)
        self.db = {}
        with open(path, "r") as f:
            for line in f:
                wmi, name = line.strip().split(",", 1)
                self.db[wmi] = name.strip()

    def get(self, wmi):
        return self.db[wmi]
