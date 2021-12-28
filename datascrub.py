import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pdfkit


url = 'https://www.transfermarkt.us/major-league-soccer/marktwerte/wettbewerb/MLS1/pos//detailpos/0/altersklasse/alle/plus/1/page/1' 
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

web = requests.get(url, headers=headers).text

source = BeautifulSoup(web, 'html.parser')
df = pd.read_html(source.prettify())
print(df)
df.to_csv()


"""table = source.find('table', class_ = 'items')
abbs = table.find_all('b')

abbs_list = [i.get_text().strip() for i in abbs]
print(abbs_list)"""



