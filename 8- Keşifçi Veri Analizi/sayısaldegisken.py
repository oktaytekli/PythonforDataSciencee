import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()


cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object","bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]
cat_but_car = [col for col in df.columns if df[col].nunique()> 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[["age","fare"]].describe().T
num_cols=[col for col in df.columns if df[col].dtypes in ["int","float"]]
num_cols=[col for col in num_cols if col not in cat_cols]

def num_summary(dataframe, numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.80]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)

def num_summary(dataframe, numerical_col,plot):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.80]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)
num_summary(df,"age",plot=True)

for col in num_cols:
    num_summary(df,col,plot=True)


def cat_summary(dataframe,col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_count(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    print("##################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

for col in cat_cols:
    cat_summary(df,col,plot=True)

for col in num_cols:
    num_summary(df,col,plot=True)