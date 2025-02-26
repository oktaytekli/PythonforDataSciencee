import pandas as pd
import seaborn as sns   

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())

# iloc: integer based selection
print(df.iloc[0:3])
print(df.iloc[0,0])


# loc: label based selection (satır ya da indexlerin değerilerine göre bizzat işlem yapmak istersek loc kullanılır.)
print(df.loc[0:3])



df.iloc[0:3,0:3] #hata verir.
df.loc[0:3,0:3]

col_names = ["age","embarked","alive"]
print(df.loc[0:3,col_names])


