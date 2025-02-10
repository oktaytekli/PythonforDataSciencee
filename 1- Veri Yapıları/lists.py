#Listeler;
    # Değiştirilebilir.
    # Sıralıdır. Index işlemler yapılabilir.
    # Kapsayıcıdır.

result = [1,2,3,4]
print(type(result))

result = ["a","b","c","d"]
print(type(result))

result = [1,2,3,"a","b","c","d",True,[1,2,3]]
print(type(result))

# print(result)
# print(result[0])
# print(result[5])
# print(result[6])
# print(result[8][1])

# Liste metodları
dir(result)

#len: builtin python fonksiyonu, boyut bilgisi
print(len(result))

#append = eleman ekler
x = result.append(100)
print(x)

# pop indexe göre siler
x= result.pop(0)
print(x)

# insert indexe ekler
x = result.insert(2,99)
print(x)






