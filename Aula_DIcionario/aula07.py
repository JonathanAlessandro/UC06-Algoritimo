#Dicionario em python e o equivalente a Objeto do javascript


aluno = {
    "nome": None,
    "idade": None,
    "nota":0.0,
    "curso":None,
    #E possivel criar arrays dentro de dicionarios
    "telefones":[],
    #E possivel criar um Dicionario dentro de outro
    "endereço":{
        "estado":None,
        "cidade":None,
        "rua":None,
        "numero":None
    }
}

print(aluno)

#acessando valor
print(aluno["nome"])

print(aluno["endereço"]["estado"])

print(aluno["telefones"])

#Adicionando valor aos campos do dicionario
#Tambem podemos alterar usando essa logica de aluno["campo_a_ser_alterado"] = "valor a ser atribuido"
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade: "))
aluno["nota"] = float(input("Digite a nota do aluno: "))
aluno["curso"]= input("Digite o curso do aluno: ")
#Primeiro crio uma variavel para receber o valor depois adiciono ele no array e não diretamente no array
numero_telefone = input("Numero de telefone: ")
aluno["telefones"].append(numero_telefone)

#Insiro direto no array sem armazenar em uma variavel antes
aluno["telefones"].append(input("Numero de telefone: "))

aluno["endereço"]["estado"] = input("Digite o Estado: ")
aluno["endereço"]["cidade"] = input("Digite a Cidade: ")
aluno["endereço"]["rua"] = input("Digite o nome da rua: ")
aluno["endereço"]["numero"] = input("Digite o numero da residencia: ")

#e possivel adicionar um novo campo tambem incluindo um array
aluno["hobbies"] = []

print(aluno)
#Os arrays sao acessados pela posicao caso nao queira completo
print(aluno["telefones"][0])
#podemos alterar o valor dos campos do array tambem
aluno["telefones"][1] = "1223445"