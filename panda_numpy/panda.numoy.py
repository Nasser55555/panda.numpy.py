import pandas as pd
import numpy as np  
df = pd.read_csv("/Users/zakaria/Desktop/panda_numpy/employees2 (1).csv")
#print(df.head())
#print(df.dtypes)
#print(df.isnull().sum())
#df["Age"].fillna(df["Age"].median(), inplace=True)
#df["Salaire"] = df.groupby("Département")["Salaire"].transform(lambda x: x.fillna(x.median()))

df["Age"].fillna(df["Age"].median(), inplace=True)
