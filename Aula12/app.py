import pandas as pd

print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Adicionar")
print("         2 > Alterar")
print("         3 > Apagar")
opcao = int(input("R: "))


if opcao == 1:
    
    #criar e adicionar ao excel
    print("Opção 1 selecionada")
    nome = str(input("Digite seu nome: "))
    idade = str(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    dados = {
    #para passar a variavel dentro do dicionario caso seja recorrente podemos colocar dentro de conchetes para trasnformar em uma lista
    "nome":[nome],
    "idade":[idade],
    "altura": [altura],
    }
    excel = pd.DataFrame(dados)
    
    excel.to_excel("Aula12\Alunos.xlsx",index=False)
elif opcao == 2:
    print("Opção 2 selecionada")
    print("")