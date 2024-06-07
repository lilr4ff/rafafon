'''
# Questão 01:

int_0_ate_25 = 0
int_25_ate_50 = 0
int_50_ate_75 = 0
int_75_ate_100= 0

for _ in range(5):
    numero = float(input("Digite um número entre 0 e 100: "))
    if 0 <= numero <= 25:
        int_0_ate_25 += 1
    elif 25 < numero <= 50:
        int_25_ate_50 += 1
    elif 50 < numero <= 75:
        int_50_ate_75 += 
    elif 75 < numero <= 100:
        int_75_ate_100 += 1

print(f"Os números de 0 até 25 são: {int_0_ate_25}")
print(f"Os números de 25 até 59 são: {int_25_ate_50}")
print(f"Os números de 50 até 75 são: {int_50_ate_75}")
print(f"Os números de 75 até 100 são: {int_75_ate_100}")
'''

#---------------------------------------------------------------------------------------

# Questão 02:

valor_inicial = int(input("Insira um valor: "))

valor_final = int(input("Insira um valor: "))

incremento = int(input("Insira um valor como incremento: "))

print(f"Valor inicial: {valor_inicial}")

while valor_inicial <= valor_final:
    valor_inicial += incremento
    print(f"Resultado da soma: {valor_inicial}")

print("O valor final foi atingido.")

