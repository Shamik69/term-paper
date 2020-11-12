import time
import pandas as pd

t0= time.time()
df = pd.read_csv('C:/Users/User/PycharmProjects/ProjectTsukinome/dataset/baal/WEOOct2019all.csv')
t1= time.time()
print(df.columns)
data = df[['ISO', 'Country', 'Subject Descriptor', 'Units', 'Scale', '2019']]
per_capita = data[data['Subject Descriptor'] == 'Gross domestic product per capita, constant prices']
unemployment= data[data['Subject Descriptor'] == 'Unemployment rate']
per_capita = per_capita[per_capita['Units'] == 'Purchasing power parity; 2011 international dollar']
for x, y in (per_capita, 'per capita GDP'), (unemployment, 'unemployment rate'):
    x = x[['ISO', 'Country', '2019']]
    x = x.dropna()
    a = []
    for i in x['2019']:
        f = list(i)
        c = f.count(',')
        if c > 0:
            for k in range(c):
                f.remove(',')
        f = ''.join(f)
        f = float(f)
        a.append(f)
    x= x.drop('2019', axis=1)
    x.insert(loc=2, column=y, value=a)
    x.to_csv('C:/Users/User/PycharmProjects/ProjectTsukinome/dataset/baal/'
             f'{y}.csv', index=False)

