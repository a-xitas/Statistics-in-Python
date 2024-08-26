## 2. Grouped Bar Plots ##

import seaborn as sns

ax = sns.countplot(x='Exp_ordinal', hue='Pos', data=wnba, order=['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],hue_order = ['C', 'F', 'F/C', 'G', 'G/F'])

## 3. Challenge: Do Older Players Play Less? ##

ax = sns.countplot(x='age_mean_relative', hue='min_mean_relative', data=wnba)

result = 'rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt

wnba[wnba.Age >=27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label= 'Young', legend =True)

plt.axvline(497, label='Average')
plt.legend()

plt.show()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >=27]['MIN'].plot.kde(label = 'Old', legend=True)

wnba[wnba['Age'] < 27]['MIN'].plot.kde(label = 'Young', legend=True)

plt.axvline(497, label = 'Average')
plt.legend()

plt.show()

## 7. Strip Plots ##

import seaborn as sns

f_w = wnba[wnba.Pos == 'F']['Weight']
g_f_w = wnba[wnba.Pos == 'G/F']['Weight']
g_w = wnba[wnba.Pos =='G']['Weight']
c_w = wnba[wnba.Pos == 'C']['Weight']
f_c_w = wnba[wnba.Pos == 'F/C']['Weight']

sns.stripplot(x='Pos', y='Weight', data=wnba, jitter=True)

plt.show()

print(wnba[['Height', 'Weight']].corr())

## 8. Box plots ##

sns.boxplot(x='Pos', y='Weight', data=wnba)

plt.show()

## 9. Outliers ##

#calcular o interquartile range (upperquartile[75%]-lowerquartile[25%]):
iqr = 29-22
#calcular o upper e lower bound, utilizando um whis de 1.5. O upper bound é o iqr * o whis de 1.5 + o valor do 3º quartil (75%). O lower bound é o mesmo processo, m agora vamos ao 1º quartil (25%), e retiramos a este valor o iqr multiplicado de 1.5:
upper_bound = 29+(7*1.5)
lower_bound = 22-(7*1.5)
#se o máximo é 32, e se o upper bound é 39.5, então poderemos presumir q não existirão outliers inferiores:
outliers_high = 0

outliers_low = round(11.5-0)

sns.boxplot(x='Games Played', data=wnba)
plt.show()