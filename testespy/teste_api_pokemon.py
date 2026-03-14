import requests

#função para chamar a api e varrer procurando os pokemons presentes nela
def listar_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=2000"
    #solicitando a api
    response = requests.get(url)
    
    #teste se o codigo e valido e a api está funcionando
    if response.status_code == 200:
        #transformando a api em um modo json
        dados = response.json()
        #pegando somenta a parte de results do arquivo json
        pokemons = dados['results']
        
        #"len" para mostrar o total de pokemons
        print(f"Total de Pokémon encontrados: {len(pokemons)}")
        #looping para verificar todos os pokemons dentro do resultado
        for pokemon in pokemons: 
            #print mostrando o pokemon encontrado para cada vez que o loop rodar "captitalize" para deixar a primeira letra maiuscula
            print(f"- {pokemon['name'].capitalize()}")
    else:
        #tratando o erro no caso do codigo ser diferente de 200
        print("Erro ao acessar a API")

#chamando a função para ver os pokemons encontrados
listar_pokemons()