import requests
import urllib.parse as urlparse

def formSafetyURL(vehicleId):
    url = "https://api.nhtsa.gov/vehicles/7295/details?data=safetyRatings"
    url_parts = list(urlparse.urlparse(url))
    splitText = url_parts[2].split("/")
    splitText[2] = str(vehicleId)
    url_parts[2] = "/".join(splitText)
    url = urlparse.urlunparse(url_parts)
    resp = requests.get(url)
    data = resp.json()
    dict = { "key":"value" }
    for i in range(len(data["results"][0]["safetyRatings"]["recommendedFeatures"])):
        dictValue = data["results"][0]["safetyRatings"]["recommendedFeatures"][i]
        dict[dictValue["label"]] = dictValue["type"]
    del dict["key"]
    print("got safety data")
    return dict
