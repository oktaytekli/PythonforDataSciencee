import pandas as pd
import seaborn as sns   

pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
print(df.head())

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

print((df["age"]/10).head())
print((df["age2"]/10).head())
print((df["age3"]/10).head())

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print(((df[col]/10).head()))

for col in df.columns:
    if "age" in col:
        df[col]=df[col]/10
        print(df[col])

df.head()
print(df[["age","age2","age3"]].apply(lambda x:x/10).head())
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x:x/10).head())
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x:(x-x.mean())/ x.std()).head())

def standart_scaler(col_name):
    return (col_name-col_name.mean()) / col_name.std()

df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()
df.loc[:,["age","age2","age3"]] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()
df.loc[:,df.columns.str.contains("age")] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()

df.head()
