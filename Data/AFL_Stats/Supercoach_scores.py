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
    supercoach_path = f"/content/drive/MyDrive/Supercoach/supercoach_{year}.csv"
    supercoach_scores = pd.read_csv(supercoach_path)
    supercoach_team_update = supercoach_scores.apply(change_team_names, axis=1)
    file_output = open(supercoach_path, "w")
    file_output.writelines("year,round,displayName,team,score\n")
    # supercoach_team_update.to_csv(supercoach_path)
    for round in supercoach_team_update.iterrows():
            out = ','.join(str(round[1][x]) for x in range(5))
            file_output.writelines(out+'\n')
    file_output.close()
rename_teams(2021)