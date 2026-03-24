#para começar a usar excel instalar pandas e openpyxl basta usar o comando pip install pandas openpyxl
#para usar excel online tem outra biblioteca

#pode renomear o import usando "as"
import pandas as pd

nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

dados = {
    #para passar a variavel dentro do dicionario caso seja recorrente podemos colocar dentro de conchetes para trasnformar em uma lista
    "nome":[nome],
    "idade":[idade],
    "altura": [altura],
}


#"DataFrame" e uma função da biblioteca pandas transforma os dados em uma tabela legivel para o python trabalhar, e o formato que o pandas consegue trabalhar
# excel = pd.DataFrame(dados)


#"to_excel" serve para criar uma nova planilha, pegar os dados digitado em formato DataFrame e gravar na planilha criada
# #"index=False" não deixa criar o indice
# excel.to_excel("Aula12\cadastro_alunos.xlsx", index=False)


#Le um arquivo excel já existente
leitura_excel = pd.read_excel("Aula12\cadastro_alunos.xlsx",dtype={'idade': str})


#o loc precisa de 2 informações
#1 = numero da linha / 2 = nome da coluna

proxima_linha= len(leitura_excel)

leitura_excel.loc[proxima_linha,"nome"] = dados["nome"]
# leitura_excel.loc[proxima_linha,"idade"] = dados["idade"]
# leitura_excel.loc[proxima_linha,"altura"] = dados["altura"]


# leitura_excel.to_excel("Aula12\cadastro_alunos.xlsx",index=False)

# print(leitura_excel["nome"])

#apagar linhas de uma planilha

#leitura_excel = leitura_excel.drop(1)

leitura_excel.loc[2,"nome"] = dados["nome"]
leitura_excel.loc[2,"idade"] = dados["idade"]
leitura_excel.loc[2,"altura"] = dados["altura"]

#salvar alteração 
leitura_excel.to_excel("Aula12\cadastro_alunos.xlsx",index=False)


