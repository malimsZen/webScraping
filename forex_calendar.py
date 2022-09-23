#The first step is importing all the required libraries for the task.
import glob
import pandas as pd
from datetime import datetime
import requests

target_file = "Transformed_data.csv" #Transformed file repo.
load_file = "load_file.txt" #Load file repo

#CSV file extraction function.
def extract_json(filetoExtract):
    data_file = pd.read_json(filetoExtract)
    print(data_file)
    return data_file
    



#Extract function that will extract all the files in a sequence and append them
# to a dataframe after being read.
def extract_file():
    #creating a dataframe for the extracted data.
    extracted_data = pd.DataFrame(columns=["Title","Country","Date","Impact","Forecast","Previous"])

    #Searching, extracting and appending both XLS files onto the dataframe through
    # iterating through the directory.
    for json_file in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_json(json_file))


    return extracted_data



# Transform the totoal_assets_us_b column data into two deciman formats.
def transform_file(data):

    data.loc[2, 'Forecast'] = 45.0
    print(data)

    return data



# Load function,loads the transformed data into a csv file.
def load_file(targetfile,data_to_load):
    data_to_load.to_csv(target_file)



#logging the ETL process.
def log(message):
    timestamp_format = ' %H:%M:%S-%h-%d-%Y' #Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now() #get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("load_file.txt",'a') as f:
        f.write(timestamp + ',' + message + '\n')



#Running the ETL Process
log("ETL Job Started")
log('Extraction phase Started')
extracted_data_file = extract_file()
extracted_data_file
log('Extraction phase ended')


log('Transform phase Started')
transformed_file = transform_file(extracted_data_file)
transformed_file
log('Transform phase ended')


log('Load phase started')
file_load = load_file(target_file,transformed_file)
file_load
log('Load phase ended.')


log('ETL Job Ended.')






    

