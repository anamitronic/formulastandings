# Importing the required modules 
import os
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
from sqlite3 import Error
from datetime import date

path = "https://www.formula1.com/en/results.html/"+date.today().strftime('%Y')+"/drivers.html"
   
# empty list
data = []
   
# for getting the header from
# the HTML file
list_header = []
soup = BeautifulSoup(requests.get(path).text,'html.parser')
header = soup.find_all("table")[0].find("tr")
  
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  
# for getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
        except:
            continue
    data.append(sub_data)
  
# Storing the data into Pandas
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.drop('',inplace=True,axis=1)
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,[0,1,3,4]]
htmlTable = dfTable.to_html(index=False,header=False)
jsData="var tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('drivers').innerHTML+=tabledata;"


# TEAM STANDINGS

path = "https://www.formula1.com/en/results.html/"+date.today().strftime('%Y')+"/team.html"
   
# empty list
data = []
   
# for getting the header from
# the HTML file
list_header = []
soup = BeautifulSoup(requests.get(path).text,'html.parser')
header = soup.find_all("table")[0].find("tr")
  
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  
# for getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
        except:
            continue
    data.append(sub_data)
  
# Storing the data into Pandas
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.drop('',inplace=True,axis=1)
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,:]
htmlTable = dfTable.to_html(index=False,header=False)
jsData+="\nvar tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('constructors').innerHTML+=tabledata;"


f = open("scripts/standingData.js", "w")
f.write(jsData)
f.close()
#close the connection to the database.
print("done")