from bs4 import BeautifulSoup
import requests


with open("tradingview.html",'r+') as fp:
    soup = BeautifulSoup(fp,features="lxml")

    file_Title = soup.title

    file_Body = soup.body
    print(file_Body['class'])

    table_rows = soup.find_all('tr')

    first_row = table_rows[0]
    print(first_row.td)
    print(soup.find_all(string="US"))

    

    

    

