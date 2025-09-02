# comparar todos os numeros

lista = [1,1,2,3,4,5]

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            print(i,j)