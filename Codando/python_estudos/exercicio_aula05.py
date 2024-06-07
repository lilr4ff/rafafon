# soma = 0

# for i in range(1, 6): #loop de 1 a 5 (i igual index; i é igual o número de vezes que o código irá rodar, se você indicar que precisa de 5 números o i irá rodar 5 vezes)
#     valor = int(input(f"Digite o {i}° valor: "))
#     soma += valor

# media = soma / 5

# print(f"A soma dos 5 números é {soma} e sua média é {media}")

#-------------------------------------------------------------------------------------

# frutas = ["maçã", "banana", "pera"]

# for fruta in frutas: #O for irá passar por todos os itens, na lista por exemplo ele irá citar todos os itens
#     print("A frita da lista é", fruta)

#-------------------------------------------------------------------------------------

# for linha in range (1, 11): #A linha 1 vai interar com todos o  números da coluna para depois trocar de número
#     for coluna in range (1, 11):
#         resultado = linha * coluna
#         print(f"{linha} x {coluna} = {resultado}")

#-------------------------------------------------------------------------------------

# Inicializando variáveis

# soma = 0
# contador = 0

# Loop for para solicitar e validar 5 números inteiros diferentes de  0
# for i in range(5):
#     while True:
#         try:
#             numero = int(input(f"Digite o {i + 1}° o número inteiro (diferente de zero): "))
#             if numero > 0:
#                 break # Sai do loop while se o número for diferente de zero
#             else:
#                 print("Erro: O número não pode ser zero. Digite novamente")
#         except ValueError:
#             print("Erro: Valor inválido. Digite um número intero")

#     # Soma dos números validos

#     soma += numero
#     contador += 1

# # Calculo de média
# if contador > 0:
#     media = soma / contador
#     print(f"A média dos {contador} números digitados é: {media:2f}")
# else:
#     print("Erro: Nenhum número válido foi digitado")

#-------------------------------------------------------------------------------------

# 1 - Faça um script em py para mostrar na tela os numeros de 0 a 100

# for numeros in range (0, 101):
#     print(numeros)

# 2 - Mostrar os números de 0 a 100 que são pares

# i = 0
# while i <= 100:
#     print(i)
#     i += 2

#-------------------------------------------------------------------------------------

# num = int(input("Digite um número inteiro positivo: "))

# soma = 0

# for i in range(2, num + 1, 2):
#     soma += i

# print(f"A soma dos números pares até {num}, é: {soma}")

