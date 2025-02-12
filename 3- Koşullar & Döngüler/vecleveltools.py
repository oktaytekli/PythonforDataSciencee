######################
# lambda, map, filter, reduce
######################

#Lambda

def summer(a,b):
    return a + b

summer(1,3)*9

new_sum = lambda a,b: a+b
print(new_sum(4,5))

#Map

salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x *20/100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

print(list(map(new_salary,salaries)))
print(list(map(lambda x:x*20/100+x,salaries)))

#del new_sum

print(list(map(lambda x:x*20/100+x,salaries)))
print(list(map(lambda x: x **2 ,salaries)))

# FILTER
list_store = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x%2==0, list_store))

#Reduce
from functools import reduce
list_store = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda a,b:a+b,list_store))



