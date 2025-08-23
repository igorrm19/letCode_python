
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
    if(a == 0 or b == 0):
        return "Erro a e b não podem ser 0"
    if(b > 0):
        b = -b
    else:
        b = b
    
    return b / a


print("A equação do primeiro grau é, {}".format(Primeiro_grau(5,0)));

