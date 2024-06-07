# Exercicio 01 - Escreva um script que tenha uma varável contendo o raio de um círculo e imprima a área do círculo e a circunferência do círculo.

# raio = 10
# pi = 3.14

# a = pi * (raio**2)
# c = round(2 * raio * pi,2)

# print(f"A área do circulo contendo um raio 10 é {a} e sua circunferencia {c}")

# import math

# raio = int(input("Digite o valor do raio: "))
# area = math.pow(raio, 2) * math.pi
# circ = 2 * raio * math.pi
# print(f"A área do circulo é: {area:.2f}")
# print(f"A circunferencia do circulo é: {circ:.2f}")


# --------------------------------------------------------------------------------------
# Exercicio 02 - Escreva um script que tenha dois números a e b e imprimi os resultados de:
# A) a + b / B) a - b / C) a*b / D) a/b

# num1 = 7
# num2 = 5

# soma = num1 + num2
# subtração = num1 - num2
# multiplicação = num1 * num2
# divisão = num1 / num2

# print(f"- O resultado da soma é {soma} \n- O resultado da subtração é {subtração} \n- O resultado da multiplicação é {multiplicação} \n- O resultado da divisão é {divisão}")


# -------------------------------------------------------------------------------------------
# Exercicio 03

# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))

# soma = num1 + num2
# subtração = num1 - num2
# multiplicação = num1 * num2
# divisão = num1 / num2

# print(f"- O resultado da soma é {soma} \n- O resultado da subtração é {subtração} \n- O resultado da multiplicação é {multiplicação} \n- O resultado da divisão é {divisão}")

# -------------------------------------------------------------------------------------------
# Exercicio 04

# def numero_primo(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num)):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Insira um número aqui: "))
# if numero_primo(num):
#     print("O número é primo")
# else:
#     print("O número não é primo")


# -------------------------------------------------------------------------------------------
# Exercicio 05

'''
def celsius_para_farenheit(celsius):
    return celsius * 9/5 + 32

def farenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float
'''

frase = input("Digite uma frase: ")
palavras = frase.split()
print("Número de palavras na frase:", len(palavras))

