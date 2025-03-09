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

# Code for ETL operations on Country-GDP data

# Importing the required libraries

def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    # soup = BeautifulSoup(url)
    r = requests.get(url).text 
    soup = BeautifulSoup(r, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    rows = soup.find_all(name='tr')
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        
        first_cell = cells[0]
        if not first_cell.find('a'):
            continue
        print(first_cell)
        if len(cells) >= 3:
            third_cell = cells[2].get_text(strip=True)
            if third_cell == '—':
                continue
        # print(row)


    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''
    pass

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''
    pass
def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    pass
def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
    pass 
''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''


# soup = BeautifulSoup(url)
# print(type(soup))
# x = [x for x in dir(soup) if 'table' in x]
# print(x)
r = requests.get(url).text 
soup = BeautifulSoup(r, 'html.parser')
df = pd.DataFrame(columns=table_attribs)
# rows = soup.find_all(name='tr')
tbodies = soup.find_all(name='tbody')
table = tbodies[2]
# print(table)
rows = table.find_all(name='tr')
for row in rows:
    print('**********************')
    print(row)

