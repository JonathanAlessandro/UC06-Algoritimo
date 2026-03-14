import pandas as pd

# 1. Inputs
nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

# 2. Dicionário (mantive as listas para caso você queira criar um DataFrame do zero depois)
dados = {
    "nome": [nome],
    "idade": [idade],
    "Altura": [altura],
}

# 3. Leitura do arquivo (usando / para evitar erros de caminho)
caminho = "Aula12/cadastro_alunos.xlsx"
leitura_excel = pd.read_excel(caminho)

# 4. Inserindo os dados corretamente
# Usamos [0] para pegar o valor de dentro da lista do dicionário
proxima_linha = len(leitura_excel) # Isso faz ele sempre adicionar na última linha disponível
leitura_excel.loc[proxima_linha, "nome"] = dados["nome"][0]
leitura_excel.loc[proxima_linha, "idade"] = dados["idade"][0]
leitura_excel.loc[proxima_linha, "Altura"] = dados["Altura"][0] # Corrigido "Altura"

# 5. Salvar de volta no arquivo (IMPORTANTE: Se não salvar, a alteração só fica na memória)
leitura_excel.to_excel(caminho, index=False)

print("Dados salvos com sucesso!")