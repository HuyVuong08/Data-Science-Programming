import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl

base_url = 'http://quotes.toscrape.com'
url = base_url

data = []

# Function to get the date of birth and place of birth in the subpage
def get_author(url):
    soup = BeautifulSoup(requests.get(url).text)
    author = {
        'date_of_birth': soup.find(class_='author-born-date').text,       
        'place_of_birth': soup.find(class_='author-born-location').text,
        'url': url
    }
    return author

# Repeats until not seeing the next page button
while True:
    try:
        response = requests.get(url).text 
    except requests.exceptions.HTTPError as err:
        print(f'An HTTP error occurred: {err}')

    try:
        soup = BeautifulSoup(response, 'html.parser')
    except bs4.FeatureNotFound as err:
        print(f'An error occurred while parsing the HTML: {err}')

    for e in soup.select('div.quote'):
        # Save basic information of authors
        qoute = {
            'author':e.find('small', class_='author').text,
            'qoute':e.find('span', class_='text').text
        }
        qoute.update(get_author(base_url+e.a.get('href')))
        data.append(qoute)

    if soup.select_one('li.next a'):
        # Get URL to the next page
        url=base_url+soup.select_one('li.next a').get('href')
    else:
        break
    
# Convert python dictionary to Pandas dataframe
df = pd.DataFrame(data)

# Save Pandas dataframe to .csv and .xlsx file
df.to_csv('../data/processed/data.cv')
df.to_excel('../data/processed/data.xlsx')