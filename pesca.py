# 1. A entrada para um clube de pesca custa R$ 20,00 por pessoa e cada pessoa tem direito a levar um peixe. Peixes extras custam 12,00. Elabore um programa que leia o número de pessoas de uma
#família que foram ao clube e o número de peixes obtidos na pescaria. Informe o valor a pagar.
#Nº Pessoas: 4
#Nº Peixes: 5
#Pagar R$: 92.00

valor_entrada = 20
valor_extra = 12

pessoas = int(input('Nº de Pessoas: '))
peixes = int(input('Nº de peixes: '))

total = pessoas * valor_entrada

if peixes > pessoas:
    extras = peixes - pessoas 
    total = total + (extras * valor_extra)

print(f"O valor é de: {total}")