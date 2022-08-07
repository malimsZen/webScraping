import pandas as pd
import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://en.wikipedia.org/wiki/World_population" # Resource containing the data to be extracted.


data = requests.get(url).text # Downloading the html file from the internet and transforming it to text for easy parsing.

#Creating a beautiful soup object.
soup = BeautifulSoup(data,"html.parser")

tables = soup.find_all('table') #find all tables in the web page.
len(tables)

#Iterating through the tables to find the requested table; one containting a population above 10 mill.
for index,table in enumerate(tables):
    if("10 most densely populated countries" in str(table)): #checks fof the string in each table after string format conversion.
        table_index = table
print(table_index)


#Use of pandas function read_html and give it the string version of the table as well as flavor which is the parsing engine bs4.
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')





