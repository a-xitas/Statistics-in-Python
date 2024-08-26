## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim=[houses['SalePrice'].min(), 
                                   houses['SalePrice'].max()])

#Ploting the mean Sale Price of the houses DS in a vertical line:
plt.axvline(houses['SalePrice'].mean(), 
            color = 'black',
            label = 'Mean')

#Ploting a vertical line of the Standard deviation distance above the Mean value:
plt.axvline(houses['SalePrice'].mean() + houses['SalePrice'].std(ddof=0),
           color = 'red',
           label = 'Standard deviation')

#Ploting the price of 220.000 in a vertical line:
plt.axvline(220000,
            color = 'orange',
            label = '220000')

plt.legend()

plt.show()

very_expensive = False

## 2. Number of Standard Deviations ##

distance_mean_220 = 220000-houses['SalePrice'].mean()

st_devs_away =  distance_mean_220 / houses['SalePrice'].std(ddof=0) 

## 3. Z-scores ##

import numpy as np

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

# Criar uma função q me vá retornar o z_score de um conjunto de dados, com base num data_point particular:
def z_score (n, array):
    media = sum(array)/len(array)
    st_dev = np.std(array) 
    distancia = n - media
    z_score = distancia/st_dev
    return z_score

# Usar as funções nos 3 data_points mencionados acima:
min_z = z_score(min_val, houses['SalePrice'])
mean_z = z_score(mean_val, houses['SalePrice'])
max_z = z_score(max_val, houses['SalePrice'])




    

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    from numpy import std
    st_dev = std(array, ddof = bessel)
    distance = value - mean
    z = distance / st_dev
    return z

#############################################################
neighborhood_z_scores = {}

for n in houses['Neighborhood'].unique():
    data_by_neighborhood = houses[houses['Neighborhood']==n]
    z_scores = z_score(200000, data_by_neighborhood['SalePrice'], bessel=1)
    neighborhood_z_scores[n] = z_scores
    
best_investment = 'College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof=0)

# Transforming the Lot Area variable into a distribution of z-scores:
mean_area = houses['Lot Area'].mean()
stdev_area = houses['Lot Area'].std(ddof=0)
houses['z_area'] = houses['Lot Area'].apply(lambda x: ((x-mean_area) / stdev_area))

# Calcular a média e o desvio padrâo da variável z_area:
z_mean_area = houses['z_area'].mean()
z_stdev_area = houses['z_area'].std(ddof=0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

mean_pop = mean(population)
stdev_pop = std(population)

pop_standard = []
for i in population:
    pop_strd = ((i-mean_pop) / stdev_pop)
    pop_standard.append(pop_strd)
    
mean_z = mean(pop_standard)
stdev_z = std(pop_standard)
    

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample, ddof=1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof=0)

mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof=0)

houses['z_1'] = houses['index_1'].apply(lambda x: ((x-mean_index1) / stdev_index1))
houses['z_2'] = houses['index_2'].apply(lambda x: ((x-mean_index2) /stdev_index2))

print(houses[['z_1', 'z_2']][:2])

better = 'first'

## 9. Converting Back from Z-scores ##

houses['z_merged'] = houses['z_merged'].apply(lambda x: x*10 + 50)

mean_transformed = houses['z_merged'].mean()
stdev_transformed = houses['z_merged'].std(ddof=0)