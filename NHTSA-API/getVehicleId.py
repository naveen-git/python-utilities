import requests
from furl import furl

def formURL(year, make, model):
    url = "https://api.nhtsa.gov/vehicles/bySearch?dateStart=2005-01-01&dateEnd=3000-01-01&max=100"
    final_url = furl(url).add({"query": str(year)+" "+make+" "+model}).url
    resp = requests.get(final_url)
    data = resp.json()
    countValue = data["meta"]["filters"]
    counter = 0;
    for i in range(len(countValue)):
       counter = data["meta"]["filters"][i]["count"]
       if counter > 0:
           break
       else:
           continue
    if counter > 0:
        return data["results"][0]["vehicleId"]
    else:
        return 0

