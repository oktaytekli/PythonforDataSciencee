######## ENUMERATE: OTOMATİK COUNTER/INDEXER İLE FOR LOOP ########

std = ["John","Mark","Venessa","Mariam"]

for student in std:
    print(student)

for index,student in enumerate(std):
    print(index,student)

a = []
b = []

for index,student in enumerate(std):
    if index % 2 == 0:
        a.append(student)
    else:
        b.append(student)  