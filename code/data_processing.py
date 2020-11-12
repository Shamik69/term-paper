import pandas as pd

path = '/home/shamik/PycharmProjects/term paper/data'
per_capita = pd.read_csv(f'{path}/per capita GDP.csv')
unemployment = pd.read_csv(f'{path}/unemployment rate.csv')
gini = pd.read_csv(f'{path}/gini_index.csv')
country_codes = pd.read_csv(f'{path}/countries_iso.csv')
countries0 = []
countries1 = []
countries2 = []
x0 = list(country_codes['Alpha3 code'])
x1 = list(country_codes['Alpha2 code'])
y = list(country_codes['Country'])
for df, counter in (per_capita, 0), (unemployment, 1):
    for x in df['ISO']:
        c = y[x0.index(f' {x}')]
        if counter == 0:
            countries0.append(c)
        elif counter == 1:
            countries1.append(c)
del x, counter
for x in gini['Country Code']:
    c = y[x1.index(f' {x}')]
    countries2.append(c)
index0 = [x for x in countries1 if x in countries2]
alpha3_list = []
alpha2_list = []
for i in index0:
    c0 = x0[y.index(f'{i}')]
    c1 = x1[y.index(f'{i}')]
    for alpha, counter in (c0, 0), (c1, 1):
        w = list(alpha)
        q = w.count(' ')
        for r in range(q):
            w.remove(' ')
        w = ''.join(w)
        if counter == 0:
            f0 = w
        elif counter == 1:
            f1 = w
    alpha2_list.append(f1)
    alpha3_list.append(f0)
del alpha, counter
per_capita_GDP = []
unemployment_rate = []
gini_index = []
for beta, counter0 in (alpha2_list, 0), (alpha3_list, 1):
    for alpha in beta:
        if counter0 == 0:
            list0 = list(gini['Country Code'])
            list1 = list(gini['gini index'])
            gini_index.append(list1[list0.index(alpha)])
        elif counter0 == 1:
            for df, counter1 in (per_capita, 0), (unemployment, 1):
                if counter1 == 0:
                    list0 = list(per_capita['ISO'])
                    list1 = list(per_capita['per capita GDP'])
                    per_capita_GDP.append(list1[list0.index(alpha)])
                elif counter1 == 1:
                    list0 = list(unemployment['ISO'])
                    list1 = list(unemployment['unemployment rate'])
                    unemployment_rate.append(list1[list0.index(alpha)])

dict0 = {'Country': index0,
         'per capita GDP': per_capita_GDP,
         'unemployment rate': unemployment_rate,
         'gini index': gini_index}
final_list= pd.DataFrame(dict0).to_csv(f'{path}/final_output.csv', index= False)