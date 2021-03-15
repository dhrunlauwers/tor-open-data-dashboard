import requests
from bs4 import BeautifulSoup
import pandas as pd


wiki_url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

website_content = requests.get(wiki_url).text
soup = BeautifulSoup(website_content, 'lxml')
table = soup.find('table', {'class':'wikitable sortable'})
postal_mapping = pd.DataFrame()

for row in table.find_all('tr'):
    row_dict = {}
    data = row.find_all('td')
    if len(data) > 0:
        row_dict['POSTAL'] = data[0].text.strip()
        row_dict['Borough'] = data[1].text.strip()
        row_dict['Neighbourhood'] = data[2].text.strip()
        postal_mapping = postal_mapping.append(row_dict, ignore_index=True)

postal_mapping.to_csv('../data/processed/postal_code_mapping.csv', header=True, index=False)