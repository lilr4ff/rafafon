# Exercicio 01
"""
numeros = []
for i in range(1,6):
    num = int(input("Insira um número: "))
    numeros.append(num)

soma = sum(numeros)

print(f"O resultado da soma dos números é {soma}")
"""

# -------------------------------------------------------------------------

# Exercicio 02
"""
palavras = []

for i in range(1,5):
    words = input("Insira uma palavra: ")
    palavras.append(words)

lista_maiuscula = [m.upper() for m in palavras]
print(lista_maiuscula)
"""

# -------------------------------------------------------------------------

# Exercicio 03

lista01 = []
lista02 = []

for i in range(1,4):
    palavras_lista01 = input("Insira as palavras para a 1° lista: ")
    lista01.append(palavras_lista01)

for i in range(1,4):
    palavras_lista02 = input("Insira as palavras para a 2° lista: ")
    lista02.append(palavras_lista02)

conjunto01 = set(lista01)
conjunto02 = set(lista02)

lista_comum = list(conjunto01.intersection(conjunto02))
print(f"As seguintes palavras estão presentes nas duas listas: {lista_comum}")