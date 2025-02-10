#set;
    # Değiştirilebilir.
    # Sırasız ve eşsizdir.
    # Kapsayıcıdır.

#difference(): iki kümenin farkı

set1 = set([1,3,5])
set2 = set([1,2,3])
print(set1)
print(set2)

print(set1.difference(set2)) # 1 de olup 2 de olmayanlar
print(set2.difference(set1)) # 2 de olup 1 de olmayanlar

#symmetric_difference(): iki kümede de birbirlerine göre olmayanlar

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

# intersection(): iki kümenin kesişimi

set1 = set([1,3,5])
set2 = set([1,2,3])
print(set1.intersection(set2))
print(set1.intersection(set2))

# union(): iki kümenin birleşimi
print(set1.union(set2))
print(set1.union(set1))

#isdisjoint(): iki kümenin kesişimi boş mu?

print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))

#issubset(): bir küme diğer kümenin alt kümesi mi?
print(set2.issubset(set1))
print(set1.issubset(set2))

#issuperset(): bir küme diğer kümenin alt kümesi mi?
print(set2.issuperset(set1))
print(set1.issuperset(set2))





