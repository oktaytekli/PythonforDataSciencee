############# RETURN: FONKSİYON ÇIKTILARINI GİRDİ OLARAK KULLANMAK ######################

# def calculate(varm,moisture,charge):
#     print((varm + moisture/charge))
# calculate(98,12,78)

# def calculate(varm,moisture,charge):
#     return(varm + moisture)/charge
# a = calculate(98,12,78)*10
# print(a)

def calculate(varm,moisture,charge):
    varm = varm *2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm,moisture,charge
print(tuple(calculate(98,12,78)))