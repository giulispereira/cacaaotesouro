#Uma pizzaria tem uma promoção: o rodízio custa R$ 50,00 por pessoa. Crianças de até 10 anos pagam apenas R$ 30,00. Elabore um programa que leia o número de adultos e o número de crianças de uma família e informe o valor total a pagar.

# rodizio = 50
#crianca = 30
#total: 0

#adultos = int(input("Numero de Adultos: "))
#crian = int(input("Numero de Crianças: "))

#total = (adultos * rodizio) + (crian * 30)
# def calcular_total(adultos, crian):

#print(f"Total a Pagar: {total}")

def preco_total(adulto, crianca):
    adultos = 50
    criancas = 30

    total = (adulto * adultos) + (criancas * crianca)

    return total

print("-----------PREÇO FINAL-----------")

adulto = int(input("QUANTOS ADULTOS? "))
crianca = int(input("QUANTAS CRIANÇAS? "))

valor = preco_total(adulto, crianca) 

print(f"Boa noite! O preço total foi de: {preco_total(adulto, crianca)}")