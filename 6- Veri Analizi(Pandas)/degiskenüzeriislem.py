import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)

df = sns.load_dataset("titanic")
print(df.head())

"age" in df

print(df["age"].head())
print(df.age.head())

print(df[["age"]].head())

df[["age","alive"]]

col_names = ["age", "adult_male","alive"]
print(df[col_names])

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

print(df.drop("age3",axis=1).head())

print(df.drop(col_names,axis=1).head())
print(df.loc[:,df.columns.str.contains()].head())
print(df.loc[:,~df.columns.str.contains()].head()) # ~ değildir demek için kullanırız.






