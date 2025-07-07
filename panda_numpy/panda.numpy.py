import pandas as pd
import numpy as np  
df = pd.read_csv("/Users/zakaria/Desktop/panda_numpy/employees2 (1).csv")
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Salary"] = df.groupby("Department")["Salary"].transform(lambda x: x.fillna(x.mean()))
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)
df["Years_Experience"] = df["Years_Experience"].astype(int)
df["Remote"] = df["Remote"].replace({"Yes": "Oui", "No": "Non"})

conditions = [
    (df["Years_Experience"] < 3),
    (df["Years_Experience"] >= 3) & (df["Years_Experience"] <= 7),
    (df["Years_Experience"] >= 8) & (df["Years_Experience"] <= 15),
    (df["Years_Experience"] > 15)
]
choices = ["Junior", "Intermédiaire", "Senior", "Expert"]
df["Ancienneté_Catégorie"] = np.select(conditions, choices)
salaire_moyen = df["Salary"].mean()
print(salaire_moyen)


