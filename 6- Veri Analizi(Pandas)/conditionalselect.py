import pandas as pd
import seaborn as sns   

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())

print(df[df["age"]> 50].head())
print(df[df["age"] > 50].count())

print(df.loc[df["age"] > 50, ["class","age"]].head())
print(df.loc[(df["age"] > 50) & (df["sex"]=="male"), ["class","age"]].head())

df_new=df.loc[(df["age"] > 50) 
             & (df["sex"]=="male") 
             & ((df["embark_town"]=="Cherbourg") | (df["embark_town"] == "Southampton")), 
             ["class","age","embark_town"]]

df_new["embark_town"].value.counts()
