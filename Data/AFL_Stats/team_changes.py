from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select
import player_rankings as pr

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/'

stats = pd.read_csv(PATH + 'stats_sorted.csv')
games = pd.read_csv(PATH + 'games_sorted.csv')
players = pd.read_csv(PATH + 'players.csv')

all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players/stats_sorted.csv"
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
    importance_out = []
    importance_in = []
    if len(out_players) == 0:
        return 0,0,0

    for player in out_players:
        # p = selected.query('playerId == @player')
        p = selected.loc[selected['playerId'] == player]
        i = p.apply(pr.calculate_player_season_average, axis = 1).values[0]
        importance_out.append(i)
        games_out.append(p.gameNumber.values[0])
    for player in in_players:
        p = previous_team.loc[previous_team['playerId'] == player]
        i = p.apply(pr.calculate_player_season_average, axis = 1).values[0]
        
        importance_in.append(i)
        games_in.append(p.gameNumber.values[0])

    diff = sum(games_in) - sum(games_out)
    importance = (sum(importance_in)/len(importance_in)) - (sum(importance_out)/len(importance_out))
    dist = (len(out_players))
    # find changed players
  
    return dist, diff, importance
    # Selected team can theoretically be inputted by the user
    # For testing purposes it will be derived from the game data

def select_player(name, team = None):
    player = (players[(players['displayName'] == name)])
    if player.shape[0] > 1:
        for id in player['playerId']:
            p = (stats[(stats['playerId'] == id) & (stats['team'] == team)])
            if p.empty:
                pass
            else:
                player = (players[(players['playerId'] == id)])
             
                id =  player['playerId'].item()
                return id
    else:
        id =  player['playerId'].item()
        return id


    

team_similarity('2012R708', '2012R604', 'Fremantle')