import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def cat_summary(dataframe,col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_count(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    print("##################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def grap_col_names(dataframe, cat_th=10,car_th=20):

    """   Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini döndürür.


Parameters  
-----------  
dataframe: dataframe  
    değişken isimleri alınmak istenen dataframe'dir.  
cat_th: int, float  
    numerik fakat kategorik olan değişkenler için sınıf eşik değeri  
car_th: int, float  
    kategorik fakat kardinal değişkenler için sınıf eşik değeri  

Returns  
-------  
cat_cols: list  
    Kategorik değişken listesi  

num_cols: list  
    Numerik değişken listesi  

cat_but_car: list  
    Kategorik görünümlü kardinal değişken listesi  """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object","bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique()> 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"Observations: {len(num_cols)}")
    print(f"Observations: {len(cat_but_car)}")
    print(f"Observations: {len(num_but_cat)}")

    return cat_cols,num_cols,cat_but_car

cat_cols, num_cols,cat_but_car = grap_col_names(df)
df.head()

df["survived"].value_counts()
cat_summary(df,"survived")


## HEDEF DEĞİŞKENİN KATEGORİK DEĞİŞKENLER İLE ANALİZİ ##

df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe, target,categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}),end ="\n\n\n")

target_summary_with_cat(df,"survived","pclass")

for col in cat_cols:
    target_summary_with_cat(df,"survived",col)


## HEDEF DEĞİŞKENİN SAYISAL DEĞİŞKENLER İLE ANALİZİ ##

df.groupby("survived")["age"].mean()
df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe,target,numerical_col):
    print(dataframe.groupby(target).agg({numerical_col:"mean"}), end ="\n\n\n")

target_summary_with_num(df,"survived","age")  

for col in num_cols:
    target_summary_with_num(df,"survived",col)