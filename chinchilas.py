#4. Digamos que o número de chinchilas de uma fazenda triplica a cada ano, após o primeiro ano.
#Elaborar um programa que leia o número inicial de chinchilas e anos e informe ano a ano o número
#médio previsto de chinchilas da fazenda. O número inicial de chinchilas deve ser maior ou igual a 2
#(um casal).
#Número de Chinchilas: 8
#Anos da criação: 6
#1º Ano: 8 chinchilas
#2º Ano: 24 chinchilas
#3º Ano: 72 chinchilas
#4º Ano: 216 chinchilas
#5º Ano: 648 chinchilas
#6º Ano: 1944 chinchilas

numero = int(input("Numero de Chinchilas: "))

if numero < 2:
    print("Poxa, é necessário um mínimo de 2 para calcularmos")

else:
    anos = int(input("Anos de Criação: "))
    populacao_atual = numero

    for i in range(1, anos + 1):
        print(f"{i}º Ano: {populacao_atual} chinchilas")
    
        populacao_atual = populacao_atual *3