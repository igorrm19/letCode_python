
# Algoritimos de força bruta
# Algoritimo de comparação

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


  def bubble_sort(lista):
    n = len(lista)
    for i in range(n):  # repete várias passagens
        for j in range(0, n - i - 1):  # percorre elementos vizinhos
            if lista[j] > lista[j+1]:  # compara
                lista[j], lista[j+1] = lista[j+1], lista[j]  # troca
    return lista

 # Exemplo
  
  

lista = [5, 1, 4, 2, 8]
print("Ordenada:", Exemplos.bubble_sort(lista))

Exemplos.Lista()
