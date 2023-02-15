## Eventually use average of players SC and DT but I need to scrape the data from a different site 
# and append it to the current dataset
from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select
# from team_changes import get_selected_team

all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/stats_sorted.csv"
all_stats_raw = pd.read_csv(all_stats_path)
games_filename_2012 = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players/2012.csv"
supercoach_2012 = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players/Supercoach/supercoach_2012.csv"
stats_2012 = pd.read_csv(games_filename_2012)
supercoach_2012 = pd.read_csv(supercoach_2012)
print(stats_2012.Supercoach.value_counts(sort=True))

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

def get_previous_games(playerId, round):
    round = str(round)
    l = stats_2012.query('round < @round and playerId == @playerId')
    if len(l) > 0:
        return l
    return pd.Series(dtype='float64')

def calculate_team_previous_game(gameId, team):
    # Looks only at each selected players previous game, returns team total and average
    team_list = get_selected_team(gameId, team)
    player_scores = []
    player_scores.append(team_list.apply(calculate_player_score, axis =1).values)
    # for player in team_list:
    #     pre = get_previous_game(player.playerId, player.round)
    #     player_scores.append(calculate_player_score(pre))
    return sum(player_scores)/len(player_scores)

def calculate_team_previous_five(gameId, team):
    # Looks at each selected players previous 5 games, returns average
    team_list = get_selected_team(gameId, team)
    player_scores = []
    player_scores = team_list.apply(calculate_player_previous_five, axis =1).values
    print(sum(player_scores)/len(player_scores))
    return sum(player_scores), sum(player_scores)/len(player_scores)

def calculate_team_player_average(gameId, team):
    # Looks at each selected players season average, returns average
    team_list = get_selected_team(gameId, team)
    player_scores = []
    player_scores = team_list.apply(calculate_player_season_average, axis =1).values
    print(sum(player_scores)/len(player_scores))
    return sum(player_scores), sum(player_scores)/len(player_scores)

def calculate_player_score(player):
    season_games = get_previous_games(player.playerId, player.round)
    if season_games.empty:
        return 0
    season_games = season_games.iloc[-1]
    stat_list = []
    stat_list.append(season_games.Kicks * 4)
    stat_list.append(season_games.Handballs * 2)
    stat_list.append(season_games.Marks * 3)
    stat_list.append(season_games.Goals * 6)
    stat_list.append(season_games.Behinds)
    stat_list.append(season_games.HitOuts * 2)
    stat_list.append(season_games.Tackles * 3)
    stat_list.append(season_games.Rebounds)
    stat_list.append(season_games.Inside50s * 2)
    stat_list.append(season_games.Clearances * 3)
    stat_list.append(season_games.Clangers * -3)
    stat_list.append(season_games.FreesAgainst * -3)
    stat_list.append(season_games.ContestedMarks * 3)
    stat_list.append(season_games.OnePercenters * 3)
    stat_list.append(season_games.GoalAssists * 2)

    return sum(stat_list)
    
def calculate_player_previous_five(player):
    season_games = get_previous_games(player.playerId, player.round)
    if season_games.empty:
        return 0

    stat_list = []
    i = len(season_games)
    if i >= 5:
        season_games = season_games.tail(5)
        i = 5
    for j in range(i):
        game = []
        game.append(season_games.iloc[j].Kicks * 4)
        game.append(season_games.iloc[j].Handballs * 2)
        game.append(season_games.iloc[j].Marks * 3)
        game.append(season_games.iloc[j].Goals * 6)
        game.append(season_games.iloc[j].Behinds)
        game.append(season_games.iloc[j].HitOuts * 2)
        game.append(season_games.iloc[j].Tackles * 3)
        game.append(season_games.iloc[j].Rebounds)
        game.append(season_games.iloc[j].Inside50s * 2)
        game.append(season_games.iloc[j].Clearances * 3)
        game.append(season_games.iloc[j].Clangers * -3)
        game.append(season_games.iloc[j].FreesAgainst * -3)
        game.append(season_games.iloc[j].ContestedMarks * 3)
        game.append(season_games.iloc[j].OnePercenters * 3)
        game.append(season_games.iloc[j].GoalAssists * 2)
        stat_list.append(sum(game))

    # print(sum(stat_list)/len(stat_list))
    return sum(stat_list)/len(stat_list)

def calculate_player_season_average(player):
    season_games = get_previous_games(player.playerId, player.round)
    if season_games.empty:
        return 0

    stat_list = []
    i = len(season_games)

    for j in range(i):
        game = []
        game.append(season_games.iloc[j].Kicks * 4)
        game.append(season_games.iloc[j].Handballs * 2)
        game.append(season_games.iloc[j].Marks * 3)
        game.append(season_games.iloc[j].Goals * 6)
        game.append(season_games.iloc[j].Behinds)
        game.append(season_games.iloc[j].HitOuts * 2)
        game.append(season_games.iloc[j].Tackles * 3)
        game.append(season_games.iloc[j].Rebounds)
        game.append(season_games.iloc[j].Inside50s * 2)
        game.append(season_games.iloc[j].Clearances * 3)
        game.append(season_games.iloc[j].Clangers * -3)
        game.append(season_games.iloc[j].FreesAgainst * -3)
        game.append(season_games.iloc[j].ContestedMarks * 3)
        game.append(season_games.iloc[j].OnePercenters * 3)
        game.append(season_games.iloc[j].GoalAssists * 2)
        stat_list.append(sum(game))

    return sum(stat_list)/len(stat_list)

# calculate_team_previous_game("2012R2205", "Collingwood")
# calculate_team_previous_five("2012R2205", "West Coast")
# calculate_team_player_average("2012R2205", "West Coast")