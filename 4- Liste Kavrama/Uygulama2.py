######################
# Bir veri setindeki değişken isimlerini değiştirmek
######################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

car_crashes = ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())


A = []
for col in df.columns:
    A.append(col.upper())

df.columns= A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]