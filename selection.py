import pandas as pd 

df = pd.read_csv(r"C:\Users\PRATHAMESH\Downloads\pokemon.csv", index_col="Name")
# selection by column
#print(df["Name"].to_string)


# sekection by rows 

# print(df.loc["Togepi"])

print(df.loc["Charmander":"Pikachu",["Height","Weight","Speed"]])

# print(df)
