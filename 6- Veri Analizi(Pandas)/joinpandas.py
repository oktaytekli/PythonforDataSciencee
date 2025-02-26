import pandas as pd
import seaborn as sns
import numpy as np

m = np.random.randint(1,30,size=(5,3))
df1 = pd.DataFrame(m,columns=["var1","var2","var3"])
df2 = df1 + 99

pd.concat([df1,df2])
pd.concat([df1,df2], ignore_index=True)
import pandas as pd

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

print(pd.merge(df1,df2))
print(pd.merge(df1,df2,on="employees"))

# AMAÇ HER ÇALIŞANIN MÜDÜRÜNÜN BİLGİSİNE ERİŞMEK İSTİYORUZ.

df3 = pd.merge(df1,df2)
df4 = pd.DataFrame({
    'group':["accounting","enginerring","hr"],
    'manager':["caner","mustafa","berkcan"]
})

print(pd.merge(df3,df4))


