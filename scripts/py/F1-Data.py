# Importing the required modules 
import os
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Message if table was empty or doesn't exist

# Function if table data unavailable
def InactiveSession():
    InactiveMsg="<tbody>\n\t<td colspan='100' style='text-align:center'>The "+datetime.today().strftime('%Y')+" season is not currently in session</td>\n</tbody>"
    DriverJsData="var tabledata=`"+InactiveMsg+"\n`;\ndocument.getElementById('f1-drivers').innerHTML+=tabledata;"
    ConstructorJsData="\nvar tabledata=`"+InactiveMsg+"\n`;\ndocument.getElementById('f1-constructors').innerHTML+=tabledata;"
    jsData=DriverJsData+ConstructorJsData
    # add last updated
    curDateTime=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    jsData+="\ndocument.getElementById('lastup').innerHTML='"+curDateTime+" UTC';"

    # writing js code to js file
    f = open("./scripts/f1standingData.js", "w")
    f.write(jsData)
    f.close()
    # close the connection
    print("F1 Script Complete - Inactive Session")
    sys.exit()
# DRIVER STANDINGS
# Path to extract from
path = "https://www.formula1.com/en/results.html/"+datetime.today().strftime('%Y')+"/drivers.html"
   
# empty list to store table data
data = []
   
# Getting the header from the HTML file
list_header = []
soup = BeautifulSoup(requests.get(path).content,'html.parser')
try:
    header = soup.find_all("table")[0].find("tr")
except IndexError:
    InactiveSession()

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  
# Getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
        except:
            continue
    data.append(sub_data)
  
# Storing the data into Pandas DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
# Removing excess data
dataFrame.drop('',inplace=True,axis=1)
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,[0,1,3,4]]
# Printing output
print(dfTable)
# Converting to html
htmlTable = dfTable.to_html(index=False,header=False)
# Checking if table is empty
if dfTable.empty:
    InactiveSession()
# Converting table to js syntax
DriverJsData="var tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('f1-drivers').innerHTML+=tabledata;"


# TEAM STANDINGS
# Path to extract from
path = "https://www.formula1.com/en/results.html/"+datetime.today().strftime('%Y')+"/team.html"
   
# empty list to store table data
data = []
   
# Getting the header from the HTML file
list_header = []
soup = BeautifulSoup(requests.get(path).content,'html.parser')
header = soup.find_all("table")[0].find("tr")
  
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  
# Getting the data 
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text().strip().replace('\r', ' ').replace('\n', ' '))
        except:
            continue
    data.append(sub_data)
  
# Storing the data into Pandas DataFrame 
dataFrame = pd.DataFrame(data = data, columns = list_header)
# Removing excess data
dataFrame.drop('',inplace=True,axis=1)
dataFrame.reset_index(drop=True, inplace=True)
dfTable = dataFrame.iloc[:,:]
# Printing output
print(dfTable)
# Converting to html
htmlTable = dfTable.to_html(index=False,header=False)
# Checking if table is empty
if dfTable.empty:
    InactiveSession()
# Converting table to js syntax
ConstructorJsData="\nvar tabledata=`"+htmlTable+"\n`;\ndocument.getElementById('f1-constructors').innerHTML+=tabledata;"
jsData=DriverJsData+ConstructorJsData
# add last updated
curDateTime=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
jsData+="\ndocument.getElementById('lastup').innerHTML='"+curDateTime+" UTC';"

# writing js code to js file
f = open("./scripts/f1standingData.js", "w")
f.write(jsData)
f.close()
# close the connection
print("F1 Script Complete")
