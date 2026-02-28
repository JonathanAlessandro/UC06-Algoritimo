"""
dicionario{} -> Para acessar dados usamos o nome da chave
listas[] - para acessar dados usamos a posicao da lista
"""


notas = [0,1,2,3,4,5,2,4,1,6,7,8,9,10,10,10]
lista_b= ["T","K","U","Z","A","B","C","D","E","F","G","H","I","J"]
#Junta ambas as listas em uma nova variavel
# tudo_junto = notas + lista_b
# #faz uma extensão da lista notas na lista_b
# lista_b.extend(notas)


# #define a posição que será incrementado
#notas.insert(0,False)
#"remove" remove pelo conteudo dentro do array
#O metodo remove e case sensitive 
# notas.remove(10)
# lista_b.remove("A")
# notas.remove(False)



#incrementa no final 
# notas.append("SENAC")

#"pop" remove pela posição caso não haja posição remove pelo ultimo
lista_b.pop()


# print(notas)


print(lista_b)
print(notas)

#"sort()"organiza em ordem crescente funciona com numeros ou textos 
notas.sort()
lista_b.sort()

print(lista_b)

#Faz o contrario do "sort" ele inverte a ordem
lista_b.reverse()

print(lista_b)

print(notas)
print(notas.index(10))
print(notas.count(10))
#clear limpa tudo 
print(notas.clear())
# for nota in notas:
#     print(nota)

