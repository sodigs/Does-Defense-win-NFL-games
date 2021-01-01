yearcorr=pd.read_csv('/Users/saumi/Documents/Python Projects/Correlation over years.csv')
yearcorr

totaltowin=yearcorr.iloc[:,0:2]
totaltowin

passtowin=yearcorr.iloc[:,2:4]
passtowin.columns=['Year','Correlation']
passtowin

rushtowin=yearcorr.iloc[:,4:6]
rushtowin.columns=['Year','Correlation']


rushtototal=yearcorr.iloc[:,6:8]
rushtototal.columns=['Year','Correlation']

passtototal=yearcorr.iloc[:,8:10]
passtototal.columns=['Year','Correlation']

rushtopass=yearcorr.iloc[:,10:12]
rushtopass.columns=['Year','Correlation']

#%%Total to win plot
plt.plot(totaltowin['Year'],totaltowin['Correlation'],'o')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.title("Correlation betweem Total DVOA and Win Pct")
m,b=np.polyfit(totaltowin['Year'],totaltowin['Correlation'],1)
TotalToWin=plt.plot(totaltowin['Year'],m*totaltowin['Year']+b)
#%% Pass to win plot
plt.plot(passtowin['Year'],passtowin['Correlation'],'o')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.title("Correlation betweem Pass DVOA and Win Pct")
m,b=np.polyfit(passtowin['Year'],passtowin['Correlation'],1)
PassToWin=plt.plot(passtowin['Year'],m*passtowin['Year']+b)
#%% Rush to win plot
plt.plot(rushtowin['Year'],rushtowin['Correlation'],'o')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.title("Correlation betweem Rush DVOA and Win Pct")
m,b=np.polyfit(rushtowin['Year'],rushtowin['Correlation'],1)
RushToWin=plt.plot(rushtowin['Year'],m*rushtowin['Year']+b)
#%% Rush to total plot
plt.plot(rushtototal['Year'],rushtototal['Correlation'],'o')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.title("Correlation betweem Rush DVOA and Total DVOA")
m,b=np.polyfit(rushtototal['Year'],rushtototal['Correlation'],1)
RushToTotal=plt.plot(rushtototal['Year'],m*rushtototal['Year']+b)
#%% Pass to total plot
plt.plot(passtototal['Year'],passtototal['Correlation'],'o')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.title("Correlation betweem Pass DVOA and Total DVOA")
m,b=np.polyfit(passtototal['Year'],passtototal['Correlation'],1)
PassToTotal=plt.plot(passtototal['Year'],m*passtototal['Year']+b)

#%%Rush to pass plot
plt.plot(rushtopass['Year'],rushtopass['Correlation'],'o')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.title("Correlation betweem Rush DVOA and PASS DVOA")
m,b=np.polyfit(rushtopass['Year'],rushtopass['Correlation'],1)
RushToPass=plt.plot(rushtopass['Year'],m*rushtopass['Year']+b)
#%%
RushToWin
RushToTotal
lin19
