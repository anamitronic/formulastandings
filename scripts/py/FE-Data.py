# Importing the required modules 
import os
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

# Message if table was empty or doesn't exist
InactiveMsg="<tbody>\n\t<td colspan='100' style='text-align:center'>The "+date.today().strftime('%Y')+" season is not currently in session</td>\n</tbody>"

# DRIVER STANDINGS
# Path to extract from
path = "https://www.fiaformulae.com/en/results/standings/driver"
   
# empty list to store table data
data = []
   
# Getting the header from the HTML file
list_header = ["pos","name","team","points"]
soup = BeautifulSoup(requests.get(path).content,'html.parser')
  
# Getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr",{"class": "table__row"})

for element in HTML_data:
    sub_data = []
    sub_element=element.find("div", {"class": "pos"}).find("span", {"class": "value"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "driver"}).img['alt']
    sub_data.append(sub_element.strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "team"}).find("span", {"class": "team__name"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "points"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    data.append(sub_data)
  
# Storing the data into Pandas DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
# Removing excess data
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,:]
# Printing output
print(dfTable)
# Converting to html
htmlTable = dfTable.to_html(index=False,header=False)
# Checking if table is empty
if dfTable.empty:
    htmlTable=InactiveMsg
# Converting table to js syntax
jsData="var tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('fe-drivers').innerHTML+=tabledata;"


# TEAM STANDINGS
# Path to extract from
path = "https://www.fiaformulae.com/en/results/standings/team"
   
# empty list to store table data
data = []
   
# Getting the header from the HTML file
list_header = ["pos","team","points"]
soup = BeautifulSoup(requests.get(path).content,'html.parser')
  
# Getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr",{"class": "table__row"})

for element in HTML_data:
    sub_data = []
    sub_element=element.find("div", {"class": "pos"}).find("span", {"class": "value"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "team"}).find("span", {"class": "team__name"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "points"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    data.append(sub_data)

  
# Storing the data into Pandas DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
# Removing excess data
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,:]
# Printing output
print(dfTable)
# Converting to html
htmlTable = dfTable.to_html(index=False,header=False)
# Checking if table is empty
if dfTable.empty:
    htmlTable=InactiveMsg
# Converting table to js syntax
jsData+="\nvar tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('fe-constructors').innerHTML+=tabledata;"

# writing js code to js file
f = open("./scripts/festandingData.js", "w")
f.write(jsData)
f.close()
# close the connection
print("done")