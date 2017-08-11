from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page = 'http://money.rediff.com/gainers/bse'
with urlopen(quote_page) as page:
    html = page.read()

soup = BeautifulSoup(page,'html.parser')

table = soup.find('table', attrs={'class':'dataTable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
data=[]
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
print(data)