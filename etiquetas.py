#3. Elaborar um programa que leia o nome de um produto e o número de etiquetas a serem
#impressas desse produto. Exiba as etiquetas com o nome do produto, com no máximo 2 etiquetas
#por linha, conforme exemplo de execução do programa, demonstrado a seguir.
#Produto: Suco Natural de Uva
#Nº de Etiquetas: 7
#Suco Natural de Uva Suco Natural de Uva
#Suco Natural de Uva Suco Natural de Uva
#Suco Natural de Uva Suco Natural de Uva
#Suco Natural de Uva

produto = input("Produto: ")
etiquetas = int(input("Nº de Etiquetas: "))

for i in range(1, etiquetas +1):
    if i % 2 != 0:
        print(f"{produto} ", end="")
    else:
        print(produto)
if etiquetas % 2 != 0:
    print()