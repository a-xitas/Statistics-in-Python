## 2. Bar Plots ##

Exp_ordinal = wnba['Exp_ordinal'].value_counts(ascending=False).iloc[[
                                                                     3,
                                                                     0,
                                                                     2,
                                                                     1,
                                                                     4]]
                                                                     

Exp_ordinal.plot.bar()

## 3. Horizontal Bar Plots ##

Exp_ordinal = wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]]

Exp_ordinal.plot.barh(title='Number of players in WNBA by level of experience')


plt.show()
                                                      
                                                      

## 4. Pie Charts ##

Exp_ordinal = wnba['Exp_ordinal'].value_counts()

Exp_ordinal.plot.pie()

plt.show()

## 5. Customizing a Pie Chart ##

import matplotlib.pyplot as plt

Exp_ordinal = wnba['Exp_ordinal'].value_counts()

Exp_ordinal.plot.pie(figsize=(6,6), autopct='%.2f%%', title='Percentage of players in WNBA by level of experience')


plt.ylabel('')

plt.show()

## 6. Histograms ##

wnba['PTS'].plot.hist()

plt.show()

## 7. The Statistics Behind Histograms ##

import numpy as np

print(wnba['Games Played'].describe())

print(np.arange(2,585, 58.2))

wnba['Games Played'].plot.hist()

plt.show()

## 9. Binning for Histograms ##

import matplotlib.pyplot as plt

wnba['Games Played'].plot.hist(range=(1,32), bins=8, title='The distribution of players by games played')

plt.xlabel('Games played')

plt.show()

print(wnba['Games Played'].describe())

## 10. Skewed Distributions ##

wnba['AST'].plot.hist()

#wnba['FT%'].plot.hist()

assists_distro = 'right skewed'

ft_percent_distro = 'left skewed'

## 11. Symmetrical Distributions ##

#wnba['Age'].plot.hist()
#wnba['Height'].plot.hist()
wnba['MIN'].plot.hist()

normal_distribution = 'Height'