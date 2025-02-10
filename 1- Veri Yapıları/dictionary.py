# Sözlükler;
    #Değiştirilebilir.
    #Sırasızdır.
    #Kapsayıcıdır.

#key-value
dic = {
    "REG": "Regression",
    "LOG":"Logistic Regression",
    "CART":"Classification and Reg"

}

dic = {
    "REG": ["Regression",10],
    "LOG":["Logistic Regression",20],
    "CART":["Classification and Reg",30]

}

# dic = {
#     "REG": 10,
#     "LOG":20,
#     "CART":30

# }
print(dic["CART"][1])
print(dic["REG"])

# key sorgulama

x = "YSA" in dic
print(x)

x = "REG" in dic
print(x)

# key e göre value ya erişmek

X= dic["REG"]
X =dic.get("REG")
print(x)

#value değiştirmek

dic["REG"] = "ysa",10
print(dic["REG"])

# tüm keylere erişmek
x = dic.keys()
print(x)

#tüm valuelara erşmek
x = dic.values()
print(x)

#tüm çiftleri tuple halinde listeye çevirme
x = dic.items()
print(x)

#key-value değerini güncellemek
x = dic.update({"REG",11})
print(x)


