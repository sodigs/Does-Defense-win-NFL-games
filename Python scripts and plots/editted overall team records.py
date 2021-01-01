import requests

from bs4 import BeautifulSoup

import pandas as pd

#%%
#2010 Standings
url="https://www.espn.com/nfl/standings/_/season/2010/group/league"

page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")

table=soup.find("table")



x=soup.find_all('th')

x

column_titles=[th.getText() for th

               in soup.find_all('th')]

column_titles

data_rows=soup.find_all('tr')[1:]

standings=[]

for i in range(len(data_rows)):

    team_row=[]

    for td in data_rows[i].find_all('td'):

        team_row.append(td.getText())

    standings.append(team_row)

team_row

standings  

Rankings2010=pd.DataFrame(standings)

Rankings2010

teams=Rankings2010.iloc[:32,0]

yeap=teams.tolist()

yeap

ranks2010=Rankings2010[33:]

ranks2010['Teams']=yeap

ranks2010

#print(ranks['Teams'], "ranks['Teams']")



Acronyms= ['NE','ATL','PIT','BAL','CHI','NYJ','NO','IND','KC','PHI','GB','NYG','TB','SD','JAX','OAK','SEA','STL','MIA','MIN','TEN','DAL','DET','SF','HOU','WSH','ARI','CLE','DEN','BUF','CIN','CAR']

Names= ['Patriots','Falcons','Steelers','Ravens','Bears','Jets','Saints','Colts','Chiefs','Eagles','Packers','Giants','Buccaneers','Chargers','Jaguars','Raiders','Seahawks','Rams','Dolphins','Vikings','Titans','Cowboys','Lions','49ers','Texans','Redskins','Cardinals','Browns','Broncos','Bills','Bengals','Panthers']

pd1=pd.DataFrame(Acronyms)

pd2=pd.DataFrame(Names)

List2=pd.concat([pd1,pd2],axis=1)

List2.columns=["Symbol","Mascot"]
List2
#print(List2)


# count the number of rows in each dataframe

numRowsRanks = len(ranks2010.index)

numRowsList2 = len(List2.index)



# for each row of ranks dataframe

for i in range(numRowsRanks):

    # FOR UNDERSTANDING ONLY: print the current value in ranks table

    #print(ranks.iloc[i,12])

    

    # for each row in the renaming dataframe

    for j in range(numRowsList2):

        # FOR UNDERSTANDING ONLY: print the current symbol that the ranks 

        # table row is being evaluated against.

         #print(List2.iloc[j,0])



        # if the acronym is found in this row of the ranks table, 

        # replace it with the corresponding name

        if List2.iloc[j,1] in ranks2010.iloc[i,12]:

            ranks2010.iloc[i,12] = List2.iloc[j,0]


ranks2010
ranks2010.columns=['Wins','Loss','Ties','WinPct','Home','Away','Div','Conf','PF','PA','Diff','Streak','Teams']
Ranks2010=ranks2010.reset_index(drop=True)
Ranks2010
Ranks2010.at[25,'Teams']='WAS'
twentyten=Ranks2010
twentyten
#%%
#2011 - 2019 Standings
y=[1,2,3,4,5,6,7,8,9]

z=[]
for i in range(len(y)):
    f=url="https://www.espn.com/nfl/standings/_/season/201{}/group/league".format(y[i])
    z.append(f)
z


dat=[]
for i in z:
    page=requests.get(i)
    soup=BeautifulSoup(page.text,"html.parser")
    table=soup.find("table")
    x=soup.find_all('th')
    column_titles=[th.getText() for th

               in soup.find_all('th')]
    column_titles
    data_rows=soup.find_all('tr')[1:]
    standings=[]
    for i in range(len(data_rows)):

        team_row=[]

        for td in data_rows[i].find_all('td'):

            team_row.append(td.getText())

        standings.append(team_row)

    team_row

    standings  

    Rankings2010=pd.DataFrame(standings)

    Rankings2010

    teams=Rankings2010.iloc[:32,0]

    yeap=teams.tolist()

    yeap

    ranks2010=Rankings2010[33:]

    ranks2010['Teams']=yeap

    Acronyms= ['NE','ATL','PIT','BAL','CHI','NYJ','NO','IND','KC','PHI','GB','NYG','TB','SD','JAX','OAK','SEA','STL','MIA','MIN','TEN','DAL','DET','SF','HOU','WSH','ARI','CLE','DEN','BUF','CIN','CAR']

    Names= ['Patriots','Falcons','Steelers','Ravens','Bears','Jets','Saints','Colts','Chiefs','Eagles','Packers','Giants','Buccaneers','Chargers','Jaguars','Raiders','Seahawks','Rams','Dolphins','Vikings','Titans','Cowboys','Lions','49ers','Texans','Redskins','Cardinals','Browns','Broncos','Bills','Bengals','Panthers']

    pd1=pd.DataFrame(Acronyms)

    pd2=pd.DataFrame(Names)

    List2=pd.concat([pd1,pd2],axis=1)

    List2.columns=["Symbol","Mascot"]
    List2
#print(List2)


# count the number of rows in each dataframe

    numRowsRanks = len(ranks2010.index)

    numRowsList2 = len(List2.index)



# for each row of ranks dataframe

    for i in range(numRowsRanks):

    # FOR UNDERSTANDING ONLY: print the current value in ranks table

    #print(ranks.iloc[i,12])

    

    # for each row in the renaming dataframe

        for j in range(numRowsList2):

        # FOR UNDERSTANDING ONLY: print the current symbol that the ranks 

        # table row is being evaluated against.

         #print(List2.iloc[j,0])



        # if the acronym is found in this row of the ranks table, 

        # replace it with the corresponding name

            if List2.iloc[j,1] in ranks2010.iloc[i,12]:

                ranks2010.iloc[i,12] = List2.iloc[j,0]


    ranks2010
    ranks2010.columns=['Wins','Loss','Ties','WinPct','Home','Away','Div','Conf','PF','PA','Diff','Streak','Teams']
    Ranks2010=ranks2010.reset_index(drop=True)
    Ranks2010
    dat.append(Ranks2010)

dat=pd.concat(dat)
dat=dat.replace('WSHWashington','WAS')
dat=dat.replace('WSH','WAS')
dat



pd.set_option('display.max_rows',None)
print(dat)
dat.head()
dat

pd.DataFrame(dat,columns=['Wins','Loss','Ties','WinPct','Home','Away','Div','Conf','PF','PA','Diff','Streak','Teams'])
#%% 
#2010 to 2019 DataFrame
ranks=pd.concat([twentyten,dat],axis=0)
ranks
r2010=ranks.iloc[:32,:]
r2011=ranks.iloc[32:64,:]
r2012=ranks.iloc[64:96,:]
r2013=ranks.iloc[96:128,:]
r2014=ranks.iloc[128:160:]
r2015=ranks.iloc[160:192,:]
r2016=ranks.iloc[192:224,:]
r2017=ranks.iloc[224:256,:]
r2018=ranks.iloc[256:288,:]
r2019=ranks.iloc[288:320,:]
r2016
#%%


