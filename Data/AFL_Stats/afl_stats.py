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
    # Assumed all teams will leave from home state
    if team == 'Geelong' & next_venue == 'Kardinia Park':
        return 0
    team_location = find_team_loaction(team)
    if team == 'Brisbane' & next_venue == 'Gabba':
        return 0
    if team == 'Gold Coast' & next_venue == 'Carrara':
        return 0
    venue_location = find_venue_location(next_venue)

    get_distance(team_location, venue_location)
    # Geelong = 0 if next_venue is Kardinia Park else loc = MEL
    # Brisbane = 0 for Gabba else QLD
    # Gold Coast = 0 for Carrara else QLD

    # Geelong, Brisbane and Gold Coast are all unique with home grounds
    

def find_team_loaction(team):
    melbourneTeams = ['Carlton', 'Collingwood','Essendon','Hawthorn','Melbourne',
    'North Melbourne','Richmond','StKilda','WesternBulldogs']
    sydneyTeams = ['Greater Western Sydney','Sydney']
    adelaideTeams = ['Adelaide','Port Adelaide']
    perthTeams = ['Fremantle','West Coast Eagles']
    if team in melbourneTeams:
        return "MEL"
    if team in sydneyTeams:
        return "SYD"
    if team in adelaideTeams:
        return "ADE"
    if team in perthTeams:
        return "PER"
    if team == 'Geelong':
        return 'GEE'
    else:
        return team
    

def find_venue_location(venue):
    VenueList = {
        "CH" : ['Jiangwan Stadium'],    
        "MEL" : ['M.C.G.', 'Docklands'],
        "VIC" : ['Kardinia Park', 'Eureka Stadium'],
        "SYD" : ['Blacktown', 'S.C.G.', 'Stadium Australia', 'Sydney Showground'],
        "QLD" : ["Cazaly's Stadium",  'Riverway Stadium', 'Carrara', 'Gabba'],
        "NT" : ['Marrara Oval', 'Traeger Park' ],
        "SA" : ['Adelaide Oval', 'Football Park'],
        "WA" : ['Perth Stadium',  'Subiaco'],
        "ACT" : [ 'Manuka Oval' ],
        "TAS" : ['Bellerive Oval', 'Bellerive Oval'],
        "NZ" :  ['Wellington'] 
    }
    for key, value in VenueList.items():
        if venue in value:
            return key

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

def get_distance(team, next_venue):
    if next_venue == 'CHI':
        return 5
    if team == 'MEL':
        if next_venue == 'MEL':
            dist = 0
        elif (next_venue == 'VIC'):
            dist = 1
        elif (next_venue == 'TAS'| next_venue == 'SYD' 
            | next_venue == 'ACT' | next_venue == 'SA'):
            dist = 2
        elif (next_venue == 'WA' | next_venue == 'NZ' 
            | next_venue == 'QLD'):
            dist = 3
        else:
            dist = 4

    if team == 'GEE':
        if next_venue == 'GEE':
            dist = 0
        elif (next_venue == 'VIC' | next_venue == 'MEL'):
            dist = 1
        elif (next_venue == 'TAS'| next_venue == 'SYD' 
            | next_venue == 'ACT' | next_venue == 'SA'):
            dist = 2
        elif (next_venue == 'WA' | next_venue == 'NZ' 
            | next_venue == 'QLD'):
            dist = 3
        else:
            dist = 4
    
    if team == 'SYD':
        if next_venue == 'SYD':
            dist = 0
        elif (next_venue == 'ACT'):
            dist = 1
        elif (next_venue == 'SA'| next_venue == 'VIC' 
            | next_venue == 'QLD'| next_venue == 'MEL'):
            dist = 2
        elif (next_venue == 'TAS' | next_venue == 'NZ'
            | next_venue == 'NT' ):
            dist = 3
        else:
            dist = 4
    
    if team == 'ADE':
        if next_venue == 'SA':
            dist = 0
        elif (next_venue == 'VIC'| next_venue == 'SYD' 
            | next_venue == 'ACT' | next_venue == 'TAS'
            | next_venue == 'MEL'):
            dist = 2
        elif (next_venue == 'QLD' | next_venue == 'WA' 
            | next_venue == 'NT'):
            dist = 3
        else:
            dist = 4
    
    if team == 'QLD':
        if next_venue == 'QLD':
            dist = 1
        elif (next_venue == 'SYD' | next_venue == 'ACT'):
            dist = 2
        elif (next_venue == 'VIC' | next_venue == 'MEL' 
            | next_venue == 'NT' | next_venue == 'SA'):
            dist = 3
        else:
            dist = 4

    if team == 'PER':
        if next_venue == 'WA':
            dist = 0
        elif (next_venue == 'SA' | next_venue == 'NT'):
            dist = 3
        else:
            dist = 4
    
    return dist

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
            elif (next_venue.location == 'VIC'):
                dist = 1
            elif (next_venue.location == 'TAS'| next_venue.location == 'SYD' 
                | next_venue.location == 'ACT' | next_venue.location == 'SA'):
                dist = 2
            elif (next_venue.location == 'WA' | next_venue.location == 'NZ' 
                | next_venue.location == 'QLD'):
                dist = 3
            else:
                dist = 4

        if self.location == 'GEE':
            if next_venue.location == 'GEE':
                dist = 0
            elif (next_venue.location == 'VIC' | next_venue.location == 'MEL'):
                dist = 1
            elif (next_venue.location == 'TAS'| next_venue.location == 'SYD' 
                | next_venue.location == 'ACT' | next_venue.location == 'SA'):
                dist = 2
            elif (next_venue.location == 'WA' | next_venue.location == 'NZ' 
                | next_venue.location == 'QLD'):
                dist = 3
            else:
                dist = 4
        
        if self.location == 'SYD':
            if next_venue.location == 'SYD':
                dist = 0
            elif (next_venue.location == 'ACT'):
                dist = 1
            elif (next_venue.location == 'SA'| next_venue.location == 'VIC' 
                | next_venue.location == 'QLD'| next_venue.location == 'MEL'):
                dist = 2
            elif (next_venue.location == 'TAS' | next_venue.location == 'NZ'
                | next_venue.location == 'NT' ):
                dist = 3
            else:
                dist = 4
        
        if self.location == 'ADE':
            if next_venue.location == 'SA':
                dist = 0
            elif (next_venue.location == 'VIC'| next_venue.location == 'SYD' 
                | next_venue.location == 'ACT' | next_venue.location == 'TAS'
                | next_venue.location == 'MEL'):
                dist = 2
            elif (next_venue.location == 'QLD' | next_venue.location == 'WA' 
                | next_venue.location == 'NT'):
                dist = 3
            else:
                dist = 4
        
        if self.location == 'QLD':
            if next_venue.location == 'QLD':
                dist = 1
            elif (next_venue.location == 'SYD' | next_venue.location == 'ACT'):
                dist = 2
            elif (next_venue.location == 'VIC' | next_venue.location == 'MEL' 
                | next_venue.location == 'NT' | next_venue.location == 'SA'):
                dist = 3
            else:
                dist = 4

        if self.location == 'PER':
            if next_venue.location == 'WA':
                dist = 0
            elif (next_venue.location == 'SA' | next_venue.location == 'NT'):
                dist = 3
            else:
                dist = 4
        
        return dist

def break_len(team):
    # Finds break between previous game and game being played
    pass

def selected_team():
    # Selected team will be inputted by the user
    pass

# print(select_prev_five('Sidebottom, Steele'))
# team_prev_five('Collingwood')
# team_similarity('2021R2308', '2021R2205', 'Collingwood')
# print(Venues)