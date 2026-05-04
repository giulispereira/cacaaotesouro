nome = input("  NOME:  ")
result = int(input("  RESULTADO:  "))

arquivo = open("nao_desista.txt", "a")
arquivo.write(f"Nome: {nome} -- Pontos: {result}\n")
arquivo.close()