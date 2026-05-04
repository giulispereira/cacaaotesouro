#Elabore um programa que peça para o usuário digitar vários números (notas de alunos). O programa deve parar quando o usuário digitar -1. No final, o programa deve mostrar:
# Quantas notas foram digitadas.
# A média das notas (Soma total dividida pela quantidade).

print("Informe as notas dos alunos separadamente. Para sair, digite -1")
print("")

# Seus "baldes" (variáveis) estão ótimos!
quantidade_notas = 0
soma = 0

while True:
    nota = int(input("Nota: "))

    if nota == -1:
        break

    # Atualizando os baldes a cada rodada
    quantidade_notas = quantidade_notas + 1
    soma = soma + nota

# AGORA, fora do loop (sem o espaço no começo), calculamos a média
if quantidade_notas > 0: # Uma segurança para não dividir por zero se o usuário sair de cara
    media = soma / quantidade_notas
    print("-" * 30)
    print(f"Notas digitadas: {quantidade_notas}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")