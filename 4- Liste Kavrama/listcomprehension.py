salaries = [1000,2000,3000,4000]
def new_salary(x):
    return x *20/100+x

for salary in salaries:
    print(new_salary(salary))

nullist=[]
for salary in salaries:
    nullist.append(new_salary(salary))

for salary in salaries:
    if salary > 3000:
        nullist.append(new_salary(salary))
    else:
        nullist.append(new_salary(salary*2))

[new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary*2 for salary in salaries]

[salary*2 for salary in salaries if salary <3000]

[salary * 2 if salary < 3000 else salary *0 for salary in salaries]

[new_salary(salary*2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

students = ["John","Mark","Vanessa","Maria"]
students_no=["John","Vanessa"]

[student.lower() if student in students_no else student.upper() for student in students]

[student.lower() if student not in students_no else student.upper() for student in students]
