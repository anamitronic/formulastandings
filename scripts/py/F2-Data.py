

# Importing the required modules 
import os
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

InactiveMsg="<tbody>\n\t<td colspan='100' style='text-align:center'>The "+datetime.today().strftime('%Y')+" season is not currently in session</td>\n</tbody>"

path = "https://www.fiaformula2.com/Standings/Driver"
   
# empty list
data = []
   
# for getting the header from
# the HTML file
list_header = ["pos","name","points"]
soup = BeautifulSoup(requests.get(path).content,'html.parser')
 
# for getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    sub_element=element.find("div", {"class": "pos"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "driver-name"}).find("span", {"class": "visible-desktop-up"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "total-points"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    data.append(sub_data)
 
# Storing the data into Pandas
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)

path = "https://www.fiaformula2.com/Teams-and-Drivers"
   
# empty list
data = []
   
# for getting the header from
# the HTML file
list_header = ["name","team"]
soup = BeautifulSoup(requests.get(path).text,'html.parser')
 
# for getting the data 
HTML_data = soup.find_all("div", {"class": "wrapper"})

for element in HTML_data:
    team=element.find("div", {"class": "brand-link"})
    drivers=element.find("div", {"class": "drivers"})
    for driver in drivers:
        sub_data = []
        name=driver.find("div", {"class": "name"})
        sub_data.append(name.get_text().strip().replace('\r', ' ').replace('\n', ' '))
        sub_data.append(team.get_text().strip().replace('\r', ' ').replace('\n', ' '))
        data.append(sub_data)
 
# Storing the data into Pandas
# DataFrame 
teamdataFrame = pd.DataFrame(data = data, columns = list_header)

merged_df = dataFrame.merge(teamdataFrame, how = 'inner', on = ['name'])
merged_df.reset_index(drop=True, inplace=True)
dfTable = merged_df.iloc[:,[0,1,3,2]]
print(dfTable)
htmlTable = dfTable.to_html(index=False,header=False)
if dfTable.empty:
    htmlTable=InactiveMsg
jsData="var tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('f2-drivers').innerHTML+=tabledata;"


# TEAM STANDINGS

path = "https://www.fiaformula2.com/Standings/Team"
   
# empty list
data = []
   
# for getting the header from
# the HTML file
list_header = ["pos","name","points"] 
# for getting the data
soup = BeautifulSoup(requests.get(path).text,'html.parser') 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    sub_element=element.find("div", {"class": "pos"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "driver-name"}).find("span", {"class": "visible-desktop-up"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    sub_element=element.find("div", {"class": "total-points"})
    sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
    data.append(sub_data)
  
# Storing the data into Pandas
# DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,:]
print(dfTable)
htmlTable = dfTable.to_html(index=False,header=False)
if dfTable.empty:
    htmlTable=InactiveMsg
jsData+="\nvar tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('f2-constructors').innerHTML+=tabledata;"


f = open("./scripts/f2standingData.js", "w")
f.write(jsData)
f.close()
#close the connection to the database.
print("done")