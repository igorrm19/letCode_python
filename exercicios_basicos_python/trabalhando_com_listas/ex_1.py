#lista com nomes aleatorios

import random;

nomes = ['igor', 'briza', 'tierre'];

random.shuffle(nomes); # deixa os nomes em ordem aleatorio

print(nomes);

for nome in nomes:
    print(nome);