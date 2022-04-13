# Count images in a webpage via web-scraping

from bs4 import BeautifulSoup
import requests
import re
base_url = "https://www.luminus.be"
parent_url = "https://www.luminus.be/nl/prive/extras"
sample_url = "https://www.luminus.be/nl/prive/extras/gamma"

'''
#Get image details

from bs4 import BeautifulSoup
html_text = requests.get(sample_url).text
soup = BeautifulSoup(html_text, 'html.parser')
lyrs = soup.findAll("img", alt="Paasei van de EXTRAS! Paaswedstrijd.")
print(lyrs)
'''

from bs4 import BeautifulSoup
# Get all weblinks from this parent url
html_text = requests.get(parent_url).text
soup = BeautifulSoup(html_text, 'html.parser')
links = []

for link in soup.findAll('a', attrs={'href': re.compile("/nl/prive/extras/*")}):
    links.append(link.get('href'))

#print(links)

count = 0
# Loop over all the pages of website and fetch em elements
for extra in links:
    print(extra)
    if "http" not in extra:
        extra_url = base_url+extra
        #print(extra_url, " modified")
    else:
        extra_url = extra
    #print(extra_url)
    html_text = requests.get(extra_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    lyrs = soup.findAll("img", alt="Paasei van de EXTRAS! Paaswedstrijd.")
    if len(lyrs) > 0:
        count = count + 1
        print(lyrs)    
print(count, " in total")
    