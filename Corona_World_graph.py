"""Doesn't work anymore"""


import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt


def extract_contents(row):
    content = []
    for x in row:
        word = x.text.replace('\n', '')
        note = 0
        for i in range(len(word)):
            if word[i] == ' ':
                note = i
                break
        if note!=0:
            word = word[:note]
        content.append(word)
    return content


URL = "https://www.worldometers.info/coronavirus/"
HEADERS = ['Country', 'Total cases', 'New cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Seroius', 'cases/mill', 'deaths/mil']
response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')


stats = []
all_rows = soup.find_all('tr')

for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if len(stat) == 10:
        stats.append(stat)
    #print(stat)
stats.remove(stats[-1])
countries = [row[0] for row in stats]
active_cases = [row[6] for row in stats]
active_cases = [int(s.replace(',', '')) for s in active_cases]
deaths = [row[3] for row in stats]
for i in range(len(deaths)):
    if deaths[i] == ' ':
        deaths[i] = 0
    elif len(deaths[i]) < 4:
        deaths[i] = int(deaths[i])
    else:
        deaths[i] = int(deaths[i].replace(',', ''))

'''
for i in range(len(countries)):
    print(countries[i], ": ", active_cases[i])'''

countries = countries[:20]
active_cases = active_cases[:20]
deaths = deaths[:20]

objects = countries

fig, ax = plt.subplots()
y_pos = np.arange(len(objects))
bar_width = 0.35

r1 = plt.bar(y_pos, active_cases, bar_width, alpha=0.8, color='b', label='Active Cases')
r2 = plt.bar(y_pos+bar_width, deaths, bar_width,alpha=0.8, color='g',label='Deaths')
plt.xlabel('Countries')
plt.ylabel('People')
plt.title("Corona Active Cases vs Deaths[Top 20 Countries]")
plt.xticks(y_pos + bar_width, objects, rotation=90)
plt.legend()

#plt.tight_layout()


'''f1 = plt.figure(1)
performance = active_cases
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Active Cases')
plt.title('Active Corona Cases')

for i, v in enumerate(active_cases):
    plt.text(i, v+3, str(v), color='Black',fontsize=8, ha='center', rotation=0)

f2 = plt.figure(2)
performance = deaths
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Deaths')
plt.title('Deaths')

for i, v in enumerate(deaths):
    plt.text(i, v+3, str(v), color='Black',fontsize=8, ha='center', rotation=0)

'''
plt.show()
