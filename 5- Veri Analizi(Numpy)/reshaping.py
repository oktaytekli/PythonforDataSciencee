import numpy as np

np.random.randint(1,10,size=9)
np.random.randint(1,10,size=9).reshape(3,3)

ar= np.random.randint(1,10,size=9)
ar.reshape(3,3)

# numpy.reshape, bir NumPy dizisinin (array) boyutlarını değiştirmek 
# için kullanılan bir fonksiyondur. Orijinal dizinin 
# eleman sayısını değiştirmeden, istenen yeni bir 
# şekle (shape) dönüştürmeye yarar.