import pandas as pd

# series = A pandas 1-Dimensional labeled array that can hold any data type 
#             Think of it like a single column in a spreadsheet (1-Dimensional)

data = [100,200,300,400,500]

series = pd.Series(data, index= ["a","b","c","d","e"])

series.loc["c"]=200

print(series[series >= 200])