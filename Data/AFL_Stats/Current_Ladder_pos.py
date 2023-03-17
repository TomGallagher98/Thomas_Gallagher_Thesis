import pandas as pd
import numpy as np
import copy

games_path = "C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Games/2012.csv"
games_raw = pd.read_csv(games_path)

# def set_ladder(season: pd.DataFrame):
#     season['homeCurrentLadderPosition'] = 0
#     season['awayCurrentLadderPosition'] = 0
    
#     return season
# team_for, against = get_all_games('Collingwood', games_2012_raw)


# def compute_ladder(row):
#     if row['round'] == 1:
#         row['homeCurrentLadderPosition'] = row['homeLadderPosition']
#         row['awayCurrentLadderPosition'] = row['awayLadderPosition']
#     return row
#         # print(row.homeLadderPosition)
# games_raw = set_ladder(games_raw)
# games_raw = games_raw.apply(compute_ladder, axis=1)
# print(games_raw)

class ladder_set():
    def __init__(self):
        self.ladders = []
    
    def get_ladder(self, round_number: int):
        if round_number >= 19:
            return self.ladders[18]
        return self.ladders[round_number-1]

    def add_ladder(self, ladder):
        self.ladders.append(ladder)

l_2012 = ladder_set()      

def ladder_builder(games):
    teams = ['Adelaide', 'Brisbane Lions','Carlton','Collingwood','Essendon','Fremantle','Geelong','Gold Coast', 'Greater Western Sydney',
         'Hawthorn','Melbourne', 'North Melbourne','Port Adelaide','Richmond','St Kilda','Sydney','West Coast','Western Bulldogs']
         
    d_init = {'team': teams,
         'for': np.zeros(18), 
         'against': np.zeros(18),
         'percentage' : np.zeros(18),
         'points': np.zeros(18)}

    ladder = pd.DataFrame(data=d_init, columns=['team', 'for','against','percentage','points'])

    l_set = ladder_set()
    l_set.add_ladder(ladder)
    
    round = [x for x in range(1, 24)]
    for r in round:
        ladder = copy.deepcopy(l_set.get_ladder(r))
        game = games.query('round == @r')
        for index, row in game.iterrows():
            ladder.loc[ladder.team == row.homeTeam, "for"] += row.homeTeamScore
            ladder.loc[ladder.team == row.homeTeam, "against"] += row.awayTeamScore
            p_for = ladder.loc[ladder.team == row.homeTeam, "for"]
            p_against = ladder.loc[ladder.team == row.homeTeam, "against"]
            ladder.loc[ladder.team == row.homeTeam, "percentage"] = (p_for / p_against) * 100

            if row.homeTeamScore > row.awayTeamScore:
                ladder.loc[ladder.team == row.homeTeam, "points"] += 4
            elif row.homeTeamScore == row.awayTeamScore:
                ladder.loc[ladder.team == row.homeTeam, "points"] += 2
            else:
                ladder.loc[ladder.team == row.awayTeam, "points"] += 4
            
            ladder.loc[ladder.team == row.awayTeam, "for"] += row.awayTeamScore
            ladder.loc[ladder.team == row.awayTeam, "against"] += row.homeTeamScore
            p_for = ladder.loc[ladder.team == row.awayTeam, "for"]
            p_against = ladder.loc[ladder.team == row.awayTeam, "against"]
            ladder.loc[ladder.team == row.awayTeam, "percentage"] = (p_for / p_against) * 100

        ladder = ladder.sort_values(['points', 'percentage'], ascending = [False,False])
        ladder = ladder.reset_index(drop=True)
        l_set.add_ladder(ladder)

    return l_set

def add_ladder_pos(games, ladders: ladder_set):
    games['homeCurrentLadderPosition'] = 0
    games['awayCurrentLadderPosition'] = 0
    home_pos = []
    away_pos = []
    for index, row in games.iterrows():
        home_team = row.homeTeam
        away_team = row.awayTeam
        r = row['round']
        ladder = ladders.get_ladder(r)
        
        if r == 1:
            home_pos.append(row.homeLadderPosition)
            away_pos.append(row.awayLadderPosition)
        else:
            home_pos.append(ladder[ladder['team'] == home_team].index[0] + 1)
            away_pos.append(ladder[ladder['team'] == away_team].index[0] + 1)
    games['homeCurrentLadderPosition'] = home_pos
    games['awayCurrentLadderPosition'] = away_pos   
    return games
        

# l = ladder_builder(games_raw)
# g = add_ladder_pos(games_raw, l)
# print(g)
for year in range(2020,2021):
    games_path = f"C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_sorted/Year/Games/{year}.csv"
    games_raw = pd.read_csv(games_path)
    l = ladder_builder(games_raw)
    games = add_ladder_pos(games_raw, l)
    games.to_csv(games_path, index=False)