# ax^2 + bx - c
import cmath

a = 0
b = 0
c = 0


def Segundo_grau(a, b, c):
    delta = (b**2) - (4*a*c)
    raizDelta = cmath.sqrt(delta)


    xUm = (-b + raizDelta) / (2*a)
    xDois = (-b - raizDelta) / (2*a)

    return "Resultado de x1,{}, resultado de x2, {}".format(xUm, xDois)

print(Segundo_grau(10,-10,10))
