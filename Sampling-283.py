## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

h = wnba.head()

t  = wnba.tail()

parameter = wnba['Games Played'].max()

sample = wnba.sample(30, random_state=1)

statistic = sample['Games Played'].max()

sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

wnba = pd.read_csv('wnba.csv')

list_pts_sample = []

for i in range(100):
    pts_sample = wnba['PTS'].sample(10, random_state=i).mean()
    list_pts_sample.append(pts_sample)

  
plt.scatter(x=np.arange(1, 101), y=list_pts_sample)
plt.axhline(wnba['PTS'].mean())
plt.show()

## 7. Stratified Sampling ##

wnba['points_per_game'] = wnba['PTS']/wnba['Games Played']

h = wnba.head()

G = wnba[wnba['Pos'] == 'G']
F = wnba[wnba['Pos'] == 'F']
C = wnba[wnba['Pos'] == 'C']
G_F = wnba[wnba['Pos'] == 'G/F']
F_C = wnba[wnba['Pos'] == 'F/C']

#for i in wnba['Pos'].unique():
 #   pos = wnba[wnba['Pos'] == i]
  #  print(pos)

positions = [G, F, C, G_F, F_C]
positions_str = ['G', 'F', 'C', 'G_F', 'F_C']

points_per_position = {}


for p in range(0,5):
    sample = positions[p]['points_per_game'].sample(10, random_state=0).mean()
    position = positions_str[p]
    points_per_position[position] = sample
                           
print(points_per_position)

position_most_points = 'C'
    

## 8. Proportional Stratified Sampling ##

import numpy as np

print(wnba['Games Played'].value_counts(bins=3, normalize=True)*100)

sample_PTS_means = []

for i in range (100):
    twelve_g = wnba[wnba['Games Played'] <= 12].sample(1, random_state=i)
    twelve_22_g = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)].sample(2, random_state=i)
    plus_22_g = wnba[wnba['Games Played'] > 22].sample(7, random_state=i)
    proportional_stratified_sample = pd.concat([twelve_g, twelve_22_g, plus_22_g])
    sample_PTS_means.append(proportional_stratified_sample['PTS'].mean())
   
#mean of the Proportional Stratified Sample (PSS):
pop_mean = wnba['PTS'].mean()


plt.scatter(x=np.arange(1, 101), y=sample_PTS_means)
plt.axhline(pop_mean)

plt.show()

## 10. Cluster Sampling ##

clusters_selection = pd.Series(wnba['Team'].unique()).sample(4, random_state=0)

clusters_data = pd.concat([wnba[wnba['Team'] == 'PHO'], 
                           wnba[wnba['Team'] == 'IND'], 
                           wnba[wnba['Team'] == 'MIN'], 
                           wnba[wnba['Team'] == 'ATL']]) 

Height_mean = clusters_data['Height'].mean()
Age_mean = clusters_data['Age'].mean()
BMI_mean = clusters_data['BMI'].mean()
Total_points_mean = clusters_data['PTS'].mean()
#measuring our sample error  (parametro[população] - estatistica[amostra]):
sampling_error_height = wnba['Height'].mean() - Height_mean
sampling_error_age = wnba['Age'].mean() - Age_mean
sampling_error_BMI = wnba['BMI'].mean() - BMI_mean
sampling_error_points = wnba['PTS'].mean() - Total_points_mean