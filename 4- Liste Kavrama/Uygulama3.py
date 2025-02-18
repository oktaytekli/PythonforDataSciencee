# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

car_crashes= ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col for col in df.columns if "INS" in col]

["FLAG_"+ col for col in df.columns if "INS" in col]

["FLAG_"+ col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns=["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

