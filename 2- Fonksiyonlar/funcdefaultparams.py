##### ÖN TANIMLI ARGÜMANLARR/PARAMETRELER (DEFAULT PARAMETERS/ARGUMENTS) #######

def divide(a,b):
    print(a/b)
divide(1,2)

def divide(a,b=1):
    print(a/b)
divide(1)

def divide(a,b):
    print(a/b)
divide(10)# böyle yaparsak b arg girmemişsin diyerek bir uyarı alırız.

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")
say_hi("mrb")

