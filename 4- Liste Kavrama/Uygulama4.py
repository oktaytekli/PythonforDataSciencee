# Amaç key'i string,value'su aşağıdaki gibi bir liste olan sözlük oluşturun.
# Sadece sayısal değişkenler için bunu yapmak istiyoruz.

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

car_crashes= {'total': ['mean', 'min', 'max', 'var'],
 'speeding': ['mean', 'min', 'max', 'var'],
 'alcohol': ['mean', 'min', 'max', 'var'],
 'not_distracted': ['mean', 'min', 'max', 'var'],
 'no_previous': ['mean', 'min', 'max', 'var'],
 'ins_premium': ['mean', 'min', 'max', 'var'],
 'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

numcols = [col for col in df.columns if df[col].dtype !="0" ]
soz = {}
agg_list = ["mean","min","max","sum"]

for col in numcols:
    soz[col] = agg_list

#kısa yol
new_dict = {col: agg_list for col in numcols}

df[numcols].head()

df[numcols].agg(new_dict)

