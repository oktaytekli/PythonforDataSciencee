######## FOR ###########

std = ["John","Mark","Venessa","Mariam"]

for student in std:
    print(student)

for student in std:
    print(student.upper())



salaries = [1000,2000,3000,4000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary*20/100+salary))



def new_salary(salary,rate):
    return int(salary*rate/100+salary)

new_salary(1500,10)
new_salary(3500,10)

for salary in salaries:
    print(new_salary(salary,20))


salaries2 = [10000,25000,37000,43000]

for salary in  salaries2:
    print(new_salary(salary,15))

for salary in salaries:
    if salary >=3000:
        print(new_salary(salary,10))
    else:
        print(new_salary(salary,20))

