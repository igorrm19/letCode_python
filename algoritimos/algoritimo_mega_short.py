# Algoritimo mega sort
# Algoritimo de comparação
# dividir parar conquistar

class Exemplo:
    def merge_sort(lista):
      if len(lista) <= 1:  # caso base: lista com 0 ou 1 elemento já está ordenada
        return lista

      meio = len(lista) // 2
      esquerda = Exemplo.merge_sort(lista[:meio])   # recursão na metade esquerda
      direita = Exemplo.merge_sort(lista[meio:])    # recursão na metade direita

      return merge(esquerda, direita)  # mescla as duas listas ordenadas


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # compara os elementos das duas listas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # adiciona o que sobrou de cada lado (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


 # Exemplo de uso:
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
print("Lista ordenada:", Exemplo.merge_sort(lista))

