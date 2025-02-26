## TOPLULAŞTIRMA VE GRUPLAMA (AGGREGATION & GROUPING) ##

import pandas as pd
import seaborn as sns   

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())

print(df["age"].mean())

print(df.groupby("sex")["age"].mean)
print(df.groupby("sex").agg({"age":"mean"}))
print(df.groupby("sex").agg({"age": ["mean","sum"]}))

print(df.groupby("sex").agg({"age": ["mean","sum"],
                             "survived":"mean"}))

print(df.groupby(["sex","embark_town"]).agg({"age": ["mean","sum"],
                             "survived":"mean"}))

print(df.groupby(["sex","embark_town","class"]).agg({"age": ["mean","sum"],
                             "survived":"mean"}))

print(df.groupby(["sex","embark_town","class"]).agg({
    "age":["mean"],
    "survived":"mean",
    "sex":"count"
}))










