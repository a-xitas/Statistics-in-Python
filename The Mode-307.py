## 1. Introduction ##

houses = pd.read_csv('AmesHousing_1.txt', delimiter='\t')

houses['Land Slope'].value_counts()

scale_land = 'ordinal'

scale_roof = 'nominal'

houses['Kitchen AbvGr'].value_counts()

kitchen_variable = 'discrete'

## 2. The Mode for Ordinal Variables ##

def moda(array):
    dct = {}
    for value in array:
        key = value
        if key in dct:
            dct[key] += 1
        else:
            dct[key] = 1
    #v = list(dct.values())
    #k = list(dct.keys())
    #return k[v.index(max(v))][0]
    return max(dct, key=dct.get)

mode_function = moda(houses['Land Slope'])


mode_method = houses['Land Slope'].mode()

same = mode_function == mode_method

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def Mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return [max(counts, key = counts.get), counts]
    #return counts

mode = Mode(houses['Roof Style'])[0]

value_counts = Mode(houses['Roof Style'])[1]

value_counts_metodo = houses['Roof Style'].value_counts()

## 4. The Mode for Discrete Variables ##


bedroom_variable = 'discrete'
bedroom_mode = houses['Bedroom AbvGr'].mode()


price_variable = 'continuous'
price_mode = houses['SalePrice'].mode()

price_mean = houses['SalePrice'].mean()

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)

mode = 150000
mean = houses['SalePrice'].mean()
median = houses['SalePrice'].median()

sentence_1 = True

sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

shape_1 = 'right skew'

shape_2 = 'right skew'

shape_3 = 'left skew'

## 7. Symmetrical Distributions ##

mode = houses['Mo Sold'].mode()

import matplotlib.pyplot as plt

houses['Mo Sold'].plot.kde(xlim=(1, 12))


plt.axvline(6, color='green', label='Mode')
plt.axvline(houses['Mo Sold'].median(), color='orange', label='Median')
plt.axvline(houses['Mo Sold'].mean(), color='black', label='Mean')

plt.legend()

plt.show()