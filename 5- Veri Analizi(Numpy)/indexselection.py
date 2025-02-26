#veri yapılarının içerisindeki verilere ulaşmamızı sağlayan yöntemdir.

import numpy as np

a =np.random.randint(10,size=10)
print(a[0])
print(a[0:5])
a[0]=999

m = np.random.randint(10,size=(3,5))
print(m)
print(m[0,0])
print(m[1,1])
print(m[2,3])
print(m[:,0])
print(m[1,:])
print(m[0:2,0:3])



