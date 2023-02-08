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

## Usage
# results_2012 = results_2012.apply(teamLastWin, axis=1)

# Winning streaks
win_streak = defaultdict(int)

def winStreaks(row):
    home_team = row["homeTeam"]
    away_team = row["awayTeam"]
    row["HomeWinStreak"] = win_streak[home_team]
    row["AwayWinStreak"] = win_streak[away_team]
    #results_2012.iloc[index] = row

    if row["homeWin"]:
        win_streak[home_team] += 1
        win_streak[away_team] = 0
    else:
        win_streak[away_team] += 1
        win_streak[home_team] = 0
    return row
# Usage
# results_2012["HomeWinStreak"] = 0
# results_2012["AwayWinStreak"] = 0
# results_2012 = results_2012.apply(winStreaks, axis=1)