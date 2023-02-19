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
    '2012': l_2011,
    '2013': l_2012,
    '2014': l_2013,
    '2015': l_2014,
    '2016': l_2015,
    '2017': l_2016,
    '2018': l_2017,
    '2019': l_2018,
    '2020': l_2019,
    '2021': l_2020})	
ladder = ladder.set_index('team')


PATH = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Games/"
def add_ladder_position(row):
    year = str(row['year'])
    row['homeLadderPosition'] = ladder[year].loc[row['homeTeam']]
    row['awayLadderPosition'] = ladder[year].loc[row['awayTeam']]

    return row

games_2012 = pd.read_csv(PATH + '2012.csv')
games_2012 = games_2012.apply(add_ladder_position, axis=1)
games_2012.to_csv(PATH + '2012.csv', index=False)
games_2013 = pd.read_csv(PATH + '2013.csv')
games_2013 = games_2013.apply(add_ladder_position, axis=1)
games_2013.to_csv(PATH + '2013.csv', index=False)
games_2014 = pd.read_csv(PATH + '2014.csv')
games_2014 = games_2014.apply(add_ladder_position, axis=1)
games_2014.to_csv(PATH + '2014.csv', index=False)
games_2015 = pd.read_csv(PATH + '2015.csv')
games_2015 = games_2015.apply(add_ladder_position, axis=1)
games_2015.to_csv(PATH + '2015.csv', index=False)
games_2016 = pd.read_csv(PATH + '2016.csv')
games_2016 = games_2016.apply(add_ladder_position, axis=1)
games_2016.to_csv(PATH + '2016.csv', index=False)
games_2017 = pd.read_csv(PATH + '2017.csv')
games_2017 = games_2017.apply(add_ladder_position, axis=1)
games_2017.to_csv(PATH + '2017.csv', index=False)
games_2018 = pd.read_csv(PATH + '2018.csv')
games_2018 = games_2018.apply(add_ladder_position, axis=1)
games_2018.to_csv(PATH + '2018.csv', index=False)
games_2019 = pd.read_csv(PATH + '2019.csv')
games_2019 = games_2019.apply(add_ladder_position, axis=1)
games_2019.to_csv(PATH + '2019.csv', index=False)
games_2020 = pd.read_csv(PATH + '2020.csv')
games_2020 = games_2020.apply(add_ladder_position, axis=1)
games_2020.to_csv(PATH + '2020.csv', index=False)
games_2021 = pd.read_csv(PATH + '2021.csv')
games_2021 = games_2021.apply(add_ladder_position, axis=1)
games_2021.to_csv(PATH + '2021.csv', index=False)

