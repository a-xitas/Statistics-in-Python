## 2. Quantitative and Qualitative Variables ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative', 'Height': 'quantitative', 'BMI': 'quantitative',
             'Birth_Place': 'qualitative', 'Birthdate': 'quantitative', 'Age': 'quantitative', 'College': 'qualitative', 'Experience': 'quantitative',
             'Games Played': 'quantitative', 'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
             '3PA': 'quantitative', 'FTM': 'quantitative', 'FTA': 'quantitative', 'FT%': 'quantitative', 'OREB': 'quantitative', 'DREB': 'quantitative',
             'REB': 'quantitative', 'AST': 'quantitative', 'PTS': 'quantitative'}

## 4. The Nominal Scale ##

nominal_scale=['Name', 'Team', 
               'Pos', 'Birth_Place', 
              'College']
nominal_scale.sort()

wnba_top_5 = wnba.head()

## 5. The Ordinal Scale ##

question1 = True
question2 = False
question3 = False 
question4 = True
question5 = False
question6 = False

## 7. The Difference Between Ratio and Interval Scales ##

interval = ['Weight_deviation', 'Birthdate']
interval.sort()

ratio = ['Weight', 'Height', 
         'Age', 'BMI',   
         'Experience', 'Games Played',
        'MIN', 'FGM', 
         'FGA', 'FG%',
        '3PA', '3P%',
        'FTM', 'FTA',
        'FT%','OREB',
        'DREB', 'REB',
        'AST', 'STL',
        'BLK', 'TO',
        'PTS', 'DD2',
        'TD3', '15:00'
        ]
ratio.sort()

top_5 = wnba.head()

print(len(top_5.columns))
print(len(ratio))
print(len(interval))

## 9. Discrete and Continuous Variables ##

ratio_interval_only = {'Height':'continuous', 'Weight': 'continuous', 'BMI': 'continuous', 'Age': 'continuous', 'Games Played': 'discrete', 'MIN': 'continuous', 'FGM': 'discrete',
                       'FGA': 'discrete', 'FG%': 'continuous', '3PA': 'discrete', '3P%': 'continuous', 'FTM': 'discrete', 'FTA': 'discrete', 'FT%': 'continuous',
                       'OREB': 'discrete', 'DREB': 'discrete', 'REB': 'discrete', 'AST': 'discrete', 'STL': 'discrete', 'BLK': 'discrete', 'TO': 'discrete',
                       'PTS': 'discrete', 'DD2': 'discrete', 'TD3': 'discrete', 'Weight_deviation': 'continuous'}

## 10. Real Limits ##

bmi = {21.201: [21.2005, 21.2015],
 21.329: [21.3285, 21.3295],
 23.875: [23.8745, 23.8755],
 24.543: [24.5425, 24.5435],
 25.469: [25.4685, 25.4695]}