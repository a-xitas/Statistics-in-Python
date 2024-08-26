## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

freq_distro_pos = wnba['Pos'].value_counts()

freq_distro_height = wnba['Height'].value_counts()

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

unique = wnba['Age'].unique()

age_ascending = wnba['Age'].value_counts().sort_index()

age_descending = wnba['Age'].value_counts().sort_index(ascending=False)

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below

pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4,
                                                                 3,
                                                                 0,
                                                                 2,
                                                                 1,
                                                                 5]]
                                                                 
                                                                 

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')

age_relative_frequencies= wnba['Age'].value_counts(normalize=True) * 100

proportion_25 = wnba['Age'].value_counts(normalize=True)[25] 
percentage_30 = wnba['Age'].value_counts(normalize=True)[30]*100

over_30 = (wnba['Age'] >= 30).value_counts(normalize=True)*100
percentage_over_30 = 26.573427

bellow_23 = (wnba['Age'] <= 23).value_counts(normalize=True)*100
percentage_below_23 = 18.881119

teste = wnba['Age'].value_counts(normalize=True).sort_index(ascending=True)

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore

wnba = pd.read_csv('wnba.csv')

percentile_rank_half_less = percentileofscore(a=wnba['Games Played'], score=17, kind='weak')

percentage_half_more = 100-percentile_rank_half_less

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')

age_upper_quartile = wnba['Age'].describe()['75%']

age_middle_quartile =wnba['Age'].describe()['50%']

age_95th_percentile = wnba['Age'].describe(percentiles=[.95])['95%']

question1 = True
question2 = False
question3 = True

## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

#Frequency Distribution Table:
PTS_freq = wnba['PTS'].value_counts().sort_index()
#Grouped Frequency Distribution Table:
grouped_freq_table = wnba['PTS'].value_counts(bins=10, normalize=True).sort_index(ascending=False)*100

## 9. Information Loss ##

import pandas as pd

wnba = pd.read_csv('wnba.csv')

# Grouped Frequency Distribution Table for MIN:

MIN_grp_frq = wnba['MIN'].value_counts(bins=10).sort_index()


## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')

# o q estamos a fzr aqui é criarmos Nós a N/tabela de intervalos, escolhendo onde começar e onde acabar, e com que frequencia. P n deixarmos p Pandas essa tarefa pq se n ele coloca intervalos um pco esquesitos. Fazemos isso recorrendo à função pd.interval_range():
intervals = pd.interval_range(start=0, end=600, freq=60)

# a seguir criamos uma Serie com esses mm intervalos criados anteriormente, como indices, e atribuindo-lhes o valor de 0:
gr_freq_table_10 = pd.Series([0,0,0,0,0,0,0,0,0,0], index=intervals)

# por último, e atraves de uma serie de for loops, 1º fazemos um for loop à Serie onde nos interessam sacar os valores, dentro do wnba DF. 2º d cada x q passamos por um desses valores, vamos aos intervalos criados, e cada intervalo em particular e, se aquele valor estiver no intervalo adicionamos(somamos) o valor 1 aquele intervalo em particular. E assim sucessivamente:
for i in wnba['PTS']:
    for interval in intervals:
        if i in interval:
            gr_freq_table_10.loc[interval] +=1
            break
            
# prova dos 9! vemos qtos jogadores temos no N/DF (cada row equivale a um jogador, dai shape[0]) e igualamos isso à soma das N/distribuições absolutas q, se td estiver correcto, deverá dar TRUE! Isto pq a soma das N/distribuições tb deverá resultar no nmr do tal de jogadores no N/DF:      
print(wnba.shape[0] == gr_freq_table_10.sum())
    