from bs4 import BeautifulSoup
import requests

html = requests.get('https://lesmeh.edu35.ru/images/rasp/Raspisanie/hg.htm').content
soup = BeautifulSoup(html, 'lxml')
rows = soup.find_all('tr')


list1 = []
list2 = []
groups = []
gr = []
new_gr = []
for gr1 in rows:
    gr.append(gr1.find('td').text)

        

for j in rows:
    if j.find('a', class_='hd'):
        groups.append(j.find('a', class_='hd').text)
for row in rows:
    cells = row.find_all('td')
    if len(cells) >= 2: # Проверяем наличие хотя бы двух ячеек
        first_cell = cells[0]
        second_cell = cells[1]

        ur_cells = [cell for cell in cells if 'ur' in cell.get('class', [])] # Находим все ячейки с классом ur
        nul_cells = [cell for cell in cells if 'nul' in cell.get('class', [])] # Находим все ячейки с классом nul


        if len(ur_cells) == 1: # Одна ячейка с классом ur
            if len(nul_cells) > 0 and cells.index(ur_cells[0]) > cells.index(nul_cells[0]): # ur после nul
                subject = ur_cells[0].find('a', class_='z1')
                if subject:
                    list2.append([subject.text, row.find('td', class_='hd').text])
                else:
                    list2.append('XX')
            elif len(nul_cells) > 0 and cells.index(ur_cells[0]) < cells.index(nul_cells[0]): # ur перед nul
                subject = ur_cells[0].find('a', class_='z1')
                if subject:
                    list1.append([subject.text, row.find('td', class_='hd').text])
                else:
                    list1.append('XX')
            else: # Только ur
                subject = ur_cells[0].find('a', class_='z1')
                if subject:
                    list1.append([subject.text, row.find('td', class_='hd').text])
                    list2.append([subject.text, row.find('td', class_='hd').text])

        elif len(ur_cells) == 2: #Две ячейки ur
            subject1 = ur_cells[0].find('a', class_='z1')
            subject2 = ur_cells[1].find('a', class_='z1')
            if subject1:
                list1.append([subject1.text, row.find('td', class_='hd').text])
            else:
                list1.append('XX')
            if subject2:
                list2.append([subject2.text, row.find('td', class_='hd').text])
        else:
            list2.append('XX')
            list1.append('XX')
            
for i in gr:
    if len(i) >= 5 and i[-1] in '0123456789':
        new_gr.append(i)

def create_groups(lst):
    groups = {}
    current_group = 0
    current_items = []
    x_count = 0
    for item in lst:
        if item == 'XX':
            x_count += 1
            if current_items:
                groups[f'Группа_{current_group}'] = current_items
                current_items = []
                current_group += 1
                x_count = 0
            if x_count > 14:
                groups[f'Группа_{current_group}'] = 'Выходной'
                current_group += 1
                x_count = 0
        else:
            current_items.append(item)

    if current_items:
        groups[f'Группа_{current_group}'] = current_items

    return groups

grouped_list1 = create_groups(list1)
grouped_list2 = create_groups(list2)

# Изменение ключей на значения из списка new_gr
def rename_keys(groups, new_keys):
    new_groups = {}
    existing_keys = list(groups.keys())
    for idx, key in enumerate(existing_keys):
        if idx < len(new_keys):
            new_groups[new_keys[idx]] = groups[key]
    return new_groups

grouped_list1_renamed = rename_keys(grouped_list1, new_gr)
grouped_list2_renamed = rename_keys(grouped_list2, new_gr)


