import requests
#se for opção 1:
"""
    Pedir para o usuario digitar um id e retornar de dentro da api o personagem referente a esse id, retornar tudo relacionado ao personagem
"""
#se for opção 2:
"""
    Pedir para o usuario digitar um nome e retornar o resultado, retornando todos os personagens com esse nome
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
def buscar(jso):
    #função generica para usarmos dentro do loop e deixarmos apresentavel
    print(f"ID: {jso["id"]}\nNome: {jso["name"]}\nStatus: {jso["status"]}\n Specie: {jso["species"]}\nTipo: {jso["type"]}\nGenero: {jso["gender"]}\nOrigem: {jso["origin"]["name"]}\nLocalizacao: {jso["location"]["name"]}")
    
#Prende o usuario no loop permitindo que saia apenas ao digitar "sair"
while True:
    #varivel para verificar a opção que o usuario deseja utilizar do sistema
    opcao = input("\nPara procurar um personagem por id digite(1). \nPara procurar um personagem por seu nome digite (2). \nPara ver todos os personagens registrados digite (3).\nPara sair digite (sair).\nDigite: ")
    
    if opcao == "1":
        #Valor do id que o usuario precisa passar
        id_usuario = int(input("Digite o ID do personagem que deseja buscar: "))
        link_api = f"https://rickandmortyapi.com/api/character/{id_usuario}"
        res_api = requests.get(link_api)
        jso = res_api.json()
        buscar(jso)
        
    elif opcao == "2":
        nome_usuario = input("Digite o Nome do personagem que deseja buscar: \n")
        link_nome_api = f"https://rickandmortyapi.com/api/character/?name={nome_usuario}"
        res_nome_api = requests.get(link_nome_api)
        json = res_nome_api.json()
        for p in json["results"]:
            print(p["name"])
        
    elif opcao == "3":
        #Url da api chamando a api
        url = f"https://rickandmortyapi.com/api/character"
        #verifica se a api está funcionando
        res_api = requests.get(url)
        #pega a api transformando em um arquivo .json
        jso = res_api.json()
        #separa em outra variavel somente a parte do resultado para usar no loop
        personagens = jso["results"]
        
        for p in personagens:
            buscar(p)
            
    elif opcao.upper() == "SAIR":
        break
    else:
        print("Comando invalido por favor digite uma das opções disponiveis\nPara procurar um personagem por id digite(1). \nPara procurar um personagem por seu nome digite (2). \nPara ver todos os personagens registrados digite (3).\nPara sair digite (sair).")