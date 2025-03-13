import requests
from bs4 import BeautifulSoup
import pandas as pd 
import sqlite3
import numpy as np 
from datetime import datetime

csv_path = """https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"""

data_url = """https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"""

table_attrib = ["Name", "MC_USD_Billion"]

final_table_attrib = ['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']

output_path = './Largest_banks_data.csv'

db_name = 'Banks.db'

table_name = 'Largest_banks'

log_file = 'code_log.txt'

conn = sqlite3.connect(db_name)

def log_progress(log_point):
    timestamp_fmt = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_fmt)
    with open(log_file, 'a') as f:
        f.write(f"{timestamp}: {log_point}")

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    # return df
    df = pd.DataFrame(columns=table_attribs)
    
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    
    
    
    
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''



"""Declaring known values	Preliminaries complete. Initiating ETL process
Call extract() function	Data extraction complete. Initiating Transformation process
Call transform() function	Data transformation complete. Initiating Loading process
Call load_to_csv()	Data saved to CSV file
Initiate SQLite3 connection	SQL Connection initiated
Call load_to_db()	Data loaded to Database as a table, Executing queries
Call run_query()	Process Complete
Close SQLite3 connection	Server Connection closed"""

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"

r = requests.get(url).text 

soup = BeautifulSoup(r, 'html.parser')

tbodies = soup.find_all('tbody')
# print((tbodies[0]))
table = tbodies[0]
print(table)