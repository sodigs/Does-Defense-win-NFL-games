import pandas as pd
floater= lambda x: float(x)
def10=pd.read_csv('/Users/saumi/Documents/Python Projects/2010 Team DVOA Ratings Defense.csv')
def10
r2010=r2010.replace("WSH","WAS")
merge2010=pd.merge(def10,r2010,how="left",on="Teams")
print(merge2010)
pd.set_option('display.max_columns',None)
merge2010
#%%
import matplotlib.pyplot as plt
import seaborn as sns
DVOAdf= merge2010[['Teams','Total DVOA Rank', 'Pass DVOA Rank', 'Rush DVOA Rank', 'WinPct']]
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
perc=merge2010[['Teams','Total DVOA', 'Pass DVOA', 'Rush DVOA', 'WinPct']]
edperc= perc.assign(WinPct=new)
edperc.columns=['Teams','Total_DVOA','Pass_DVOA','Rush_DVOA','WinPct']
edperc
edperc.corr()
sns.pairplot(edperc)
plt.scatter(edperc['Total_DVOA'],edperc['WinPct'].map(floater))
np.corrcoef(edperc['Total_DVOA'],edperc['WinPct'].map(floater))

from scipy.stats import linregress
linregress(edperc['Total_DVOA'],edperc['WinPct'].map(floater))
linregress(edperc['Rush_DVOA'],edperc['WinPct'].map(floater))
#%%
#Adding sacks to Regression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

defsacks= pd.merge(edperc,sacks,how='left',on="Teams")
defsacks= pd.merge(defsacks,eddf,how='left',on="Teams")
defsacks
defsacks.columns=['Teams','Total_DVOA','Pass_DVOA','Rush_DVOA','WinPct','Sackspg','Total_DVOA_Rank','Pass_DVOA_Rank','Rush_DVOA_Rank','WinPct_y']
eddefsacks=defsacks['Sackspg'].map(floater)
eddefsacks
editdefsacks=defsacks.assign(Sackspg=eddefsacks)
jut10=editdefsacks.iloc[:,1:6].corr()
jut10
editdefsacks.corr()
sns.pairplot(editdefsacks.iloc[:,1:6])
heat10=sns.heatmap(jut10,vmin=-1,vmax=1,cmap='viridis',annot=True,linewidth=0.1)
#%%
#Multiple Linear Regression Model | Total DVOA_Rank Logilikelihood=14.29,.294,.218
lm0=smf.ols(formula='WinPct~ Total_DVOA_Rank+Pass_DVOA_Rank+Rush_DVOA_Rank',data=editdefsacks).fit()
lm0.summary()


#%%
#Multiple Linear Regression Model | Total DVOA + Sackspg Logilikelihood=13.3,0.250,0.198


from sklearn import linear_model
import statsmodels.formula.api as smf
lm1=smf.ols(formula='WinPct~ Total_DVOA+Sackspg',data=editdefsacks).fit()
lm1.summary()
 
#%%
#Multiple Linear Regression Model | Total DVOA + +Rush DVOA + Sackspg Logilikelihood=13.5,.258,.179
lm2=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA+Sackspg',data=editdefsacks).fit()
lm2.summary()

#%%
#Multiple Linear Regression Model | Total DVOA + +Rush DVOA + Pass DVOA +Sackspg Logilikelihood=14.487, .303, .199
lm3=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA+Pass_DVOA+Sackspg',data=editdefsacks).fit()
lm3.summary()
#%%
#Multiple Linear Regression Model | Total DVOA + +Rush DVOA + Pass DVOA Logilikelihood=14.45, .301, .226
lm4=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA+Pass_DVOA',data=editdefsacks).fit()
lm4.summary()

#%%
#Multiple Linear Regression Model | Total DVOA + Pass DVOA Logilikelihood=13.335, .250, .199
lm5=smf.ols(formula='WinPct~ Total_DVOA+Pass_DVOA',data=editdefsacks).fit()
lm5.summary()
#%%
#Multiple Linear Regression Model | Total DVOA + Rush DVOA Logilikelihood=13.488, .258, .206
lm6=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA',data=editdefsacks).fit()
lm6.summary()
#%%
#Multiple Linear Regression Model | Total DVOA + Rush DVOA Logilikelihood=13.488, .258, .206
lm6=smf.ols(formula='WinPct~ Total_DVOA',data=editdefsacks).fit()
lm6.summary()
#%%
xs=merge2010['Teams']
ys=merge2010['WinPct'].map(floater)
plt.scatter(xs,ys)
#for i, txt in enumerate(merge2010['Teams']):
 #   plt.annotate(txt,merge2010['Teams'][i],merge2010['WinPct'][i])
    
for x,y in zip(xs,ys):
    label = merge2010['Teams']
    plt.annotate(label,(x,y))
    
plt.show()
#%%
editdefsacks
x=editdefsacks.iloc[:,1:4].values
y=editdefsacks.iloc[:,4].values
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3)
from sklearn.ensemble import RandomForestRegressor
RandomForestRegModel=RandomForestRegressor()
RandomForestRegModel.fit(x_train,y_train)
y_pred=RandomForestRegModel.predict(x_test)
y_pred
y_test
xaxis=x_test[:,0:1]
xaxis
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
rmse

ax=plt.gca()

ax.scatter(xaxis,y_test,color='b')
ax.scatter(xaxis,y_pred,color='r')

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred=lr.predict(x_test)
y_pred
pd.DataFrame(y_pred)

#%%




nested_dic={'washington':{'pass_dvoa':.06,'total_dvoa':-.056}}
def pot(teamname,nested_dic):
    dvoa=nested_dic[teamname]["total_dvoa"]
    result = -1.0175*dvoa+ 0.4983
    nested_dic[teamname]["prdwin"]=result
    return result
pot('washington',nested_dic)
print(nested_dic['washington']["prdwin"])
nested_dic

nested_dict = { 'dict1': {'key_A': 'value_A'}, 
                'dict2': {'key_B': 'value_B'}}

 
