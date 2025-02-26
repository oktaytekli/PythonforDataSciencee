import pandas as pd
import seaborn as sns   

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())


print(df.pivot_table("survived","sex","embarked", aggfunc="std"))
print(df.pivot_table("survived","sex",["embarked","class"]))

print(df.pivot_table("survived","sex",["embarked","class"]))

df["new_age"] = pd.cut(df["age"],[0,10,18,25,40,90]) #sayısal değişkeni kategoril değişkene çevirmek için kullanılır.
print(df["new_age"])
print(df.pivot_table("survived","sex",["new_age","class"]))
pd.set_option('display.width',500)



