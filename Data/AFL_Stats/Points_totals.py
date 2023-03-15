import pandas as pd

def get_all_games(team: str, game_list: pd.DataFrame):
    print(type(game_list))
    games = game_list.query('homeTeam == @team or awayTeam == @team')
    
    team_scores = []
    opp_scores = []
    for index, row in games.iterrows():
        if row.homeTeam == team:
            team_scores.append(row.homeTeamScore)
            opp_scores.append(row.awayTeamScore)
        else:
            team_scores.append(row.awayTeamScore)
            opp_scores.append(row.homeTeamScore)
    return team_scores, opp_scores

def calculate_points(round: int, team_scores, opp_scores):
    if round == 1:
        return 0, 0
    team_for = sum(team_scores[:round - 1])
    team_against = sum(opp_scores[:round - 1])

    print(team_for)
    print(team_against)

def calculate_points_row(row, team, team_scores, opp_scores):
    print(row)
    if row['round'] == 1:
        return row
    if row.homeTeam == team:
        row['homeTeamPointsFor'] = sum(team_scores[:row['round'] - 1])
        row['homeTeamPointsAgainst'] =  sum(opp_scores[:row['round'] - 1])
        return row
    elif row.awayTeam == team:
        row['awayTeamPointsFor'] = sum(team_scores[:row['round'] - 1])
        row['awayTeamPointsAgainst'] =  sum(opp_scores[:row['round'] - 1])
        return row
    return row

    
    

teams = ['Hawthorn', 'Sydney']
def calc_season(season: pd.DataFrame):
    season['homeTeamPointsFor'] = 0
    season['homeTeamPointsAgainst'] = 0
    season['awayTeamPointsFor'] = 0
    season['awayTeamPointsAgainst'] = 0
    for team in teams:
        print(type(season))
        team_for, against = get_all_games(team, season)
        season = season.apply(calculate_points_row, args=(team, team_for, against), axis=1)
        print(type(season))
    print (season)
    
games_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Games/2012.csv"
games_2012_raw = pd.read_csv(games_path)

team_for, against = get_all_games('Collingwood', games_2012_raw)

calculate_points(5, team_for, against)

calc_season(games_2012_raw)