import numpy as np

v = np.array([1,2,3,4,5])
print(v/5)
print(v*5/10)
print(v**2)
print(v-1)

print(np.subtract(v,1))
print(np.add(v,1))
print(np.mean(v))
print(np.sum(v))
print(np.min(v))
print(np.max(v))
print(np.var(v))

v= np.subtract(v,1)


## İKİ BİLİNMEYENLİ DENKLEM ÇÖZÜMÜ ##

# 5*x0+x1=12
# x0+3*x1=10

a = np.array([[5,1],[1,3]])
b = np.array([12,10])
np.linalg.solve(a,b)

