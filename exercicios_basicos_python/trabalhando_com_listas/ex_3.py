#formatação de strings

nome = str(input("Digiti seu nome ")).strip();

print("Analisar nome...");
print("Seu nome em maiusculo é {}".format(nome.upper()))
print("Seu nome em minuscullo é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)))


