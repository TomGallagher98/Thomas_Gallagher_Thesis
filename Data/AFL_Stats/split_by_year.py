import pandas as pd
import time

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/'

class Season():
    def __init__(self) -> None:
        self.Players = [[] for x in range(2012,2022)]
        self.Games = [[] for x in range(2012,2022)]

    def split_into_years_inner(self, stats, type):
        print(time.time())
        for data in stats.iterrows():
            if data[1]['year'] == 2012:
                i = 0
            elif data[1]['year'] == 2013:
                i = 1
            elif data[1]['year'] == 2014:
                i = 2
            elif data[1]['year'] == 2015:
                i = 3
            elif data[1]['year'] == 2016:
                i = 4
            elif data[1]['year'] == 2017:
                i = 5
            elif data[1]['year'] == 2018:
                i = 6
            elif data[1]['year'] == 2019:
                i = 7
            elif data[1]['year'] == 2020:
                i = 8
            elif data[1]['year'] == 2021:
                i = 9
            l = self.Players[i]
            g = self.Games[i]
            if type == "player":
                l.append(data)
            else:
                g.append(data)
            
        print(time.time())

    def write_players_to_csv(self):
        header = 'gameId,team,year,round,playerId,displayName,gameNumber,Disposals,Kicks,Marks,Handballs,Goals,Behinds,Hit Outs,Tackles,Rebounds,Inside 50s,Clearances,Clangers,Frees,Frees Against,Brownlow Votes,Contested Possessions,Uncontested Possessions,Contested Marks,Marks Inside 50,One Percenters,Bounces,Goal Assists,% Played,Subs'
        fields = header.split(',')

        for playerList in self.Players:
            year = playerList[0][1]['year']
            file_output = open(PATH+'Year/Players/'+str(year)+'.csv', 'w')
            file_output.writelines(header+'\n')

            for player in playerList:
                out = ','.join(str(player[1][x]) for x in fields)
                file_output.writelines(out+'\n')
            file_output.close()
    
    def write_games_to_csv(self):
        header = 'gameId,year,round,date,venue,startTime,attendance,homeTeam,homeTeamScore,awayTeam,awayTeamScore,rainfall'
        fields = header.split(',')

        for gameList in self.Games:
            year = gameList[0][1]['year']
            file_output = open(PATH+'Year/Games/'+str(year)+'.csv', 'w')
            file_output.writelines(header+'\n')

            for player in gameList:
                out = ','.join(str(player[1][x]) for x in fields)
                file_output.writelines(out+'\n')
            file_output.close()           
        
stats = pd.read_csv(PATH + 'stats_sorted.csv')
games = pd.read_csv(PATH + 'games_sorted.csv')

def show_dtypes(df):
    for index in range(len(df.dtypes)):
        print(f'{df.columns[index]} -> {df.dtypes[index]}' )

t12 = Season()

t12.split_into_years_inner(stats, "player")
t12.split_into_years_inner(games, "games")
t12.write_players_to_csv()
t12.write_games_to_csv()