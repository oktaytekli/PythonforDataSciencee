import numpy as np

# np.array([1,2,3,4])

# np.zeros(10,dtype=int)
# np.random.randint(0,10,size=10)
# np.random.normal(10,4,(3,4))

###########################

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10,size=5)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
