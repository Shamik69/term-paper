import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
import statsmodels.api as stat

sns.set()
path= '/home/shamik/PycharmProjects/term paper/data'
data= pd.read_csv(f'{path}/final_output.csv')
gdp= preprocessing.scale(data['per capita GDP'])
unemployment= preprocessing.scale(data['unemployment rate'])
gini= preprocessing.scale(data['gini index'])

x0 = preprocessing.scale(data['unemployment rate'])
x1 = preprocessing.scale(data['gini index'])
y= preprocessing.scale(data['per capita GDP'])

constant0 = stat.add_constant(x0)
constant1 = stat.add_constant(x1)

model0= stat.OLS(y, x0).fit()
model1= stat.OLS(y, x1).fit()


sns.scatterplot(gdp, unemployment)
sns.lineplot(y, model0.predict(y), color='red')
plt.ylabel('unemployment rate')
plt.xlabel('per capita GDP')
plt.show()

sns.scatterplot(gdp, gini)
sns.lineplot(y, model1.predict(y), color='red')
plt.ylabel('gini index')
plt.xlabel('per capita GDP')
plt.show()