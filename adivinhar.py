#5. Elaborar um programa que leia ‘n’ números, até ser digitado 0. Ao final, exiba quantos números
#foram digitados, a soma dos números e qual o maior número digitado.
#Informe números ou 0 para sair
#Número: 12
#Número: 39
#Número: 13
#Número: 26
#Número: 0
#-----------------------------
#Números digitados: 4
#Soma dos Números: 90
#Maior Número: 39

print("Informe números diversos. Aperte 0 para sair.")
quantidade = 0
soma = 0
maior = 0

while True:
    num = int(input("Número: "))

    if num == 0:
        break

    quantidade = quantidade + 1
    soma = soma + num

    if num > maior:
        maior = num

print(f"N digitados: {quantidade}")
print(f"Soma: {soma}")
print(f"Maior numero: {maior}")