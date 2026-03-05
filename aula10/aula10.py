#open() usado para abrir arquivos
#"w" modo escreve(write)
#"a" modo adicionar(append)
#"r" modo ler (read)

#o with define que com o arquivo aberto ele coloca o open na variavel temporaria arquivo ao acabar ele fecha o arquivo aberto
with open("aula10/nota.txt", "w") as texto:
    texto.write("Oi")


#adiciona ao final
with open("aula10/nota.txt", "a") as adicionar_texto:
    #\n gera uma quebra de linha
    adicionar_texto.write("\n\nTudo bem")

#abre e lê o arquivo
with open("aula10/nota.txt","r") as leitura_texto:
    texto = leitura_texto.read()
    print(texto)
