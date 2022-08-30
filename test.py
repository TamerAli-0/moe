import requests
from bs4 import BeautifulSoup
url = "https://raw.githubusercontent.com/Blatzar/scraping-tutorial/master/README.md"
respone = requests.get(url)
soup = BeautifulSoup(respone.text, 'lxml')
element = soup.select("div.pre.language-python")
print(element[0].text.strip())