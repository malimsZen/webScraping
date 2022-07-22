import json
import requests
import glob
import pandas as pd
from datetime import datetime

def extract_csvfile(filetoExtract):
    data_file = pd.read_csv(filetoExtract)
    print(data_file)
    return data_file
    

extract = extract_csvfile("ff_calendar_thisweek.csv")

extract.head()
    

