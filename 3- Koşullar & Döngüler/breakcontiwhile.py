######### BREAK & CONTINUE & WHILE ############

salaries = [1000,2000,3000,4000,5000]

#break
for salary in salaries:
    if salary == 3000:
        break
    print(salary)

#continue
for salary in salaries:
    if salary==3000:
        continue
    print(salary)

#while
number = 1
while number < 5:
    print(number)
    number +=1