# 1 - Escreva um programa em Python para converter Celsius para Fahrenheit (7)

celsius = int(input("Insira a temperatura: "))

fahrenheit = (celsius) * 1.8 + 32
print(f"A temperatura em Fahrenheit é {fahrenheit}")

#----------------------------------------------------------------------------------

# 2 - Escreva um programa em Python para converter KM em Milhas

milhas = float(input("Insira a velocidade: "))

kilometro = (milhas * 1.60934)
print(f"A sua distancia é {kilometro} KM")

#----------------------------------------------------------------------------------

# 3 - Escreva um programa em Python para calcular a média de 5 números, os números devem ser digitados pelo usuário. Regra: os números devem ser diferentes de Zero e não podem ser negativos.

num1 = int(input("Insira seu primeiro valor: "))
if num1 <= 0:
    print("Você não pode inserir um número negativo ou igual a 0")
    num1 = int(input("Insira o primeiro número novamente: "))

num2 = int(input("Insira seu segundo valor: "))
if num2 <= 0:
    print("Você não pode inserir um número negativo ou igual a 0")
    num2 = int(input("Insira o segundo número novamente: "))

num3 = int(input("Insira seu terceio valor: "))
if num3 <= 0:
    print("Você não pode inserir um número negativo ou igual a 0")
    num3 = int(input("Insira o terceiro número novamente: "))

num4 = int(input("Insira seu quarto valor: "))
if num4 <= 0:
    print("Você não pode inserir um número negativo ou igual a 0")
    num4 = int(input("Insira o quarto número novamente: "))

num5 = int(input("Insira seu quinto valor: "))
if num5 <= 0:
    print("Você não pode inserir um número negativo ou igual a 0")
    num5 = int(input("Insira o quinto número novamente: "))

media = (num1 + num2 + num3 + num4 + num5) / 5

print(f"A sua média é {media}")

#--------------------------------------------------------------------------------------------------

# 4 - Escreva um programa em Python que receba 3 números digitados pelo usuário e exiba qual é o maior valor entre eles.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro número é o maior entre os três")
elif num2 > num3 and num2 > num1:
    print("O segundo número é o maior entre os três")
else:
    print("O terceiro número é o maior entre os três")

#--------------------------------------------------------------------------------------------------

# 5 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num1 = int(input("Por favor insira um número: "))
print(f"O número informado foi {num1}")

#--------------------------------------------------------------------------------------------------

# 6 - Faça um Programa que peça 2 números inteiros e um número real (decimal).
#       Calcule e mostre:
#       i. o produto do dobro do primeiro com metade do segundo.
#       ii. a soma do triplo do primeiro com o terceiro.
#       iii. o terceiro elevado ao cubo.

num1 = int(input("Insira o primeira número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = float(input("Insira o primeiro número decimal: "))

i = (num1 * 2) + (num2 // 2)
ii = round((num1 * 3) + num3,2)
iii = round(num3 **3,2)

print(f"O produto do dobro do primeiro com metade do segundo é: {i}")
print(f"A soma do triplo do primeiro com o terceiro é: {ii}")
print(f"O terceiro elevado ao cubo é: {iii}")

#--------------------------------------------------------------------------------------------------

# 7 - Calcularadora de salario liquido

preco_hora = float(input("Quanto você recebe por hora trabalhada? R$"))
quantidade_horas = float(input("Quantas horas você trabalhou no mês? "))

# Import para dar clear quanto o usuário digitar e mostrar apenas os resultados
import os
os.system('cls')

# Import para limpar as casas decimais
from decimal import Decimal

salario_bruto = preco_hora * quantidade_horas
ir = (salario_bruto*11)/100
inss = (salario_bruto*8)/100
sindicato = (salario_bruto*5)/100
salario_liquido = salario_bruto - ir - inss - sindicato

print(f"O seu salário liquido será: \n - Salário bruto: + R${salario_bruto} \n - Imposto de renda: - R${ir} \n - INSS: - R${inss} \n - Sindicato: - R${sindicato} \n - Salário liquido: + R${salario_liquido}")

#--------------------------------------------------------------------------------------------------

# 8 - Calculadora de gastos com tintas

area = float(input("Insira o tamanho (em metros²) da área que você deseja pintar: "))

import os
os.system('cls')

import math

total_tinta = area / 3
total_latas = total_tinta / 18
arredondar_latas = math.ceil(total_latas)
total_valor = arredondar_latas * 80

print(f"Você gastará {arredondar_latas} lastas de tintas, que ficaram R${total_valor}")

#--------------------------------------------------------------------------------------------------

# 9 - Faça um Programa que converta metros para centímetros.

metragem = float(input("Insira sua metragem : "))

metros_to_cm = metragem * 100

print(f"Sua metragem em centimetros é: {metros_to_cm}")

#--------------------------------------------------------------------------------------------------

# 10 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 𝐀 = 𝛑. 𝐫²

raio = float(input("Insira o seu raio: "))

import os
os.system('cls')

area = round(3.14 * (raio**2),2)

print(f"A área do seu circulo é: {area}")