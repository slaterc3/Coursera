import requests
from bs4 import BeautifulSoup
import pandas as pd 
import sqlite3
import numpy as np 
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

csv_path = """https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"""

data_url = """https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"""

table_attribs = ["Name", "MC_USD_Billion"]

final_table_attrib = ['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']

output_path = './Largest_banks_data.csv'

db_name = 'Banks.db'

table_name = 'Largest_banks'

log_file = 'code_log.txt'


def log_progress(log_point):
    timestamp_fmt = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_fmt)
    with open(log_file, 'a') as f:
        f.write(f"\n{timestamp}: {log_point}\n")

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    df = pd.DataFrame(columns=table_attribs)
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find_all('tbody')[0]
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if not cells or len(cells) < 3:
            continue
        bank_name = cells[1].get_text(strip=True)
        # print('*******************')
        # print(cells[1].find_all('a')[1]['title'])
        market_cap = float(cells[2].get_text(strip=True))
        temp_df = pd.DataFrame({
            table_attribs[0]: bank_name, # bank name
            table_attribs[1]: market_cap # $ amt
        }, index=[0])
        df = pd.concat([df, temp_df], ignore_index=True)
    return df 

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    exchange_rate_df = pd.read_csv(csv_path)
    exchange_rate = dict(zip(exchange_rate_df['Currency'], exchange_rate_df['Rate']))
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    return df


def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace',index=False)

def run_query(query_statement, sql_connection):
    """''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''"""
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


if __name__ == '__main__':
    log_progress("Preliminaries complete. Initiating ETL process")
    df = extract(data_url, table_attribs)
    log_progress('Data extraction complete. Initiating Transformation process')
    # print(df)
    csv_path = 'exchange_rate.csv'
    df2 = transform(df, csv_path)
    log_progress("Data transformation complete. Initiating Loading process")
    # print(df)
    print('Market cap for 5th largest bank in Europe:')
    print(df['MC_EUR_Billion'][4])
    load_to_csv(df2, output_path)
    log_progress('Data saved to CSV file')
    conn = sqlite3.connect(db_name)
    log_progress('SQL Connection initiated')
    load_to_db(df2, conn, table_name)
    log_progress('Data loaded to Database as a table, Executing queries')
    # log_progress('')
    sql_stmt1 = 'SELECT * FROM Largest_banks'
    sql_stmt2 = 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
    sql_stmt3 = 'SELECT Name from Largest_banks LIMIT 5'
    run_query(sql_stmt1, conn)
    run_query(sql_stmt2, conn)
    run_query(sql_stmt3, conn)
    log_progress('Process Complete')
    conn.close()
    log_progress('Server Connection Closed')