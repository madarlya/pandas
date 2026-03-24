import pandas as pd

calories = {"Day 1" : 1750 , "Day 2" : 1530 , "Day 3" : 1540 , "Day 4" : 1790 , "Day 5" : 1940 }
series = pd.Series(calories)
print(series)
series.loc["Day 1"] += 300
print(series.loc['Day 1'])
print(series[series >= 2000])

