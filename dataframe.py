import pandas as pd 

# Database = A tabular data structred with rows and columns . (2-Dimensional)
#             similar to an Excel spreadsheet

data = {
    "Name":["Prathamesh","Ganesh","Ramesh","Santosh"],
    "Age":[19,21,18,17]
    }

df = pd.DataFrame(data,index=["Student 1","Student 2", "Student 3", "Student 4"])

# Add new column

df["Sub"] = ["Ai/Ml", "Python","Java","N/A"]

# Add a bew Row

New_Row = pd.DataFrame([{"Name": "tejas", "Age" : 21 , "Sub": "db"}],
                       index=["Student 5"])
df = pd.concat([df,New_Row])
print(df)

