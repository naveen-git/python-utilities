import requests
from xml.etree import ElementTree
from urllib.request import urlopen
import csv

def getResponse(url):
    responseXML = requests.get(url, stream=True)
    responseXML.raw.decode_content = True
    events = ElementTree.iterparse(responseXML.raw)
    list_of_rows = []
    for event, elem in events:
        list_vin_details = []
        if elem.tag == "DecodedVINValues":
            if elem.findtext("ErrorCode") == "0 - VIN decoded clean. Check Digit (9th position) is correct":
                list_vin_details.append(elem.findtext("VIN"))
                list_vin_details.append(elem.findtext("Make"))
                list_vin_details.append(elem.findtext("Model"))
                list_vin_details.append(elem.findtext("ModelYear"))
                list_of_rows.append(list_vin_details)
    outfile = open("./vin_details.csv", "a", newline='')
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)
