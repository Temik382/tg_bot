import requests
from bs4 import BeautifulSoup


url = 'https://lesmeh.edu35.ru/dni-otkr-dverej-2/nashi-spetsialnosti'
response = requests.get(url).content
soup = BeautifulSoup(response, 'lxml')

data = soup.find('div', class_='attachmentsList')
data2 = data.find('table')
tr = data.find_all('tr')
list_sp = []
new_list = []
for i in tr:
    list_sp.append(str(i.find('td', class_='at_filename').find('a', class_='at_url').text))
for j in list_sp:
     new_list.append(j.replace('.pdf', ''))
print(new_list)