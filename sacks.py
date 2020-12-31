url="https://www.teamrankings.com/nfl/stat/sacks-per-game?date=2011-02-07"
page=requests.get(url)
soup= BeautifulSoup(page.text, "html.parser")
table= soup.find("table")
x=soup.find_all('th')
x
column_heads=[th.getText() for th
              in soup.find_all('th')]
column_heads
data_rows=soup.find_all('tr')[1:]
sacks=[]
for i in range(len(data_rows)):
    team_row=[]
    for td in data_rows[i].find_all('td'):
        team_row.append(td.getText())
    sacks.append(team_row)
sacks

sacks=pd.DataFrame(sacks, columns=column_heads)
sacks=sacks.iloc[:,[1,2]]
sacks
#%%
#Rename in Acronyms
Name= ['New England Patriots','Atlanta Falcons','Pittsburgh Steelers','Baltimore Ravens','Chicago Bears','NY Jets','New Orleans Saints','Indianapolis Colts','Kansas City Chiefs','Philadelphia Eagles','Green Bay Packers','NY Giants','Tampa Bay Buccaneers','LA Chargers','Jacksonville Jaguars','Las Vegas Raiders','Seattle Seahawks','LA Rams','Miami Dolphins','Minnesota Vikings','Tennessee Titans','Dallas Cowboys','Detroit Lions','San Francisco 49ers','Houston Texans','Washington Redskins','Arizona Cardinals','Cleveland Browns','Denver Broncos','Buffalo Bills','Cincinnati Bengals','Carolina Panthers']
Numteam=len(sacks['Team'])
Numnames= len(Name)
Numteam



for i in range(Numteam):
    for j in range (Numnames):
        if sacks.iloc[i,0] in Name[j]:
            sacks.iloc[i,0] = Name[j]
            
sacks
List2            

for i in range(Numteam):
    for j in range(numRowsList2):
        if List2.iloc[j,1] in sacks.iloc[i,0]:
            sacks.iloc[i,0]= List2.iloc[j,0]
            
sacks.columns= ['Teams','Sackspg']
sacks.at[26,'Teams']='WAS'
