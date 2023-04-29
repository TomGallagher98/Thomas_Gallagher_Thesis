# Rearrange Player Names
import pandas as pd

def find_different_names():
    all_names = []
    all_sc_names = []
    for year in range(2012, 2022):
        file_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players/{year}.csv"
        fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players/Fantasy/fantasy_{year}.csv"
        sc = pd.read_csv(fantasy_path, index_col=False)
        n = pd.read_csv(file_path, index_col=False)
        sc_names = sc.player.unique()
        sc_names = [x.lower() for x in sc_names]
        names = n.displayName.unique()
        names = [x.lower() for x in names]

        missing = [item for item in names if item not in sc_names]
        missing_sc = [item for item in sc_names if item not in names]

        all_names += [item for item in missing if item not in all_names]
        all_sc_names += [x for x in missing_sc if x not in all_sc_names]
      
    return all_names, all_sc_names
    
different_names = find_different_names()[0]
different_sc_names = find_different_names()[1]
def fix_name(name):
    for n in different_names:
        l = n.split()
        last = name.split()
        if last[1] == l[1]:
            if last[0][0] == l[0][0]:
                return n

# Lower Player names
def update_names(year):
    file_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players/Fantasy/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(file_path)
    fantasy_player_update = fantasy_scores.apply(lower_player_names, axis=1)
    fantasy_player_update.to_csv(file_path, index=False)

def lower_player_names(row):
    name = row[2].lower()
    if name.find('injured') != -1:
        n = name.split()
        n.remove('injured')
        n = ' '.join(n)
        row[2] = n
        name = n
    if name.find("'") != -1:
        name = name.replace("'","")
        row[2]=name
    row[2] = row[2].lower()
    if name == "angus dewar":
        row[2] = "angus litherland"
    if name == "mitchell white":
        row[2] = "mitch white"
    if name == "matthew white":
        row[2] = "matthew white"
    if name == "jay kennedy-harris":
        row[2] = "jay kennedy harris"
    if name == "josh deluca-cardillo":
        row[2] = "josh deluca"
    if name == "joshua kennedy":
        row[2] = "josh kennedy"
    if name in different_sc_names:
        f = fix_name(name)
        row[2] = f
    return row

for year in range (2012, 2022):
    update_names(year)

all_stats_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players"
fantasy_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players"

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
    fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players/Fantasy/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(fantasy_path)
    fantasy_team_update = fantasy_scores.apply(change_team_names, axis=1)
    fantasy_team_update.to_csv(fantasy_path, index=False)

for year in range (2012, 2022):
    rename_teams(year)

def add_fantasy_scores(year):
    file = f"/{year}.csv" 
    round_scores = pd.read_csv(all_stats_path + file)
    fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players/Fantasy/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(fantasy_path)
    round_scores = round_scores.apply(find_score_for_player, axis=1)
    round_scores.to_csv(all_stats_path+f'/{year}.csv', index=False)

def find_score_for_player(row):
    row['Fantasy'] = 0
    year = row.year
    player = (row.displayName).lower()
    team = row.team
    round = row['round']
    if round == "EF" or round == "QF" or round == "SF" or round == "PF" or round == "GF":
        print(round)
        return row

    round = int(round)
    fantasy_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/Year/Players/Fantasy/fantasy_{year}.csv"
    fantasy_scores = pd.read_csv(fantasy_path)
    
    round_score = fantasy_scores.query('player == @player & team == @team & round == @round')
    
    score = round_score.score.values
    if score.size <= 0:
        score = [0]
    row['Fantasy'] = score[0]
    return row

for year in range(2012, 2022):
    add_fantasy_scores(year)