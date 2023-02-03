import pandas as pd

PATH = 'C:/Users/Craig/Documents/Thesis/Thomas_Gallagher_Thesis/Data/AFL_Stats_Sorted/'



class Season():
    def __init__(self, year) -> None:
        self.Year = year
        self.stats = []

    def split_into_years(self, player_stats):
        for player in player_stats:
            print(player)
            if (player[(player['year'] == self.Year)]):
                self.stats.add(player)

    def write_to_csv(self):
        file_output = open((PATH+'Game/'+str(self.Year)+'.csv'), 'w')
        for player in self.stats:
            file_output.writelines(player)
            


stats = pd.read_csv(PATH + 'stats_sorted.csv')

def show_dtypes(df):
    for index in range(len(df.dtypes)):
        print(f'{df.columns[index]} -> {df.dtypes[index]}' )

print(stats.head(10))

print('Stats \n')
show_dtypes(stats)


t12 = Season(2012)
t12.split_into_years(stats)

