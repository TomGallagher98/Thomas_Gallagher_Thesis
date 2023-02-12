## Eventually use average of players SC and DT
from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select
from team_changes import get_selected_team

all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/stats_sorted.csv"
all_stats_raw = pd.read_csv(all_stats_path)
games_filename_2012 = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players/2012.csv"
stats_2012 = pd.read_csv(games_filename_2012)
# Kick 4
# Handball 2
# Mark 3
# Goal 6
# Behind 1
# Hitout 2
# Tackles 3
# Rebounds 1
# Inside 50s 2
# Clearances 3
# Clangers -3
# Free Against -3
# Contested Marks 3
# One Percenters 3
# Goal Assist 2

def get_previous_game(playerId, round):
    round = str(round)
    l = stats_2012.query('round < @round and playerId == @playerId')
    if len(l) > 0:
        # print(l.values[-1])
        return l.iloc[-1]
    return pd.Series(dtype='float64')

def calculate_team(gameId, team):
    team_list = get_selected_team(gameId, team)
    player_scores = []
    player_scores.append(team_list.apply(calculate_player_score, axis =1).values)
    # for player in team_list:
    #     pre = get_previous_game(player.playerId, player.round)
    #     player_scores.append(calculate_player_score(pre))
    print(sum(player_scores[0]))
    return sum(player_scores)

def calculate_player_score(player):
    prev_game = get_previous_game(player.playerId, player.round)
    if prev_game.empty:
        return 0
    stat_list = []
    stat_list.append(prev_game.Kicks * 4)
    stat_list.append(prev_game.Handballs * 2)
    stat_list.append(prev_game.Marks * 3)
    stat_list.append(prev_game.Goals * 6)
    stat_list.append(prev_game.Behinds)
    stat_list.append(prev_game.HitOuts * 2)
    stat_list.append(prev_game.Tackles * 3)
    stat_list.append(prev_game.Rebounds)
    stat_list.append(prev_game.Inside50s * 2)
    stat_list.append(prev_game.Clearances * 3)
    stat_list.append(prev_game.Clangers * -3)
    stat_list.append(prev_game.FreesAgainst * -3)
    stat_list.append(prev_game.ContestedMarks * 3)
    stat_list.append(prev_game.OnePercenters * 3)
    stat_list.append(prev_game.GoalAssists * 2)

    print(sum(stat_list))
    return sum(stat_list)
    


calculate_team("2015R2201", "Collingwood")