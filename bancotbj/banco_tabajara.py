#  Banco Tabajara
# Vamos criar um sistema bancário chamado banco tabajara, nosso banco terá as seguintes caracteristicas:
"""
Contas:
- Corrente
- Poupança
- Salario

Dados do cliente que vamos guardar em um excel:
- nome_cliente
- tipo_conta
- numero_conta
- cpf
- agencia
- extrato_bancario
- deposito
- saque

Obs: Esse serão os nomes das colunas no nosso excel

Seguintes regras para cada conta:
Saques na conta Corrente: 5% de taxa
Saques na conta Corrente: Poupança 0% de taxa
Saques na conta Corrente: Salario 2% de taxa

Desenvolvimento

Crie um menu com as seguintes opções:
1 - Criar conta
2 - Acessar conta

Regras para cada opção no menu
1 - Criar conta > Solicitar ao usuario as seguintes informações:
- nome_cliente
- cpf
- tipo_conta

O outros campos serão gerados de forma automatica
- numero_conta = Será gerada de forma sequencial começando do 0 até 100
- agencia = será gerado de forma sequencial começando do 400 até 700
- extrato_bancario = valor inicial terá que começar em 0

Ao finalizar mostrar para o usuário o nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario

2 - Acessar conta > É necessário que o usuário passe os seguites dados:
- cpf
- numero_conta
> Precisa percorrer o excel e encontra o cliente com os mesmo dados de cpf e numero_conta caso encontre o cliente na base retornar uma mensagem: "Bem-vindo "nome_cliente" ao banco Tabajara" SENAO se o usuario não existir na base então retornamos uma mensagem "Usuário não encontrado, tentar novamente ou realizar o cadastro"
"""
import pandas as pd
import os

# Caminho do arquivo Excel onde os dados dos alunos serão salvos
FILE_PATH = "bancotbj/bancotbj.xlsx"



print("================================================")
print("        BEM - VINDO AO BANCO TABAJARA")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Acessar conta")
print("         2 > Criar conta")
opcao = int(input("R: "))
#faço a conexão e criação do arquivo caso não exista
#se o caminho existir apenas atribui o arquivo a variavel
if os.path.exists(FILE_PATH):
    df = pd.read_excel(FILE_PATH)
#caso o arquivo não exista cria o arquivo com os campos vazios apenas as colunas definidas
else:
    df = pd.DataFrame(columns=[
            "numero_conta","nome_cliente", "tipo_conta",
            "cpf", "agencia", "extrato_bancario"
        ])
    df.to_excel(FILE_PATH, index=False)


def criar_conta():
    print("Para realizar o cadastro informe seu nome, cpf e tipo de conta desejada:")
    nome_cliente = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    print("Digite o tipo de conta desejada:\n 1 > Corrente\n 2 > Poupanca\n 3 > Salario")
    
    while True:
        tipo_conta = input("Digite o tipo de conta desejada: ")
        
        if tipo_conta.upper() =="CORRENTE" :
            tipo_conta = tipo_conta
            break
        elif tipo_conta.upper() == "POUPANCA":
            break
        elif tipo_conta.upper() == "SALARIO":
            break
        else:
            print("Digite um dos tipos de contas aceitos")
            
    #armazena o tamanho do excel para usarmos como numero de conta e fazer a soma para a agencia
    conta= len(df)
    if conta < 100:
        dados = pd.DataFrame({
            "numero_conta": [conta],
            "nome_cliente":   [nome_cliente],
            "tipo_conta": [tipo_conta],
            "cpf":  [cpf],
            "agencia":[conta+400],
            "extrato_bancario":[0]
        })
        
        criar = df
        proxima_linha = len(criar) # Isso faz ele sempre adicionar na última linha disponível
        criar.loc[proxima_linha, "numero_conta"] = dados["numero_conta"][0]
        criar.loc[proxima_linha, "nome_cliente"] = dados["nome_cliente"][0]
        criar.loc[proxima_linha, "tipo_conta"] = dados["tipo_conta"][0]
        criar.loc[proxima_linha, "cpf"] = dados["cpf"][0]
        criar.loc[proxima_linha, "agencia"] = dados["agencia"][0]
        criar.loc[proxima_linha, "extrato_bancario"] = dados["extrato_bancario"][0]
        criar.to_excel(FILE_PATH, index=False)
        
        print(f"Conta criada com sucesso seu numero de conta é: {conta}")
    else:
        print("Numero maximo de contas já cadastradas")
        
    print("Conta cadastrada com sucesso")
    acessar_conta()

def acessar_conta():
    while True:
        numero_conta = int(input("Digite o numero da sua conta: "))
        cpf = int(input("Digite seu cpf: "))
        login = df[(df['numero_conta'] == numero_conta) & (df['cpf'] == cpf)]
        
        if not login.empty:
            print("Login Realizado com sucesso!")
        else:
            print("Conta ou CPF incorretos.")

if opcao == 1:
    acessar_conta()
elif opcao == 2:
    criar_conta()