# quantidade de vezes que o numero aparece
# dicionario

nums = [111,222,1,333,4,21,1,222,2,2,2,1,5]

contagem = {}

for num in nums:
    contagem[num] = contagem.get(num, 0) + 1

for num, qtd in contagem.items():
    print(f"o numero {num} aparece {qtd}")


