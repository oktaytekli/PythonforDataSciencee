######################
# Uygulama - Mülakat Sorusu
######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""
    
    #girilen string'in indexlerinde gez.
    for string_index in range(len(string)):
        #index çift ise büyük harfe çevir.
        if string_index % 2 ==0:
            new_string +=string[string_index].upper()
        #index tek ise küçük harfe çevir.
        else:
            new_string +=string[string_index].lower()
    print(new_string)
alternating("hi my name is john and i am learning python")

