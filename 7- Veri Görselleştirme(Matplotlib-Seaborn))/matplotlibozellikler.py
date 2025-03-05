import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

## Plot ##
x = np.array([1,8])
y = np.array([0,150])
plt.plot(x,y)
plt.show()

plt.plot(x,y,'o')
plt.show()

x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])

plt.plot(x,y)
plt.show()

plt.plot(x,y,'o')
plt.show()

## Marker ##
y = np.array([13,28,11,100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y,marker='*')
plt.show()

markers = ['o','*','.',',','x','X','+','P','s','D','d','p','H','h']


## Line ##
y = np.array([13,28,11,100])
plt.plot(y,linestyle="dashed")
plt.plot(y,linestyle="dotted")
plt.plot(y,linestyle="dashdot")
plt.plot(y,linestyle="dashdot", color = 'r')
plt.show()

## Multiple Lines ##
x= np.array([23,18,31,10])
y = np.array([13,28,11,100])
plt.plot(x)
plt.plot(y)
plt.show()

## Labels ##

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.title("Bu ana başlık") #başlık
plt.xlabel("X ekseni isimlendirmesi") #x eksenini isimlendirme
plt.ylabel("Y ekseni isimlendirmesi") #y eksenini isimlendirme
plt.grid()
plt.show()

## Subplots ##
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot(1,2,1)
plt.title("1")
plt.plot(x,y)
plt.show()

#plot2
x = np.array([8,8,9,9,10,15,11,15,12,15])
y = np.array([24,20,26,27,280,29,30,30,30,30])
plt.subplot(1,3,2)
plt.title("2")
plt.plot(x,y)
plt.show()


#plot3
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot(1,2,2)
plt.title("3")
plt.plot(x,y)
plt.show()
