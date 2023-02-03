import pandas as pd
import time

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/'



class Season():
    def __init__(self, year) -> None:
        self.Year = year
        self.players = []
        self.games = []
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

    def split_into_years(self, stats, type):
        print(time.time())
        for data in stats.iterrows():
            if data[1]['year'] == self.Year:
                if type == "player":
                    self.players.append(data)
                else:
                    self.games.append(data)
            
        print(time.time())

    def write_player_to_csv(self):
        file_output = open(PATH+'Year/Players/'+str(self.Year)+'test.csv', 'w')
        header = 'gameId,team,year,round,playerId,displayName,gameNumber,Disposals,Kicks,Marks,Handballs,Goals,Behinds,Hit Outs,Tackles,Rebounds,Inside 50s,Clearances,Clangers,Frees,Frees Against,Brownlow Votes,Contested Possessions,Uncontested Possessions,Contested Marks,Marks Inside 50,One Percenters,Bounces,Goal Assists,% Played,Subs'
        file_output.writelines(header+'\n')
        
        fields = header.split(',')
        for player in self.Players[0]:
            out = ','.join(str(player[1][x]) for x in fields)
            file_output.writelines(out+'\n')

    def write_game_to_csv(self):
        file_output = open(PATH+'Year/Games/'+str(self.Year)+'.csv', 'w')
        header = 'gameId,year,round,date,venue,startTime,attendance,homeTeam,homeTeamScore,awayTeam,awayTeamScore,rainfall'
        file_output.writelines(header+'\n')
        
        fields = header.split(',')
        for player in self.games:
            out = ','.join(str(player[1][x]) for x in fields)
            file_output.writelines(out+'\n')

            
        
stats = pd.read_csv(PATH + 'stats_sorted.csv')
games = pd.read_csv(PATH + 'games_sorted.csv')

def show_dtypes(df):
    for index in range(len(df.dtypes)):
        print(f'{df.columns[index]} -> {df.dtypes[index]}' )


t12 = Season(2012)
# t12.split_into_years(stats, "player")
# t12.write_player_to_csv()

t12.split_into_years_inner(stats, "player")
t12.write_players_to_csv()
t12.write_games_to_csv()
t13 = Season(2013)
t13.split_into_years(stats, "player")
t13.write_player_to_csv()

t14 = Season(2014)
t14.split_into_years(stats, "player")
t14.write_player_to_csv()

t15 = Season(2015)
t15.split_into_years(stats, "player")
t15.write_player_to_csv()

t16 = Season(2016)
t16.split_into_years(stats, "player")
t16.write_player_to_csv()

t17 = Season(2017)
t17.split_into_years(stats, "player")
t17.write_player_to_csv()

t18 = Season(2018)
t18.split_into_years(stats, "player")
t18.write_player_to_csv()

t19 = Season(2019)
t19.split_into_years(stats, "player")
t19.write_player_to_csv()

t20 = Season(2020)
t20.split_into_years(stats, "player")
t20.write_player_to_csv()

t21 = Season(2021)
t21.split_into_years(stats, "player")
t21.write_player_to_csv()