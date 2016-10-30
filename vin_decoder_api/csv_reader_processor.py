import csv
from connect_api import formURL
from response_xml_processor import getResponse

f = open('sample_file.csv')
csv_f = csv.reader(f)
for row in csv_f:
    print("Processing for VIN:",row[0])    
    url = formURL(row[0])
    getResponse(url)
print("Successful")
