import pandas as pd
filename = './befkbhalderstatkode.csv'

bef_stats_df = pd.read_csv(filename)
dd = bef_stats_df.as_matrix()

mask = (dd[: , 0] == 1998)
print(dd[mask])