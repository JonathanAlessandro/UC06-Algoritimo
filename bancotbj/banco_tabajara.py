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




SEGUNDA PARTE

Quando o usuário selecionar a opção "2 - Acessar conta" e o campo cpf e numero_conta forem encontrados na base, além de mostrar a mensagem acima, mostre um menu com as seguintes opções:

1 - Saque
2 - Deposito
3 - Saldo

Regras para cada opção
1 - Saque > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante:
- O valor solicitado para saque não pode ser maior que o valor em conta(coluna extrato_bancario), se for digitado um valor maior encerre o fluxo e mostre a mensagem "Valor maior que o disponivel em conta";
- Se o valor for menor que o disponivel em conta, realizar a subitração do valor - o valor na coluna coluna extrato_bancario, quando a operação for realizada com sucesso mostre a mensagem 
print("================================================")
print(      Saque realizado com sucesso!)
print(      Saque: (valor Solicitado)
print(      Valor em conta: (coluna extrato_bancario))
print(      Taxa para saque: (seguir regras para cada conta))
print(      Valor de desconto saque: (seguir regras para cada conta))
print("================================================\n")

OBS: Criar a logica de desconto da taxa para cada conta especifica


2 - Deposito > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante, se o valor for valido então somar com o valor já existente na coluna "extrato_bancario" e mostrar o valor final da conta bancaria(coluna extrato_bancario);
- Se o usuário digita um número negativo então encerre o fluxo e mostre a mensagem "Numero invalido, operação encerrada";


3 - Saldo > Mostre em tela o seguinte template
print("================================================")
print("   Tipo conta: (coluna tipo_conta)")
print("   Saldo em conta: (Coluna extrato_bancario)
print("================================================\n")

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
    df = pd.read_excel(FILE_PATH,dtype={'cpf': str})
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
        tipo_conta = input("Digite o tipo de conta desejada: ").upper()
        
        if tipo_conta =="CORRENTE" :
            tipo_conta = tipo_conta
            break
        elif tipo_conta == "POUPANCA":
            break
        elif tipo_conta == "SALARIO":
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
            "extrato_bancario":[0.0]
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
        try:    
            numero_conta = int(input("Digite o numero da sua conta: "))
            cpf = input("Digite seu cpf: ")
            
            #cria o login encontrado em uma variavel local com todos os dados
            login = df[(df['numero_conta'] == numero_conta) & (df['cpf'] == cpf)]
            
            print(type(numero_conta), type(cpf))
            if not login.empty:
                nome_usuario = login['nome_cliente'].values[0]
                print(f"Bem-vindo {nome_usuario} ao banco Tabajara")
                
                main_menu(login)
                break
        except Exception as e:
            print("Valor digitado invalido!\n")
            
            while True:
                try:
                    novamente = input("\nPara tentar novamente digite (1)\nPara sair digite (2)\nDigite: ")
                    if novamente == "1":
                        break
                    elif novamente == "2":
                        break
                except Exception as e:
                    print("Valor Digitado invalido!")
                    
        
def main_menu(login):
    print("\nDigite a opção desejada: \nSaque\nDeposito\nSaldo\n")
    
    opcao_desejada = input("Digite: ").upper()

    if opcao_desejada == "SAQUE":
        
        saque(login)
        
    elif opcao_desejada == "DEPOSITO":
        deposito(login)
        
    elif opcao_desejada == "SALDO":
        quantidade_conta = login['extrato_bancario'].values[0]
        print(quantidade_conta)



# Seguintes regras para cada conta:
# Saques na conta Corrente: 5% de taxa
# Saques na conta Poupança: Poupança 0% de taxa
# Saques na conta Salario: Salario 2% de taxa
def saque(login):
    
    #dicionario com as formas possiveis
    taxas = {"CORRENTE": 0.05, "POUPANCA": 0.0, "SALARIO": 0.02}
    
    valor_conta = login['extrato_bancario'].values[0]
    conta = login['tipo_conta'].values[0]
    #passa a conta para vermos no dicionario qual valor utilizar
    taxa_percentual = taxas[conta]

    try:
        valor_saque = float(input("Qual o valor que deseja sacar: "))
    except ValueError:
        print("Valor inválido!")
        return

    if valor_saque > valor_conta:
        print("Valor maior que o disponível!")
        return

    taxa = valor_saque * taxa_percentual
    calculo = valor_conta - valor_saque - taxa

    print("================================================")
    print("      Saque realizado com sucesso!")
    print(f"      Saque: {valor_saque}")
    print(f"      Valor em conta: {calculo:.2f}")
    print(f"      Taxa para saque: {taxa_percentual*100:.0f}%")
    print(f"      Valor de desconto saque: {taxa:.2f}")
    print("================================================\n")


    #para salvar precisa chamar a variavel global e passar a variavel local que e o login e salvar as alterações
    df.loc[login.index[0], 'extrato_bancario'] = calculo
    df.to_excel(FILE_PATH, index=False)


def deposito(login):
    try:
        valor_deposito = float(input("Qual o valor que deseja sacar: "))
    except ValueError:
        print("Valor inválido!")
        return
    valor_conta = login['extrato_bancario'].values[0]
    total = valor_deposito + valor_conta
    
    df.loc[login.index[0], 'extrato_bancario'] = total
    df.to_excel(FILE_PATH, index=False)
    
if opcao == 1:
    acessar_conta()
elif opcao == 2:
    criar_conta()