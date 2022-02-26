from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from urllib.error import HTTPError
from json.decoder import JSONDecodeError

# setting header and proxy
HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

s = requests.Session()
s.proxies = {"http": "http://61.233.25.166:80"}

# Reading URLs from the given cvs file
url = []
test = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   '1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM' +
                   '/export?gid=0&format=csv',
                   # Set first column as rownames in data frame
                   index_col=0
                  )
for idx, row in test.iterrows():
	country = row['country']
	asin = row['Asin']
	url.append('https://www.amazon.{}/dp/{}'.format(country,asin))

# this list stores all products
products = []

for u in url:
		source = s.get(u, headers=HEADERS)
    soup = BeautifulSoup(source.content, 'lxml')

		# this dictionary contains the information of a single product
		my_dict = {}

		# Product -> Title | Image Url | Price | Details
		title = soup.find("span", attrs={"id": 'productTitle'})
		if title is not None:
			my_dict['Title'] = title.text.strip()
		image = soup.find("img", attrs={"id": 'landingImage'})
		if image is not None:
			my_dict['Image'] = image.attrs["src"]
		price = soup.find("span", attrs={"class": 'a-offscreen'})
		if price is not None:
			my_dict['Price'] = price.text.strip()
		details_string = ''
		for details in soup.findAll("span", attrs={"class": 'a-list-item'}):
			if details.string is not None:
				details_value = details.text.strip()
				if len(details_value) != 1:
					details_string += details_value + ' '
		if details_string != '':
			my_dict['Details'] = details_string
		if my_dict != {}:
			products.append(my_dict)
		
with open('result.json', 'r+') as fp:
	try: 
		file_data = json.load(fp)
		file_data += products
		fp.seek(0)
		json.dump(file_data, fp, indent=4)
	except JSONDecodeError:
		json.dump(products, fp, indent=4)

'''-------------------------------END-------------------------------'''
