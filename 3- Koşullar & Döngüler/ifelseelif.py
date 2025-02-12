####### IF #######

# if 1 == 1:
#     print("something")

# if 1 == 2:
#     print("something")

number = 11
number2 = 20 

if number == 10:
    print("number is 10")

def number_check(number):
    if number == 10:
        print("number is 10")
number_check(12) # çıktı vermez

########## ELSE #####
def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")
number_check(12)

########## ELIF #####

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")
number_check(6)


