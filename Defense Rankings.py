
pip install upgrade beautifulsoup4
pip install --upgrade html5lib
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
#%%
#2010 Defense
URL="https://www.footballoutsiders.com/stats/nfl/team-defense/2010"
page=requests.get(URL)
soup=BeautifulSoup(page.text,"html.parser")
table = soup.find("table")

soup.findAll('th')
column_headers= [th.getText() for th in
                 soup.find_all('th')]
data_rows=soup.find_all('tr')[1:]
team_data=[]
for i in range(len(data_rows)):
    player_row=[]
    for td in data_rows[i].find_all('td'):
        player_row.append(td.getText())
    team_data.append(player_row)

data_rows
column_headers
year10= pd.DataFrame(team_data)
year10
#%%
#2011 Defense
URL="https://www.footballoutsiders.com/stats/nfl/team-defense/2011"
page=requests.get(URL)
soup=BeautifulSoup(page.text,"html.parser")
table = soup.find("table")

soup.findAll('th')
column_headers= [th.getText() for th in
                 soup.find_all('th')]
data_rows=soup.find_all('tr')[1:]
team_data=[]
for i in range(len(data_rows)):
    player_row=[]
    for td in data_rows[i].find_all('td'):
        player_row.append(td.getText())
    team_data.append(player_row)



year11= pd.DataFrame(team_data,columns=column_headers)
year11.drop(columns=1)
year11
#%%
#2012 Defense
URL="https://www.footballoutsiders.com/stats/nfl/team-defense/2012"
page=requests.get(URL)
soup=BeautifulSoup(page.text,"html.parser")
table = soup.find("table")

soup.findAll('th')
column_headers= [th.getText() for th in
                 soup.find_all('th')]
data_rows=soup.find_all('tr')[1:]
team_data=[]
for i in range(len(data_rows)):
    player_row=[]
    for td in data_rows[i].find_all('td'):
        player_row.append(td.getText())
    team_data.append(player_row)



year12= pd.DataFrame(team_data,columns=column_headers)
year12
#%%
#2013 Defense
URL="https://www.footballoutsiders.com/stats/nfl/team-defense/2013"
page=requests.get(URL)
soup=BeautifulSoup(page.text,"html.parser")
table = soup.find("table")

soup.findAll('th')
column_headers= [th.getText() for th in
                 soup.find_all('th')]
data_rows=soup.find_all('tr')[1:]
team_data=[]
for i in range(len(data_rows)):
    player_row=[]
    for td in data_rows[i].find_all('td'):
        player_row.append(td.getText())
    team_data.append(player_row)



year13= pd.DataFrame(team_data,columns=column_headers)
year13