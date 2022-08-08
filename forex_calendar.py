#The first step is importing all the required libraries for the task.
from calendar import calendar
import glob
import pandas as pd
from datetime import datetime

#First, file sources declaration(CSVs & JSONs).
calendar_csv = "https://nfs.faireconomy.media/ff_calendar_thisweek.csv?version=6cc2dd4a2e75ce89f7e4ddae2f92184e"
calendar_json = "https://nfs.faireconomy.media/ff_calendar_thisweek.json?version=6cc2dd4a2e75ce89f7e4ddae2f92184e"

#CSV file extraction function.
def extract_csvfile(filetoExtract):
    data_file = pd.read_csv(filetoExtract)
    return data_file
    
#JSON file extraction function.
def extract_jsonfile(filetoExtract):
    data_file = pd.read_json(filetoExtract)
    return data_file

#Extract function that will extract all the files in a sequence and append them
# to a dataframe after being read.

def extract_file():
    #creating a dataframe for the extracted data.
    extracted_data = pd.DataFrame(columns=["Title","Country","Date","Time","Impact","Forecast","Previous"])

    #Searching, extracting and appending CSV files onto the dataframe through
    # iterating through the directory.

    for csv in glob.glob('*.csv'):
        extracted_data = extracted_data.append(extract_csvfile(csv))

    


    

