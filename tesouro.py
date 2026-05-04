import random

print("-------------BEM VINDO: ESSE É O CAÇA AO TESOURO!---------------")
for i in range(1,4):
    print(i)
nome = input("Antes, me fala aí, Qual seu nome jogador? :   ")
print(f"Beleza, {nome}! Vamos lá!")

for i in range(4,7):
    print(i)

def criar_mapa():
    mapa = []
    for i in range(1,5):
        adiciona_ponto = ["."]*4
        mapa.append(adiciona_ponto)
    
    return mapa

def linha_tesouro():
    return random.randint(0,3)

def coluna_tesouro():
    return random.randint(0,3)


def exibir_ranking():
    print("\n" + "=" *30)
    print("           RANKING DOS PIRATAS")
    print("="*30)
    try:
        arquivo = open("ranking_tesouro.txt", "r")
        print(arquivo.read())
        arquivo.close()
    except:
        print("Ainda não há registros no ranking.")
        print("="*30)


tabuleiro = criar_mapa()
alvo_linha = linha_tesouro()
alvo_coluna = coluna_tesouro()


print("Esse é o Mapa! Dá uma olhada: ")
for linha in tabuleiro:
    print(linha)
print("-" * 30)

tentativas = 3

#chutel=[] ia usar mas nao vou mais
#chutec=[]

while tentativas > 0:
    print(f"\nVocê tem {tentativas} tentativas!")

    chute_l = int(input("Digite a LINHA (de 0 a 3): "))
    chute_c = int(input("Digite a COLUNA(de 0 a 3): "))

    if chute_l== alvo_linha and chute_c==alvo_coluna:
        resultado ="vencedor"
        print("Você achou o tesouro, Luffy de One Piece!")
        break
    else:
        tentativas -=1
        if tentativas > 0:
            print("Errou! Vamos, mais uma chance...")
        else:
            print(f"É você não será o Rei dos Piradas dessa vez! O tesouro estava na linha {alvo_linha} e na coluna {alvo_coluna}.")
            resultado = "perdeu"

arquivo = open("ranking_tesouro.txt", "a")
arquivo.write(f"Jogador: {nome:.<15} | RESULTADO: {resultado}\n")
arquivo.close()

print("Seu desempenho foi salvo no ranking, belê? Até a próxima, Pirata!")

print("\n" + "-"*30)
ver_rank = input("Deseja ver o Ranking acumulado agora? (S/N): ")
if ver_rank.lower() == "s":
    exibir_ranking()

else:
    print(f"Então, até a próxima, {nome}!")