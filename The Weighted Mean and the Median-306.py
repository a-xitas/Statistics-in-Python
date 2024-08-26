## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()

mean_original = houses['SalePrice'].mean()

difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['total_n_houses'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']

TOTAL_houses = houses_per_year['total_n_houses'].sum()

weighted_mean = TOTAL_houses/(houses_per_year['Houses Sold'].sum())

mean_original = houses['SalePrice'].mean()

difference = round(mean_original, 10) - round(weighted_mean, 10)

## 3. The Weighted Mean ##

import numpy as np

def media_ponderada(array_medias, array_pesos):
    somatorio_medias_ponderadas = (array_medias*array_pesos).sum()
    somatorio_pesos = array_pesos.sum()
    media_ponderada = somatorio_medias_ponderadas/somatorio_pesos
    return media_ponderada

weighted_mean_function = media_ponderada(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])

weighted_mean_numpy = np.average(houses_per_year['Mean Price'], weights=houses_per_year['Houses Sold'])

equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)

    

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

n_quartos = houses['TotRms AbvGrd'].replace('10 or more', 10).copy()

n_quartos = n_quartos.astype(int).sort_values()
print(n_quartos.shape
      )

n_quartos.value_counts().sort_index()

median = 6

## 6. The Median as a Resistant Statistic ##

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1 = houses['Lot Area'].plot.box()

ax2 = houses['SalePrice'].plot.box()

plt.show()

lot_mean = houses['Lot Area'].mean()
lot_median = houses['Lot Area'].median()

saleprice_mean = houses['SalePrice'].mean()
saleprice_median = houses['SalePrice'].median()

lotarea_difference = lot_mean - lot_median
saleprice_difference = saleprice_mean - saleprice_median

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()

median = houses['Overall Cond'].median()

houses['Overall Cond'].plot.hist()

plt.show()

more_representative = 'mean'