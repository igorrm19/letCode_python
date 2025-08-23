num1 = 0
num2 = 0 

class Calculadora:

    def Soma(num1, num2):
      return num1 + num2;

    def Subtrair(num1, num2):
      return num1 - num2;

    def Divisao(num1, num2):
      return num1 / num2;

    def Multiplicar(num1, num2):
      return num1 * num2;



print("A soma é {}".format(Calculadora.Soma(2,2)));
print("A soma é {}".format(Calculadora.Subtrair(2,2)));
print("A soma é {}".format(Calculadora.Divisao(2,2)));
print("A soma é {}".format(Calculadora.Multiplicar(2,2)));

