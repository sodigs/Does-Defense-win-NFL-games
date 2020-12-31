import pandas as pd
import os
import numpy as np
os.getcwd()
def11=pd.read_csv('/Users/saumi/Documents/Python Projects/2011 Team DVOA Ratings Defense.csv')
def11
r2011
merge2011=pd.merge(def11,r2011,how="left",on="Teams")
print(merge2011)
pd.set_option('display.max_columns',None)
merge2011
#%%
import matplotlib.pyplot as plt
import seaborn as sns
DVOAdf= merge2011[['Teams','Total DVOA Rank', 'Pass DVOA Rank', 'Rush DVOA Rank', 'WinPct']]
DVOAdf
DVOAdf.corr('pearson')
plt.scatter(DVOAdf['Total DVOA Rank'],DVOAdf['WinPct'].map(floater))
#%% Ranking
ok=DVOAdf['WinPct'].apply(lambda x: float(x))
floater= lambda x: float(x)
new=DVOAdf['WinPct'].map(floater)
new
eddf= DVOAdf.assign(WinPct=new)
eddf
eddf.corr()
sns.pairplot(eddf)
#%% DVOA Value
import matplotlib.lines as mlines
perc=merge2011[['Teams','Total DVOA', 'Pass DVOA', 'Rush DVOA', 'WinPct']]
edperc= perc.assign(WinPct=new)
edperc.columns=['Teams','Total_DVOA','Pass_DVOA','Rush_DVOA','WinPct']
edperc
edperc.corr()
sns.pairplot(edperc)
plt.plot(edperc['Total_DVOA'],edperc['WinPct'].map(floater),'o')
plt.xlabel('Total DVOA')
plt.ylabel('Win %')
plt.title("2011: Defense vs Win Pct")
m,b=np.polyfit(edperc['Total_DVOA'],edperc['WinPct'].map(floater),1)
lin11=plt.plot(edperc['Total_DVOA'],m*edperc['Total_DVOA']+b)

lin11

np.corrcoef(edperc['Total_DVOA'],edperc['WinPct'].map(floater))

from scipy.stats import linregress
linregress(edperc['Total_DVOA'],edperc['WinPct'].map(floater))
linregress(edperc['Rush_DVOA'],edperc['WinPct'].map(floater))
#%%
#Heatmap

jut11=edperc.iloc[:,1:5].corr()
jut11
heat11=sns.heatmap(jut11,vmin=-1,vmax=1,cmap='viridis',annot=True,linewidth=0.1)

#%%
#Multiple Linear Regression Model | Total DVOA + +Rush DVOA + Pass DVOA Logilikelihood=13.229, .368, .301
from sklearn import linear_model
import statsmodels.formula.api as smf
lm4=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA+Pass_DVOA',data=edperc).fit()
lm4.summary()


