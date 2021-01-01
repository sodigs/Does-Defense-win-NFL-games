# Does-Defense-win-NFL-games
##I started out with the question, **How important is defense to winning NFL games?** 

To track defensive play, we used the metric DVOA. [DVOA Explanation](https://www.footballoutsiders.com/info/methods) 

DVOA stands for Defense-adjusted Value Over Average, although we use the same letters to refer to defensive rankings which are adjusted to take into account the quality of offensive opponents. When not adjusted for opponent, this stat is called VOA. The main statistic used on Football Outsiders, DVOA breaks down the entire season play-by-play, comparing success on each play to the league average based on a number of variables including down, distance, location on field, current score gap, quarter, and opponent quality. While it can be used as a measure of total team performance, it differs from other power ratings found throughout the Web because it can be broken down to analyze team effectiveness in any number of ways: down, quarter, rushing vs. receiving, location on field, passes to backs vs. passes to receivers, and so on. **The lower the DVOA, the better the defense.**

Using beautiful soup, I scraped DVOA rankings from 2010 to 2019 from the Pro Football Outsiders website. I then scraped the NFL Standings for the same time period from ESPN.com. I cleaned, wrangled, and sorted the data to the point where I was able to merge the Defensive ranking data frame with the NFL Standings Data Frame by team and year. I also scraped sacks per game for every team in 2010 and added it to the 2010 Data Frame. Using the variables Sacks per game, Total DVOA, Rush DVOA, and Pass DVOA, I generated models with all the possible combinations in regressing those variables onto win percentage. Sacks per game ended drawing a very low correlation of .31 to win percentage, as well as not being very statistically significant in the OLS models, with p-values around 0.8. The model that was chosen to was the OLS model where Win percentage was regressed on Total DVOA, Pass DVOA, and Rush DVOA. This model had the highest adjusted R-squared value with .226. It also had a Log-likelihood value of 14.45, and R-squared of 0.301, both among one of the highest scores for those two respective metrics among all the models.

For 2010 to 2019, linear regressions were run on the data for each individual year. And correlations between all four variables were also tracked in heat maps for every year. This was to see if any trends could be detected such as Pass defense being more important to Win percentage because of the increase in the passing game over the past decade. The only real trend that was found was that the correlation of Rush DVOA to Total DVOA overall showed a slightly downward trend, with 2015 and 2018 being outliers. The correlation between Total DVOA, Pass DVOA, and Rush DVOA and Win Percentage varied sporadically from year to year. One trend was that Pass DVOA always had a correlation over 0.9 to Total DVOA every year, it was always significantly higher than the correlation between Rush DVOA and Pass DVOA. And other than 2018, the correlation between Pass DVOA and Win Percentage was always higher than the correlation between Rush DVOA and Win Percentage.

All the data from 2010 to 2019 was combined into one large data frame, and analysis was performed. I used XGboost to perform gradient boosting for regression analysis on the aggregated data set. Gradient boosting is a supervised machine learning algorithm that uses decision trees to help minimize loss when adding new models. I imported skicit_learn to create a training and testing data set, and combined with XG boost, trained the model to help predict Win Percentage based off of Total DVOA, Rush DVOA, and Pass DVOA. Overall there were 320 data points, however the best model that  was able to be built has a root mean square error of 0.19. So the average predicted win percentage was off by 19% from the true win percentage, which is quite large. So overall, with the data from the last 10 years, just knowing a team’s Total DVOA, Pass DVOA, and Rush DVOA is not enough to accurately predict their total win percentage. It is interesting to note however that XG boost found Total DVOA and Pass DVOA to be much more important features in predicting Win Percentage. Total DVOA has an F-score of 4, and Pass DVOA had an F score of 2. 

Finally, I used OLS Regression on the aggregated data over all the years, regressing solely Total DVOA onto Win Percentage.

[OLS Regression explained](https://setosa.io/ev/ordinary-least-squares-regression/)

Based off of the ten years of data I found:

-If you finished in the bottom 1% of defense that year in the league, you had a predicted win percentage of 31.6%. 

-Bottom 25%, expected win percentage of 34.4%.

-Middle 50%, expected win percentage of 49%. 

-Top 25%, expected win percentage of 56.7%. 

-Top 1%, expected win percentage of 74.4%

Heat Map for the correlation across data from 2010 to 2019:


![Final heat map](https://user-images.githubusercontent.com/75696444/103423509-f98d2b00-4b74-11eb-9a4d-e3ab8a344719.png)

OLS Plot:

![Final OLS Plot](https://user-images.githubusercontent.com/75696444/103423675-e6c72600-4b75-11eb-9199-703b148dd28e.png)

Pairplot:

![Final pairplot](https://user-images.githubusercontent.com/75696444/103423738-41f91880-4b76-11eb-888e-cb03228769d7.png)


