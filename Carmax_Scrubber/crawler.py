import requests
import re
import csv
import fileinput
from BeautifulSoup import BeautifulSoup

url = 'https://www.carmax.com/stores/states/'
response = requests.get(url)
html = response.content
list_of_rows = []
soup = BeautifulSoup(html)
typo = soup.find('ul',attrs={"class":"stores-states--list"}).findAll('a')
for getin in typo:
    hrefval = getin.get('href')
    statename = hrefval.split("/")[3]
    urlstate = 'https://www.carmax.com'+hrefval
    responsestate = requests.get(urlstate)
    htmlstate = responsestate.content
    list_of_store_data = []
    soupstate = BeautifulSoup(htmlstate)
    typostate = soupstate.findAll('a', attrs={"class":"btn"})
    for getinstate in typostate:
        hrefvalstate = getinstate.get('href')
        storenumber = hrefvalstate.split("/")[2]
        urlstatestore = 'https://www.carmax.com'+hrefvalstate
        responsestatestore = requests.get(urlstatestore)
        htmlstatestore = responsestatestore.content
        soupstatestore = BeautifulSoup(htmlstatestore)
        storename = soupstatestore.find('h1', attrs={"class":"store-details--store-name"}).text
        storename = storename.split("-")[0]
        print (statename)
        storeaddress = soupstatestore.find('div', attrs={"class":"store-details--address"}).text
        addressLine = storeaddress.split(",")[0]
        temp = storeaddress.split(",")[1]
        stateCode = temp.split(" ")[1]
        zipCode = temp.split(" ")[2]
        list_of_store_data.append(storenumber)
        list_of_store_data.append(statename)
        list_of_store_data.append(storename)
        list_of_store_data.append(addressLine)
        list_of_store_data.append(stateCode)
        list_of_store_data.append(zipCode)
    list_of_rows.append(list_of_store_data)
outfile = open("./carmax_details.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
print ("Successful")
