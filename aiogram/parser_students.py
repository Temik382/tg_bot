from bs4 import BeautifulSoup
import requests

file = 'sent.xlsx'
###########################################     УСТАРЕВШИЙ ПАРСЕР, АКТУАЛЬНЫЙ - best_pars.py     !!!!!!!
###########################################     УСТАРЕВШИЙ ПАРСЕР, АКТУАЛЬНЫЙ - best_pars.py     !!!!!!!
###########################################     УСТАРЕВШИЙ ПАРСЕР, АКТУАЛЬНЫЙ - best_pars.py     !!!!!!!
###########################################     УСТАРЕВШИЙ ПАРСЕР, АКТУАЛЬНЫЙ - best_pars.py     !!!!!!!
###########################################     УСТАРЕВШИЙ ПАРСЕР, АКТУАЛЬНЫЙ - best_pars.py     !!!!!!!
###########################################     УСТАРЕВШИЙ ПАРСЕР, АКТУАЛЬНЫЙ - best_pars.py     !!!!!!!
url = 'https://lesmeh.edu35.ru/images/rasp/Raspisanie/hg.htm'

response = requests.get(url).content
l1, l2, l3, l4, l5, l6 = [], [], [], [], [], []
group_1 = []

s = BeautifulSoup(response, 'lxml')
dat = s.find('table', class_='inf')
data = dat.find_all('tr')
data2 = s.find_all('tr')
avg = s.find('div', class_='lrg2')
avg2 = avg.find('ul', class_='zg').find('li', class_='zgr').text

for i in data:
    group = i.find_all('td', class_='hd')

for j in data:
    if j.find('a', class_='hd'):
        l1.append(j.find('a', class_='hd').text)

for j in data:
    if j.find('td', class_='ur'):
        l3.append(j.find('td', class_='hd').text)


    elif j.find('td', class_='nul'):
        l3.append(j.find('td', class_='hd').text)
for h in data:
    if h.find('td', class_='ur'):
        l4.append(h.find('td', class_='ur').find('a', class_='z3').text)
    elif h.find('td', class_='nul'):
        l4.append('XX')

for k in data:
    if k.find('td', class_='ur'):
        if k.find('td', class_='ur').find('a', class_='z2'):
            l5.append(k.find('td', class_='ur').find('a', class_='z2').text)
        else:
            l5.append('')
    elif k.find('td', class_='nul'):
        l5.append('XX')

for x in data:
    if x.find('td', class_='ur'):
        group_1.append(x.find('a', class_='z1').text)
    elif x.find('td', class_='nul'):
        group_1.append('XX')




