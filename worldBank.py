import pandas as pd
import wbgapi as wb

#wb.data.DataFrame('SP.POP.TOTL', time=2015, labels=True).reset_index()
# The aim of this module is to extract world pupulation data from each individual nation and store it in  a
# dataframe before loading it to a storage system.


def extract_population():
    # I'll use a new dataframe to append the extracted API data.
    wpdf = pd.DataFrame(columns=['economy','Country','Population']) 

    #extracting data
    wp = wb.data.DataFrame('SP.POP.TOTL', time=2021, labels=True).reset_index() 

    #appending the extracted data to the newly created dataframe. 
    for data in wp:
        wpdf = wpdf.append(data)


    print(wpdf)
    return wp

#Transform the population column(SP.POP.TOTL) 
def transform_population(wpdf):
    wpdf['Population'] = round(wpdf.Population,2)

    print(wpdf)
    return wpdf

e_population = extract_population() # running the extract function.

t_populaton = transform_population(e_population)    #transfofm function.``
t_populaton




