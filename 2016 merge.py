import pandas as pd
import os
import numpy as np
def16=pd.read_csv('/Users/saumi/Documents/Python Projects/2016 Team DVOA Ratings Defense.csv')
def16
r2016
r2016=r2016.replace("STL","LAR")
merge2016=pd.merge(def16,r2016,how="left",on="Teams")
print(merge2016)
pd.set_option('display.max_columns',None)
merge2016
#%%
import matplotlib.pyplot as plt
import seaborn as sns
DVOAdf= merge2016[['Teams','Total DVOA Rank', 'Pass DVOA Rank', 'Rush DVOA Rank', 'WinPct']]
DVOAdf
DVOAdf.corr('pearson')
#%% DJUSTMENT
ok=DVOAdf['WinPct'].apply(lambda x: float(x))
floater= lambda x: float(x)
new=DVOAdf['WinPct'].map(floater)
new
#%% DVOA Value
import matplotlib.lines as mlines
perc=merge2016[['Teams','Total DVOA', 'Pass DVOA', 'Rush DVOA', 'WinPct']]
edperc= perc.assign(WinPct=new)
edperc.columns=['Teams','Total_DVOA','Pass_DVOA','Rush_DVOA','WinPct']
edperc
edperc.corr()
sns.pairplot(edperc)
plt.plot(edperc['Total_DVOA'],edperc['WinPct'].map(floater),'o')
plt.xlabel('Total DVOA')
plt.ylabel('Win %')
plt.title("2016: Defense vs Win Pct")
m,b=np.polyfit(edperc['Total_DVOA'],edperc['WinPct'].map(floater),1)
lin16=plt.plot(edperc['Total_DVOA'],m*edperc['Total_DVOA']+b)

lin16

np.corrcoef(edperc['Total_DVOA'],edperc['WinPct'].map(floater))

from scipy.stats import linregress
linregress(edperc['Total_DVOA'],edperc['WinPct'].map(floater))
linregress(edperc['Rush_DVOA'],edperc['WinPct'].map(floater))
#%%
#Heatmap

jut16=edperc.iloc[:,1:5].corr()
jut16
heat16=sns.heatmap(jut16,vmin=-1,vmax=1,cmap='viridis',annot=True,linewidth=0.1)

#%%
#Multiple Linear Regression Model | Total DVOA + +Rush DVOA + Pass DVOA Logilikelihood=10.766, .230, .148
from sklearn import linear_model
import statsmodels.formula.api as smf
lm4=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA+Pass_DVOA',data=edperc).fit()
lm4.summary()


