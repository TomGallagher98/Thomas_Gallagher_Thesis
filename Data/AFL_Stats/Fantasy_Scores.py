# Rearrange Player Names
from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select

# Lower Player names
def update_names(year):
    file_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players/Fantasy/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(file_path)
    fantasy_player_update = fantasy_scores.apply(lower_player_names, axis=1)
    fantasy_player_update.to_csv(file_path, index=False)

def lower_player_names(row):
    row[2] = row[2].lower()
    return row
    
# for year in range (2012, 2022):
#     update_names(year)

all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players"
fantasy_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players"


def change_team_names(row):
    team = row[3]
    if team == "Crows":
        row[3] = "Adelaide"
    elif team == "Lions":
        row[3] = "Brisbane Lions"
    elif team == "Blues":
        row[3] = "Carlton"
    elif team == "Magpies":
        row[3] = "Collingwood"
    elif team == "Bombers":
        row[3] = "Essendon"
    elif team == "Dockers":
        row[3] = "Fremantle"
    elif team == "Cats":
        row[3] = "Geelong"
    elif team == "Suns":
        row[3] = "Gold Coast"
    elif team == "Giants":
        row[3] = "Greater Western Sydney"
    elif team == "Hawks":
        row[3] = "Hawthorn"
    elif team == "Demons":
        row[3] = "Melbourne"
    elif team == "Kangaroos":
        row[3] = "North Melbourne"
    elif team == "Power":
        row[3] = "Port Adelaide"
    elif team == "Tigers":
        row[3] = "Richmond"
    elif team == "Saints":
        row[3] = "St Kilda"
    elif team == "Swans":  
        row[3] = "Sydney"
    elif team == "Eagles":
        row[3] = "West Coast"
    elif team == "Bulldogs":
        row[3] = "Western Bulldogs"
    return row

def rename_teams(year):
    fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(fantasy_path)
    fantasy_team_update = fantasy_scores.apply(change_team_names, axis=1)
    file_output = open(fantasy_path, "w")
    file_output.writelines("year,round,displayName,team,score\n")
    # fantasy_team_update.to_csv(fantasy_path)
    for round in fantasy_team_update.iterrows():
            out = ','.join(str(round[1][x]) for x in range(5))
            file_output.writelines(out+'\n')
    file_output.close()

# rename_teams(2012)
# rename_teams(2013)
# rename_teams(2014)
# rename_teams(2015)
# rename_teams(2016)
# rename_teams(2017)
# rename_teams(2018)
# rename_teams(2019)
# rename_teams(2020)
# rename_teams(2021)

def add_fantasy_scores(year):
    file = f"/{year}.csv" 
    round_scores = pd.read_csv(all_stats_path + file)
    fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(fantasy_path)
    round_scores = round_scores.apply(find_score_for_player, axis=1)
    
    file_out = open(all_stats_path+f'/{year}.csv', "w")
    for player in round_scores.iterrows():
            out = ','.join(str(player[1][x]) for x in range(32))
            file_out.writelines(out+'\n')
    file_out.close()

def find_score_for_player(row):
    row['Fantasy'] = 0
    year = row.year
    player = row.displayName
    team = row.team
    round = row['round']
  
    if round == "EF" or round == "QF" or round == "SF" or round == "PF" or round == "GF":
        print(round)
        return row

    round = int(round)
    fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(fantasy_path)

    round_score = fantasy_scores.query('displayName == @player & team == @team & round == @round')
    
    score = round_score.score.values
    if score.size <= 0:
        score = [0]
    row['Fantasy'] = score[0]
    return row

# add_fantasy_scores(2012)
# add_fantasy_scores(2013)
# add_fantasy_scores(2014)
# add_fantasy_scores(2015)
# add_fantasy_scores(2016)
# add_fantasy_scores(2017)
# add_fantasy_scores(2018)
# add_fantasy_scores(2019)
# add_fantasy_scores(2020)
# add_fantasy_scores(2021)