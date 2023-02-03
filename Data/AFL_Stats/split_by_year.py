import pandas as pd
import time

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/'



class Season():
    def __init__(self, year) -> None:
        self.Year = year
        self.stats = []

    def split_into_years(self, player_stats):
        print(time.time())
        for player in player_stats.iterrows():
            if player[1]['year'] == self.Year:
                self.stats.append(player)
            
        print(time.time())

    def write_to_csv(self):
        file_output = open((PATH+'Year/Players/'+str(self.Year)+'.csv'), 'w')
        header = 'gameId,team,year,round,playerId,displayName,gameNumber,Disposals,Kicks,Marks,Handballs,Goals,Behinds,Hit Outs,Tackles,Rebounds,Inside 50s,Clearances,Clangers,Frees,Frees Against,Brownlow Votes,Contested Possessions,Uncontested Possessions,Contested Marks,Marks Inside 50,One Percenters,Bounces,Goal Assists,% Played,Subs'
        file_output.writelines(header+'\n')
        
        fields = header.split(',')
        for player in self.stats:
            out = ','.join(str(player[1][x]) for x in fields)
            file_output.writelines(out+'\n')

            
            


stats = pd.read_csv(PATH + 'stats_sorted.csv')

def show_dtypes(df):
    for index in range(len(df.dtypes)):
        print(f'{df.columns[index]} -> {df.dtypes[index]}' )

# print(stats.head(10))

# print('Stats \n')
# show_dtypes(stats)


t12 = Season(2012)
t12.split_into_years(stats)
t12.write_to_csv()

t13 = Season(2013)
t13.split_into_years(stats)
t13.write_to_csv()

t14 = Season(2014)
t14.split_into_years(stats)
t14.write_to_csv()

t15 = Season(2015)
t15.split_into_years(stats)
t15.write_to_csv()

t16 = Season(2016)
t16.split_into_years(stats)
t16.write_to_csv()

t17 = Season(2017)
t17.split_into_years(stats)
t17.write_to_csv()

t18 = Season(2018)
t18.split_into_years(stats)
t18.write_to_csv()

t19 = Season(2019)
t19.split_into_years(stats)
t19.write_to_csv()

t20 = Season(2020)
t20.split_into_years(stats)
t20.write_to_csv()

t21 = Season(2021)
t21.split_into_years(stats)
t21.write_to_csv()