
a = 0
b = 0

# eq = 2x + 8 = 0
# eq = 2x = 0 - 8
# eq = x = -8 / 2
# eq = x = -4
# eq = x - 5 = 0
# eq = x = 0 + 5
# eq = x = 5

def Primeiro_grau(a,b):
    if(a == 0):
        if(b == 0):
            return 'impossible'
        else 
          return  'imposible'
    if(b > 0):
        b = -b
        if(a > 0):
            a = -a;
            if(a < 0):
                a = a
    if(b < 0):
        b = b
        if(a < 0):
            a = a
            if(a > 0):
                a = -a
    
    return b / a


print("A equação do primeiro grau é {}".format(Primeiro_grau(5,0)));

