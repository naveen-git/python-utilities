import urllib.parse as urlparse
from urllib.parse import urlencode

def formURL(vin_number):
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/?format=xml"
    url_parts = list(urlparse.urlparse(url))
    url_parts[2] = url_parts[2] + vin_number
    url = urlparse.urlunparse(url_parts)
    return url
