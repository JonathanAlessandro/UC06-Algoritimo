texto = "         SENAC Lorem ipsum dolor นั่ง amet consectetur adipisicing elit. Nulla, เอิ่ม คอรัปชั่น? Perspiciatis จัดเตรียม asperiores dolorum dignissimos ut magni mollitia modi quae! Temporibus, maxime obcaecati officiis nulla animi quasi ipsum hic! Lorem                   "
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
print(len(texto))


# FUN Maiuscula e minuscula
nome = "jonatHaN olIvEira"
print(nome.upper())
print(nome.lower())
#somente a primeira letra maiuscula as demais ficam minusculas
print(nome.capitalize())
#title deixa apenas a primeira letra de cada palavra em maiusculo as demais são minusculas
print(nome.title())


#metodo para retornar parte da string sendo o primeiro valor o inicio e o ultimo o fim caso esteja em branco o valor ele entende como o inicio e o final exibindo tudo
print(texto[0:3])


#.replace("esse", "por esse") utilizar uma nova varivael para receber a antiga e fazer a substituição
novo_texto = texto.replace(" ","")

print(novo_texto)

#remover espaços em branco ".strip()" remove dos dois lados ".lstrip()" remove da esquerda ".rstrip()" remove da direita
print("____________________________________")
print(texto.strip())
print("____________________________________")
print(texto.lstrip())
print("____________________________________")
print(texto.rstrip()+"asdasd")
print("__________________________________________________________")


#"in" retorna verdadeiro ou falso para se o caracter ou palvra buscado existe na variavel que esta procurando, ele é case sensitive 
print("Lorem" in texto)

#".find()" busca um texto especifico e retorna a posição em que está
print(texto.find("Lorem")) #começa na 15
print(texto[15:21])

#".count()" conta a quantidade de vezes que algo se repete
print(texto.count("l"))


#".startswith()" e ".endswith()" verifica se o elemento inicia com ou termina com, e retorna um booleano (Ele verifica se a string começa)

print(nome.startswith("jo"))
print(texto.endswith(" "))