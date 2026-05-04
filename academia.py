#Um treinador de academia quer um programa para ajudar seus alunos a contarem as séries. O programa deve ler o nome do exercício e o número de séries. Exiba na tela a contagem das séries da seguinte forma:
#Exemplo:
#Exercício: Agachamento
# Séries: 3
# 1ª Série de Agachamento: Concluída!
# 2ª Série de Agachamento: Concluída!
# 3ª Série de Agachamento: Concluída!

exer = input("Nome do Exercicio: ")
ser = int(input("Numero de Séries: "))

for i in range(1, ser+1):
    print(f"{i}ª Série de {exer}: Concluída!")