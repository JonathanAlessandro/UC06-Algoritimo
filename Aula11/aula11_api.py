import requests
#API ela precisa ser armazenada em uma variavel
url = "https://rickandmortyapi.com/api/character"


#a função get quando executar o codigo ele vai pegar a api e solicitar uma resposta da api se está funcionando
resposta = requests.get(url)
# print(resposta)
#agora atribuimos a varivael criada json a resposta em formato de arquivo json
json = resposta.json()

# print(json)

personagem = json["results"]

# print(personagem)

#laço de repetição para consultar os nomes dos personagens
# for p in personagem:
    
#     print(p["name"])
    

#------------------------------------------------------------------------------------------------

#retornar mais informações alem do nome

# for mais_info in personagem:
#     print("Nome: ", mais_info["name"])
#     print("Status: ", mais_info["status"])
#     print("Especie: ", mais_info["species"])
#     print("-------------------------------------------------------")

#------------------------------------------------------------------------------------------------
#Pedir para o usuario digitar um id e retornar da api o personagem referente a esse id

id_usuario = int(input("Digite um numero inteiro: "))
link_api = f"https://rickandmortyapi.com/api/character/{id_usuario}"
res = requests.get(link_api)
jso = res.json()

print("Nome: ", jso["name"])
print("Status: ", jso["status"])
print("Especie: ", jso["species"])
print("-------------------------------------------------------")

#criar um menu para seleção 
#1 - consultar por ID
#2 - consultar por nome
#3 - lista de personagens


#se for opção 1:
"""
    Pedir para o usuario digitar um id e retornar de dentro da api o personagem referente a esse id, retornar tudo relacionado ao personagem
"""
#se for opção 2:
"""
    Pedir para o usuario digitar um nome e retornar o resultado
    
    
    OBS: para percorrer o json e retornar o nome digitado.
"""

    #for mais_info in personagem:
    #     print("Nome: ", mais_info["name"])



#se for opção 3:
"""
    retornar todos os personagens
    "id"
    "name"
    "status"
    "species"
    "gender"
    "origin": {
    "name": "Earth",
    }
    location": {
    "name": "Earth",
    }
    "image"
    
"""