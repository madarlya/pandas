import pandas as pd

df = pd.read_csv(r"C:\Users\PRATHAMESH\Downloads\pokemon.csv", index_col= "Name")

pokemon = input("Enter a name of Pokemon : ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon}" " not found ")