## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')


def Range (array):
    return max(array) - min(array)


range_by_year = {}

for h in houses['Yr Sold'].unique():
    sales_price_by_year = houses[houses['Yr Sold'] == h]
    range_by_year[h] = Range(sales_price_by_year['SalePrice'])        


one = False
two = True 


## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]


def avg_distancee(array):
    mean = sum(array)/len(array)
    lista = []
    for i in array:
        distancia = i - mean
        lista.append(distancia)
    return sum(lista)/len(lista)


avg_distance = avg_distancee(C)



## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def mean_absolute_deviation (array):
    mean = sum(array)/len(array)
    lista = []
    for n in array:
        absolute_distance = abs(n - mean)
        lista.append(absolute_distance)
    return sum(lista)/len(lista)


mad = mean_absolute_deviation(C)    

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def variance(array):
    media = sum(array)/len(array)
    lista=[]
    for n in array:
        squared_distance = (n - media)**2
        lista.append(squared_distance)
    return sum(lista)/len(lista)

variance_C = variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(array):
    media = sum(array)/len(array)
    lista=[]
    for n in array:
        squared_distance = (n-media)**2
        lista.append(squared_distance)
    return sqrt(sum(lista)/len(lista))

standard_deviation_C = standard_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

dictt_std_dev = {}
for y in houses['Yr Sold'].unique():
    data_per_y = houses[houses['Yr Sold'] == y]
    sale_price_stnddev = standard_deviation(data_per_y['SalePrice'])
    dictt_std_dev[y] = sale_price_stnddev

greatest_variability = max(dictt_std_dev, key=dictt_std_dev.get)
lowest_variability = min(dictt_std_dev, key=dictt_std_dev.get)



## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = 'sample 2'

st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

lista_stdev = []
for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state=i)
    stdev = standard_deviation(sample)
    lista_stdev.append(stdev)

plt.hist(lista_stdev)
plt.axvline(standard_deviation(houses['SalePrice']))

plt.show()

print(standard_deviation(houses['SalePrice']))

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(pop_stdev)  # pop_stdev is pre-saved from the last screen

plt.show()

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std()
numpy_stdev = numpy.std(sample['SalePrice'], ddof=1)

equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var()
numpy_var = numpy.var(sample['SalePrice'], ddof=1)

equal_vars = pandas_var == numpy_var
                      
                    

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

variances=[]
stdevs = []
for i in samples:
    var = numpy.var(i, ddof=1)
    stdev = numpy.std(i, ddof=1)
    variances.append(var)
    stdevs.append(stdev)

#Variances:
variances_mean = sum(variances) / len(variances)
variance_pop = numpy.var(population)

#Standard_Deviations:
stdevs_mean = sum(stdevs) / len(stdevs)
stdevs_pop = numpy.std(population)

equal_var = variances_mean == variance_pop
equal_stdev = stdevs_mean == stdevs_pop  