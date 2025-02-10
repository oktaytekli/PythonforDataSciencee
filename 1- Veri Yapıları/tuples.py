#TUPLE lar ;
    #Değiştirilemez.
    #Sıralıdır..
    #Kapsayıcıdır.


t = ("oktay","tekli",0,2)
print(t)
print(t[0])
print(t[0:3])

t = list(t)
t[0] = 99
t = tuple(t)

print(t)