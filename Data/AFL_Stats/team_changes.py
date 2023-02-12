from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/'

stats = pd.read_csv(PATH + 'stats_sorted.csv')
games = pd.read_csv(PATH + 'games_sorted.csv')
players = pd.read_csv(PATH + 'players.csv')

all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/stats_sorted.csv"
all_stats_raw = pd.read_csv(all_stats_path)

def get_selected_team(gameId, team):
    team_l = all_stats_raw.query('gameId == @gameId and team == @team')
    return team_l
    
def team_similarity(s_team, prev_team, team):
    # Measures changes in selected team and previous team
    # HAMMING, Jaccard, Cosine (Will start with Hamming)
    selected = get_selected_team(s_team, team)
    previous_team = get_selected_team(prev_team, team)
    l1 = [x for x in selected['playerId']]
    l2 = [x for x in previous_team['playerId']]
    out_players = list(set(l1) - set(l2))
    in_players = list(set(l2) - set(l1))
    games_out = []
    games_in = []
    for player in out_players:
        p = selected.query('playerId == @player')
        games_out.append(p.gameNumber.values[0])
    for player in in_players:
        p = previous_team.query('playerId == @player')
        games_in.append(p.gameNumber.values[0])

    diff = sum(games_in) - sum(games_out)
    
    dist = (len(out_players))
    # find changed players
    return dist, diff
    # Selected team can theoretically be inputted by the user
    # For testing purposes it will be derived from the game data


def player_prev_five(player, team = None):
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