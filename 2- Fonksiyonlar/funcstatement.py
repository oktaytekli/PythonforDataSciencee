# def function_name(parameters/arguments):
#     statements (function body)

def say_hi(string):
    #print("Merhaba")
    print(string)
    print("Hi")
    print("Hello")
say_hi("selamlaar")

def multiplication(a,b):
    c= a*b
    print(c)
multiplication(10,9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = []

def add_element(a,b):
    c = a*b
    list_store.append(c)
    print(list_store)
add_element(1,7)
add_element(2,7)
add_element(3,7)
