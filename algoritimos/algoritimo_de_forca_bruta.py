
#Algoritimos de força bruta

class   Exemplos:

  def Lista():

    lista = [15, 23, 7, 9, 42, 30]
    alvo = 42

    for i in range(len(lista)):
       print(f"Verificando índice {i}, valor {lista[i]}") 

       if lista[i] == alvo:
        print(f"Número {alvo} encontrado no índice {i}")
        break


  def Caractere():

    senha = "42"

    for i in range(10):      # primeiro dígito
      for j in range(10):  # segundo dígito
          tentativa = str(i) + str(j)
          print(f"Tentando senha: {tentativa}")
          if tentativa == senha:
              print(f"Senha encontrada: {tentativa}")
              break


Exemplos.Lista()
