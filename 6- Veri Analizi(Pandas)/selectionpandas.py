import pandas as pd
import seaborn as sns   

df = sns.load_dataset("titanic")
print(df.head())
print(df.index)
print(df[0:13])
print(df.drop(0,axis=0).head())

delete_indexes= [1,3,5,7]
print(df.drop(delete_indexes, axis=0).head(10))

# df = df.drop(delete_indexes, axis=0)
# print(df.drop(delete_indexes, axis=0, inplace=True))

## DEĞİŞKENİ INDEXE ÇEVİRMEK ##
print(df["age"].head())
print(df.age.head())

df.index = df["age"]
print(df.drop("age",axis=1).head())
print(df.drop("age",axis=1, inplace=True))

### INDEXI DEĞİŞKENE ÇEVİRMEK

df.index
df["age"] = df.index

print(df.head())

df.drop("age",axis=1,inplace=True)
print(df.reset_index().index())
df= df.reset_index()
print(df.head())



