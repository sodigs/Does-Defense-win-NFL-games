
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

xgmerge=pd.concat([merge2010,merge2011,merge2012,merge2013,merge2014,merge2015,merge2016,merge2017,merge2018,merge2019])
xgmerge.head()
xgdata=xgmerge[['Total DVOA','Pass DVOA', 'Rush DVOA', 'WinPct']]
xgdata=pd.DataFrame(xgdata)
xgdata.columns=['Total_DVOA','Pass_DVOA','Rush_DVOA','WinPct']
xgdata['Total_DVOA']=xgdata['Total_DVOA'].astype(float)
xgdata['Pass_DVOA']=xgdata['Pass_DVOA'].astype(float)
xgdata['Rush_DVOA']=xgdata['Rush_DVOA'].astype(float)
xgdata['WinPct']=xgdata['WinPct'].astype(float)


x,y=xgdata.iloc[:,:-1],xgdata.iloc[:,-1]
dmatrixdata=xgb.DMatrix(data=x,label=y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123)
xg_reg=xgb.XGBRegressor(objective='reg:linear',colsample_bytree=0.3,learning_rate=0.1,max_depth=5,alpha=10,n_estimators=10)

xg_reg.fit(x_train,y_train)
preds=xg_reg.predict(x_test)
preds

y_test=y_test.map(floater)
y_test

x_test



rmse=np.sqrt(mean_squared_error(y_test,preds))
rmse
#%%
#k-folds
params={"objective":"reg:linear",'colsample_bytree':0.3,'learning_rate':0.1,'max_depth':5,'alpha':10}
cv_results=xgb.cv(dtrain=dmatrixdata,params=params,nfold=3,num_boost_round=50,early_stopping_rounds=10,metrics="rmse",as_pandas=True,seed=123)
cv_results
finalcv=(cv_results['test-rmse-mean'].tail(1))
finalcv

xgb.plot_importance(xg_reg)
plt.rcParams['figure.figsize'] = [10, 10]
plt.show()

#%%
#heatmap
mergecorr=xgdata.corr()
heatmerge=sns.heatmap(mergecorr,vmin=-1,vmax=1,cmap='viridis',annot=True,linewidth=0.1)

#%%
sns.pairplot(xgdata)
plt.plot(xgdata['Total_DVOA'],xgdata['WinPct'].map(floater),'o')
plt.xlabel('Total_DVOA')
plt.ylabel('Win %')
plt.title("2010-2019: Defense vs Win Pct")
m,b=np.polyfit(xgdata['Total_DVOA'],xgdata['WinPct'].map(floater),1)
total=plt.plot(xgdata['Total_DVOA'],m*xgdata['Total_DVOA']+b)

#%%
plt.scatter(x_test['Total_DVOA'],y_test,label="original")
plt.scatter(x_test['Total_DVOA'],preds,label="predicted")
plt.title("Win Pct Test and Predicted Values")
plt.legend()
plt.show()
#%%
#%%
#Multiple Linear Regression Model | Total DVOA + +Rush DVOA + Pass DVOA Logilikelihood=143.68, .352, .345
from sklearn import linear_model
import statsmodels.formula.api as smf
lm4=smf.ols(formula='WinPct~ Total_DVOA+Rush_DVOA+Pass_DVOA',data=xgdata).fit()
lm4.summary()

lm5=smf.ols(formula='WinPct~ Total_DVOA',data=xgdata).fit()
lm5.summary()
#%%

np.percentile(xgdata.Total_DVOA,[1,25,50,75,99])
xgdata.Total_DVOA.quantile([0.25,0.5,0.75])
#(0.188,0.06725,0.0095,-0.0695,-0.25181)
# lm: 0.4993-0.9708(x)

x=[0.188,0.06725,0.0095,-0.0695,-0.25181]
quantiles=[]
for i in x:
    z=0.4993-0.9708*i
    quantiles.append(z)
quantiles

#bottom 1% defense. Expected win %:
#31.6% win pct

#bottom 25% defense. Expected win %:
#34.4%

#middle 50% defense. Expected win %:
#49%

#top 25% defense. Expected win %:
#56.7%

#top 1% defense. Expected win %:
#74.4%

#%%
jut11
jut12
jut13
jut14
jut15
jut16
jut17
jut18
jut19
