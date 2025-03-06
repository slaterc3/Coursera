import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'C:\\Users\\slate\\Coursera\\ibm\\dataEngineeringProfCert\\PythonProject\\top_50_films.csv'
df = pd.DataFrame(columns=['Average Rank','Film', 'Year'])
count = 0

html_page = requests.get(url).text # .text solved issue (BS expects string)
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
# print(tables)
rows = tables[0].find_all('tr')

# print(rows)
for idx, row in enumerate(rows):
    data_dict = {}
    if idx < 50:
        col = row.find_all('td')
        # print(col)
        if len(col) != 0: # if columns exist
            data_dict['Average Rank'] = col[0].contents[0]
            data_dict['Film'] = col[1].contents[0]
            data_dict['Year'] = col[2].contents[0]
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
    else:
        break 

df.to_csv(csv_path)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()