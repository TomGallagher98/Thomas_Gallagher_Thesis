# Rearrange Player Names
from unicodedata import name
import pandas as pd
from scipy.__config__ import show
from soupsieve import select

# all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players"

# file_out_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Players/supercoach_2012.csv"
# year = 2012
# file_output = open(file_out_path, 'w')
# for i in range(1,24):
#     file = f"/supercoach_round{i}_{year}.csv" 
#     round_scores = pd.read_csv(all_stats_path + file)

#     for round in round_scores.iterrows():
#         out = ','.join(str(round[1][x]) for x in range(5))
#         file_output.writelines(out+'\n')
# file_output.close()
all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players"
supercoach_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players"


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
    supercoach_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players/supercoach_{year}.csv"
    supercoach_scores = pd.read_csv(supercoach_path)
    supercoach_team_update = supercoach_scores.apply(change_team_names, axis=1)
    file_output = open(supercoach_path, "w")
    file_output.writelines("year,round,displayName,team,score\n")
    # supercoach_team_update.to_csv(supercoach_path)
    for round in supercoach_team_update.iterrows():
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

def add_supercoach_scores(year):
    file = f"/{year}.csv" 
    round_scores = pd.read_csv(all_stats_path + file)
    supercoach_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players/supercoach_{year}.csv"
    supercoach_scores = pd.read_csv(supercoach_path)
    round_scores = round_scores.apply(find_score_for_player, axis=1)
    
    file_out = open(all_stats_path+f'/{year}.csv', "w")
    for player in round_scores.iterrows():
            out = ','.join(str(player[1][x]) for x in range(32))
            file_out.writelines(out+'\n')
    file_out.close()

def find_score_for_player(row):
    row['supercoach'] = 0
    year = row.year
    player = row.displayName
    team = row.team
    round = row['round']

    print([year, player, team, round])

  
    if round == "EF" or round == "QF" or round == "SF" or round == "PF" or round == "GF":
        print(round)
        return row

    round = int(round)
    supercoach_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats/Year/Players/supercoach_{year}.csv"
    supercoach_scores = pd.read_csv(supercoach_path)
    print([round_score.displayName, round_score.team, round_score['round']])
    round_score = supercoach_scores.query('displayName == @player & team == @team & round == @round')
    
    score = round_score.score.values
    if score.size <= 0:
        score = [0]
    row['supercoach'] = score[0]
    return row

add_supercoach_scores(2012)
# add_supercoach_scores(2013)
# add_supercoach_scores(2014)
# add_supercoach_scores(2015)
# add_supercoach_scores(2016)
# add_supercoach_scores(2017)
# add_supercoach_scores(2018)
# add_supercoach_scores(2019)
# add_supercoach_scores(2020)
# add_supercoach_scores(2021)