import pandas as pd

# load data and assign
surveys_df = pd.read_csv("surveys.csv")
# descrive weight coloumn
desc_weight = surveys_df["weight"].describe()

# print sumary statistics
print(desc_weight)
