#2. Um número é dito perfeito, quando é igual a soma dos seus divisores (exceto com o próprio
#número). Ler um número, exibir os seus divisores e informar se ele é ou não perfeito.
#Número: 28
#Divisores do 28: 1, 2, 4, 7, 14
#Soma dos divisores: 28
#Portanto, 28 é um número perfeito

numero = int(input("Divisores do: "))
calculadora = 0
divisores = []

for i in range(1, numero) :
        if numero % i == 0:
            divisores.append(i)
            calculadora +=(i)

print(f"Divisores do {numero} : {divisores}")
print(f"Soma dos divisores de {numero}: {calculadora}")

if calculadora == numero:
    print(f"Então, o número {numero} é um número perfeito")

else:
    print(f"Vish, {numero} é um número imperfeito")
