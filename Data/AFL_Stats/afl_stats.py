import csv
from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/'

stats = pd.read_csv(PATH + 'stats_sorted.csv')
games = pd.read_csv(PATH + 'games_sorted.csv')
players = pd.read_csv(PATH + 'players.csv')
# print(stats.describe())

def show_dtypes(df):
    for index in range(len(df.dtypes)):
        print(f'{df.columns[index]} -> {df.dtypes[index]}' )

# print(stats.head(10))

# print('Stats \n')
# show_dtypes(stats)
# print('\nPlayers')
# show_dtypes(players)
# print('\nGames')
# show_dtypes(games)

def select_player(name, team = None):
    
    player = (players[(players['displayName'] == name)])
    if player.shape[0] > 1:
        for id in player['playerId']:
            p = (stats[(stats['playerId'] == id) & (stats['team'] == team)])
            if p.empty:
                pass
            else:
                player = (players[(players['playerId'] == id)])
                print(player)
                id =  player['playerId'].item()
                return id
    else:
        print(player)
        id =  player['playerId'].item()
        return id
            
def print_team(gameId, team):
    # join using & https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/
    players = (stats[(stats['gameId'] == gameId) & (stats['team'] == team)])
    return (players)


# print(players.iloc[[1]])
# print (select_player('Kennedy, Josh', 'Sydney'))
# print_team('R15', 'Collingwood', 2019)

def select_prev_five(player, team = None):
    #get stats from players previous 5 games
    # pd.set_option('display.max_columns', None)
    id = select_player(player, team)
    print(id)
    l_five = stats[(stats['playerId'] == id)]
    return l_five.tail(5)

def team_prev_five(team):
    prev_games = games[(games['homeTeam'] == team) | (games['awayTeam'] == team)]
    prev_games = prev_games.tail(5)
    ids = [x for x in prev_games['gameId']]
    print (ids)

def team_similarity(s_team, prev_team, team):
    # Measures changes in selected team and previous team 
    # HAMMING, Jaccard, Cosine (Will start with Hamming)
    selected = print_team(s_team, team)
    previous_team = print_team(prev_team, team)
    l1 = [x for x in selected['playerId']]
    l2 = [x for x in previous_team['playerId']]
    dist = 0
    for x in l1:
        if x in l2:
            continue
        else:
            dist += 1

    print(dist)
    
def team_travel(team, next_venue):
    # Measures distance travelled between games
    prev_games = games[(games['homeTeam'] == team) | (games['awayTeam'] == team)]
    last_game = prev_games.tail(1)
    last_venue = last_game['venue']
    pass

venues_raw = {'VIC': [0,2,2,2,5,2,3,4,3,6], 
              'NSW': [2,0,3,1,5,2,2,4,3,6],
              'TAS': [2,3,0,1,5,2,4,5,3,6],
              'ACT': [2,1,2,0,5,2,2,4,3,6],
               'WA': [5,5,5,5,0,4,5,4,5,6],
               'SA': [2,2,2,2,4,0,3,3,4,6],
              'QLD': [3,2,4,2,5,3,0,3,4,6],
               'NT': [4,4,5,4,4,3,3,0,5,6],
               'NZ': [3,3,3,3,5,5,4,5,0,6],
              'CHI': [6,6,6,6,6,6,6,6,6,0]}
Venues = pd.DataFrame(data=venues_raw)
Venues.index = ['VIC', 'NSW', 'TAS', 'ACT', 'WA', 'SA', 'QLD', 'NT', 'NZ', 'CHI']

class Venue():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    """    	VIC	NSW	TAS	ACT	WA	SA	QLD	NT	NZ	CHI
    VIC	    0	2	2	2	4	2	3	4	3	6
    NSW	    2	0	3	1	4	2	2	4	3	6
    TAS	    2	3	0	2	4	2	4	5	3	6
    ACT	    2	1	2	0	4	2	2	4	3	6
    WA	    4	4	4	4	0	3	4	3	5	6
    SA	    2	2	2	2	3	0	3	3	4	6
    QLD	    3	2	4	2	4	3	0	3	4	6
    NT	    4	4	5	4	3	3	3	0	5	6
    NZ	    3	3	3	3	5	5	4	5	0	6
    CHI	    6	6	6	6	6	6	6	6	6	0
    """
    
    def distance(self, next_venue):
        if self.location == 'MEL':
            if next_venue.location == 'MEL':
                dist = 0
            elif (next_venue.location == 'BAL' | next_venue.location == 'GEE'):
                dist = 1
            elif (next_venue.location == 'HOB'| next_venue.location == 'LAU' 
                | next_venue.location == 'SYD' | next_venue.location == 'ADE'):
                dist = 2
            elif (next_venue.location == 'PER' | next_venue.location == 'ALI' 
                | next_venue.location == 'DAR' | next_venue.location == 'BRI'):
                dist = 3
            else:
                dist = 4

def break_len(team):
    # Finds break between previous game and game being played
    pass

def selected_team():
    # Selected team will be inputted by the user
    pass

# print(select_prev_five('Sidebottom, Steele'))
# team_prev_five('Collingwood')
# team_similarity('2021R2308', '2021R2205', 'Collingwood')
print(Venues)