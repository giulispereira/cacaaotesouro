import random

# 1. Função para criar o oceano (matriz)
# Usa uma lógica de compreensão de lista para criar as linhas e colunas [cite: 13, 25]
def criar_oceano(tamanho):
    # Cada elemento '~' representa a água do mar [cite: 12]
    return [['~' for _ in range(tamanho)] for _ in range(tamanho)]

# 2. Função para colocar os alvos (navios) de forma aleatória [cite: 20]
def posicionar_alvos(matriz, quantidade):
    posicionados = 0
    while posicionados < quantidade:
        # Sorteia a posição usando a biblioteca random
        filar = random.randint(0, len(matriz) - 1)
        colun = random.randint(0, len(matriz) - 1)
        
        # Verifica se a célula está vazia para não sobrepor navios [cite: 16, 30]
        if matriz[filar][colun] == '~':
            matriz[filar][colun] = 'S' # 'S' de Ship (Navio)
            posicionados += 1

# 3. Função para desenhar o jogo na tela para o usuário [cite: 32, 33]
def desenhar_jogo(matriz, fim_de_jogo=False):
    # Imprime os números das colunas no topo [cite: 89]
    print("\n    0 1 2 3 4")
    # Percorre cada linha da matriz [cite: 36]
    for idx, linha in enumerate(matriz):
        # Cria uma lista temporária para esconder os navios durante o jogo
        visual = []
        for celula in linha:
            if celula == 'S' and not fim_de_jogo:
                visual.append('~') # Esconde o navio com onda
            else:
                visual.append(celula)
        # Exibe o índice da linha e o conteúdo [cite: 112, 113]
        print(f"{idx} | {' '.join(visual)} |")

# --- INÍCIO DO JOGO ---
# Pede o nome para o ranking final 
estudante = input("Nome da Capitã: ")
grade = 5
mar = criar_oceano(grade)
posicionar_alvos(mar, 4)

vidas = 5 # Diferente do seu, ela pode ter um sistema de 'vidas'
pontos_giuli = 0

print(f"\nPrepare-se {estudante}! Você tem {vidas} chances.")

# Loop de repetição do jogo [cite: 31, 32]
while vidas > 0:
    desenhar_jogo(mar)
    try:
        # Entrada de dados do usuário [cite: 65]
        alvo_l = int(input("\nEscolha a Linha: "))
        alvo_c = int(input("Escolha a Coluna: "))

        # Lógica de acerto na matriz [cite: 18, 30]
        if mar[alvo_l][alvo_c] == 'S':
            print("DIRETO NO ALVO! +50 pontos.")
            mar[alvo_l][alvo_c] = 'X' # Marca o acerto [cite: 114]
            pontos_giuli += 50
        elif mar[alvo_l][alvo_c] == '~':
            print("Errado... a munição caiu na água.")
            mar[alvo_l][alvo_c] = 'O' # Marca o erro
            vidas -= 1
        else:
            print("Você já atacou essas coordenadas!")
            
    except (ValueError, IndexError):
        print("Coordenadas fora do mapa! Tente de 0 a 4.")

# 4. Finalização e salvamento do Ranking em arquivo .txt [cite: 70, 71]
print(f"\nFim da missão! {estudante}, você fez {pontos_giuli} pontos.")
with open("placar_batalha.txt", "a") as arquivo_ranking:
    arquivo_ranking.write(f"Capitã: {estudante} - Score: {pontos_giuli}\n")

# Exibe o ranking acumulado [cite: 71]
print("\n--- QUADRO DE HONRA ---")
try:
    with open("placar_batalha.txt", "r") as arq:
        print(arq.read())
except FileNotFoundError:
    print("Nenhum recorde ainda.")