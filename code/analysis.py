from sklearn import preprocessing, cluster
import pandas as pd
import numpy as np

path= 'C:/Users/User/PycharmProjects/term paper/data'
data= pd.read_csv(f'{path}/final_output.csv').drop('Country', axis=1)
data= pd.DataFrame(preprocessing.scale(data), columns=['per capita GDP', 'unemployment rate', 'gini index'])

km = cluster.KMeans(
    n_clusters=3, init='random',
    n_init=10, max_iter=300,
    tol=1e-04, random_state=0
)
y_km = km.fit_predict(data)
print(data)