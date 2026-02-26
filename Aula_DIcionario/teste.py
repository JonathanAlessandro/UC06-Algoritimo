aluno = {
    "nome": "Carlos",
    "idade": "150",
    "nota":9.0,
    "curso":"Criomancia",
    #E possivel criar arrays dentro de dicionarios
    "telefones":[12345,67890,12344,5553334],
    #E possivel criar um Dicionario dentro de outro
    "endereço":{
        "estado":"SP",
        "cidade":"Santo Andre",
        "rua":"Ramiro colleoni",
        "numero":"110"
    }
}


#forma de percorrer array em python 
for tel in aluno["telefones"]:
    print(aluno["telefones"])

#nesse try o erro e "KeyError"
try:
    print(aluno["hobbies"])
except KeyError:
    print("Esse campo ainda não existe")


#e possivel adicionar um novo campo tambem incluindo um array
aluno["hobbies"] = []

aluno["hobbies"].append("Surfar")


#Trata o erro "IndexError" os erros aparecem no codigo qual foi
try:
    print(aluno["hobbies"][1])
except IndexError:
    print("Esse campo não existe")


#para deletar um campo é possivel usar a palavra reservada "del" sendo possivel deletar mais de um campo simultaneamente  
del aluno["idade"], aluno["curso"]

# print(aluno)

#percorrer Dicionario e mostrar os campos
for chave in aluno:
    print(chave)
#retorna os valores dos campos
for valor in aluno.values():
    print(valor)
#Percorrer o dicionario retornando chave + valor utilizando o metodo ".items()"
for chave,valor in aluno.items():
    print(chave," : ",valor)
