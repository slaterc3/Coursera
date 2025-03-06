"""Try the following practice problems to test your understanding of the lab. Please note that the solutions for the following are not shared. You are encouraged to use the discussion forums in case you need help.

Modify the code to extract Film, Year, and Rotten Tomatoes' Top 100 headers.

Restrict the results to only the top 25 entries.

Filter the output to print only the films released in the 2000s (year 2000 included)."""

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

db_name = 'Movies_RT25.db'
table_name = 'Top_25'
csv_path = 'C:\\Users\\slate\\Coursera\\ibm\\dataEngineeringProfCert\\PythonProject\\top_25_films_from_RT.csv'

# Create an empty DataFrame with desired columns
df = pd.DataFrame(columns=['Film', 'Year', 'Rotten Tomatoes Top 100'])
count = 0

# Fetch and parse the HTML content
html_page = requests.get(url).text
soup = BeautifulSoup(html_page, 'html.parser')

tables = soup.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    # Stop once we have collected 25 entries
    if count >= 25:
        break

    col = row.find_all('td')
    if len(col) == 0:
        # Skip header or empty rows instead of breaking the loop
        continue

    # Extract values using .get_text(strip=True) for robustness
    film = col[1].get_text(strip=True)
    year_text = col[2].get_text(strip=True)
    rt_top100 = col[3].get_text(strip=True)

    try:
        year = int(year_text)
    except ValueError:
        # If the year can't be converted to an integer, skip this row
        continue

    # Filter: Only include films released in 2000 or later
    if year < 2000:
        continue

    # Create a dictionary for the current row and append it to the DataFrame
    data_dict = {
        'Film': film,
        'Year': year,
        'Rotten Tomatoes Top 100': rt_top100
    }
    df = pd.concat([df, pd.DataFrame(data_dict, index=[0])], ignore_index=True)
    count += 1

# Save DataFrame to CSV
df.to_csv(csv_path, index=False)

# Write DataFrame to SQLite database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

print(df)