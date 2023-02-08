from collections import defaultdict
won_last = defaultdict(bool)

def teamLastWin(row):
    home_team = row["homeTeam"]
    away_team = row["awayTeam"]
    row["homeTeamLastWin"] = won_last[home_team]
    row["awayTeamLastWin"] = won_last[away_team]
    
    won_last[home_team] = row["homeWin"]
    won_last[away_team] = not row["homeWin"]
    
    return row