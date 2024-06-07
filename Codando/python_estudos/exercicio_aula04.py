#teste de se e se não

# num1 = 1
# num2 = 3

# if num1 > num2:
#     print("Número 1 maior que número 2")
# elif num1 == num2:
#     print("Números iguais")
# else:
#     print("Número 1 menor que número 2")

#--------------------------------------------------------------------

#Verificando se  número é positivo ou negativo

# numero = 150

# if numero > 0:
#     print("O número é positivo")
# elif numero == 0:
#     print("O número é positivo")
# else:
#     print("O número é negativo")

#--------------------------------------------------------------------

#Verificando a faixa etaria de uma pessoa

# idade = 25

# if idade < 18:
#     print("Você é menor de idade")
# elif idade >= 18 and idade <= 65:
#     print("Você é adulto")
# else:
#     print("Você é idoso")

#--------------------------------------------------------------------

#Verificando se um ano é bissexto

# ano = 2026

# % significa modulo = resto de uma divisão // todo "and" precisa ser true, todo "or" pode ser ture ou false

# if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#     print("O ano é bissexto.")
# else:
#     print("O ano não é bissexto")

#--------------------------------------------------------------------

#Verificar se um elemento está presenta em uma lista

#"in" = se está presente (lembrar do "In" na lingua inglesa)

# frutas = ('maçã', 'banana', 'mamão', 'uva')

# if 'banana' in frutas:
#     print('A banana está na lista')
# else:
#     print('A banana não está na lista')

#--------------------------------------------------------------------

#Exercicio 01 - Escreva um programa que verifica se um número é positivo, negativo ou zero.

numero = 150

# if numero > 0:
#     print("O número é positivo")
# elif numero == 0:
#     print("O número é zero")
# else:
#     print("O número é negativo")

#Exercicio 02 - Crie um programa que solicita a idade do usuário e verifica se ele é elegível para tirar carteira de motorista.

# idade = int(input('Insira sua idade '))

# if idade >= 18:
#     print("Você está elegivel a dirigir")
# else:
#     print("Você não pode dirigir por ser menor de idade")

#Exercicio 03 - Desenvolva um programa que verifica se uma pessoa pode assistir a um filme com classificação indicativa de 12 anos ou mais.

# idade = int(input('Insira sua idade '))

# if idade >= 12:
#     print("Você pode assitir ao filme")
# else:
#     print("Você não pode assistir ao filme")

#--------------------------------------------------------------------

peso = float(input("Insira seu peso "))
altura = float(input("Insira sua altura"))

imc = peso % (altura**2)

if imc < 18.5:
    print("Você está com magreza, obesidade grau 0")
elif imc == 18.5 or imc < 24.9:
    print("Você está normal, obesidade grau 0")
elif imc == 25 or imc < 29.9:
    print("Você está com sobrepeso, obesidade grau 1")
elif imc == 30 or imc < 39.9:
    print("Você está com obesidade grau 2")
else:
    print("Você está com obesidade grave grau 3")

