# Add previous season ladder position
# Noted in various models that it is a useful predictor
import pandas as pd

l_2011 = [14, 15, 5, 1, 8, 11, 2, 17, 18, 3, 13, 9, 16, 12, 6, 7, 4, 10] 
l_2012 = [2, 13, 10, 4, 11, 7, 6, 17, 18, 1, 16, 8, 14, 12, 9, 3, 5, 15]
l_2013 = [11, 12, 8, 6, 9, 3, 2, 14, 18, 1, 17, 10, 7, 5, 16, 4, 13, 15]
l_2014 = [10, 15, 13, 11, 7, 4, 3, 12, 16, 2, 17, 6, 5, 8, 18, 1, 9, 14]
l_2015 = [7, 17, 18, 12, 15, 1, 10, 16, 11, 3, 13, 8, 9, 5, 14, 4, 2, 6]
l_2016 = [5, 17, 14, 12, 18, 16, 2, 15, 4, 3, 11, 8, 10, 13, 9, 1, 6, 7]
l_2017 = [1, 18, 16, 13, 7, 14, 2, 17, 4, 12, 9, 15, 5, 3, 11, 6, 8, 10]
l_2018 = [12, 15, 18, 3, 11, 14, 8, 17, 7, 4, 5, 9, 10, 1, 16, 6, 2, 13]
l_2019 = [11, 2, 16, 4, 8, 13, 1, 18, 6, 9, 17, 12, 10, 3, 14, 15, 5, 7]
l_2020 = [18, 2, 11, 8, 13, 12, 4, 14, 10, 15, 9, 17, 1, 3, 6, 16, 5, 7]
l_2021 = [15, 4, 13, 17, 8, 11, 3, 16, 7, 14, 1, 18, 2, 12, 10, 6, 9, 5]

ladder = pd.DataFrame({'team': ['Adelaide','Brisbane Lions', 'Carlton', 'Collingwood','Essendon','Fremantle',
    'Geelong', 'Gold Coast', 'Greater Western Sydney', 'Hawthorn', 'Melbourne', 'North Melbourne', 'Port Adelaide',
    'Richmond', 'St Kilda', 'Sydney', 'West Coast', 'Western Bulldogs'],
    'position': l_2011})	
ladder = ladder.set_index('team')


PATH = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Games/"
def add_ladder_position(row):
    row['homeLadderPosition'] = ladder.loc[row['homeTeam']].values[0]
    row['awayLadderPosition'] = ladder.loc[row['awayTeam']].values[0]

    return row

games_2012 = pd.read_csv(PATH + '2012.csv')
# games_2012 = games_2012.apply(add_ladder_position, axis=1)
print(ladder.sort_values(by=['position']))
