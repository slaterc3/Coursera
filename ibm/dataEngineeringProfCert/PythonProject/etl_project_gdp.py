import requests
from bs4 import BeautifulSoup
import pandas as pd 
import sqlite3
import numpy as np 
from datetime import datetime

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

log_file = 'etl_project_log.txt'

database = 'World_Economies.db'

table_name = 'Countries_by_GDP'

csv_path = 'Countries_by_GDP.csv'

table_attribs = ['Country', 'GDP_USD_millions']

conn = sqlite3.connect(database)

# Code for ETL operations on Country-GDP data

# Importing the required libraries

def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    # soup = BeautifulSoup(url)
    
    df = pd.DataFrame(columns=table_attribs)
    
    r = requests.get(url).text 
    soup = BeautifulSoup(r, 'html.parser')
    tbodies = soup.find_all('tbody')
    if len(tbodies) < 3:
        raise Exception("not enough tabular elements")
    table = tbodies[2] # grabs the table in index #2
    
    rows = table.find_all(name='tr')
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        
        first_cell = cells[0]
        if not first_cell.find('a'):
            continue
        country = first_cell.get_text(strip=True)
        
        if len(cells) < 3:
            continue
        third_cell = cells[2].get_text(strip=True)
        if third_cell == '—':
            continue
        imf_estimate = third_cell
        # print(row)
        temp_df = pd.DataFrame({
            table_attribs[0]: [country],
            table_attribs[1]: [imf_estimate]
        })
        df = pd.concat([df, temp_df], ignore_index=True)


    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
    df['GDP_USD_millions']=df['GDP_USD_millions'].str.replace(',','').astype(float)
    df['GDP_USD_millions'] = (df['GDP_USD_millions']/1000).round(2)
    df.rename(columns={'GDP_USD_millions': 'GDP_USD_billions'}, inplace=True)
    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement,sql_connection)
    print(query_output)

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(f"{timestamp} : {message}\n")

''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''



log_progress('Initiating ETL processes')
log_progress('Extracting data...')
df3 = extract(url, table_attribs)
print(df3.head(3))
log_progress('Transforming data...')
df4 = transform(df3)
print(df4.head(2))
log_progress(f'loading data to csv: {csv_path}')
load_to_csv(df4, csv_path)
load_to_db(df4,conn,table_name)

query = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
log_progress(f'querying {table_name}:\n"{query}"')
run_query(query, conn)

log_progress("ETL processes completed")
