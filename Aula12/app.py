import pandas as pd
import os

# Caminho do arquivo Excel onde os dados dos alunos serão salvos
FILE_PATH = "Aula12/Alunos.xlsx"

# Exibe o menu principal no terminal
print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Adicionar")
print("         2 > Alterar")
print("         3 > Apagar")
opcao = int(input("R: "))


# ─────────────────────────────────────────────
# OPÇÃO 1 — ADICIONAR ALUNO
# ─────────────────────────────────────────────
if opcao == 1:
    print("\nOpção 1 selecionada - Adicionar aluno\n")

    # Coleta os dados do novo aluno via input
    nome   = str(input("Digite seu nome: "))
    idade  = str(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    # Cria um DataFrame com os dados do novo aluno
    novo = pd.DataFrame({
        "nome":   [nome],
        "idade":  [idade],
        "altura": [altura]
    })

    # Se o arquivo já existir, lê os dados anteriores e concatena com o novo
    # Caso contrário, usa apenas o novo registro
    if os.path.exists(FILE_PATH):
        existente  = pd.read_excel(FILE_PATH)
        atualizado = pd.concat([existente, novo], ignore_index=True)
    else:
        atualizado = novo

    # Salva o DataFrame atualizado no arquivo Excel (sem coluna de índice)
    atualizado.to_excel(FILE_PATH, index=False)
    print(f"\n✅ Aluno '{nome}' adicionado com sucesso!")


# ─────────────────────────────────────────────
# OPÇÃO 2 — ALTERAR ALUNO
# ─────────────────────────────────────────────
elif opcao == 2:
    print("\nOpção 2 selecionada - Alterar aluno\n")

    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(FILE_PATH):
        print("❌ Nenhum arquivo encontrado. Adicione alunos primeiro.")
    else:
        # Lê o arquivo Excel e carrega os dados em um DataFrame
        df = pd.read_excel(FILE_PATH)

        # Verifica se há alunos cadastrados
        if df.empty:
            print("❌ Nenhum aluno cadastrado.")
        else:
            # Exibe a lista de alunos com seus índices para o usuário escolher
            print(df.to_string(index=True))
            indice = int(input("\nDigite o índice do aluno que deseja alterar: "))

            # Valida se o índice informado existe na tabela
            if indice < 0 or indice >= len(df):
                print("❌ Índice inválido.")
            else:
                print(f"\nAlterando dados de: {df.loc[indice, 'nome']}")

                # Solicita os novos dados e substitui diretamente na linha do DataFrame
                df.loc[indice, "nome"]   = input("Novo nome: ")
                df.loc[indice, "idade"]  = input("Nova idade: ")
                df.loc[indice, "altura"] = float(input("Nova altura: "))

                # Salva o DataFrame com os dados atualizados no arquivo Excel
                df.to_excel(FILE_PATH, index=False)
                print(f"\n✅ Dados atualizados com sucesso!")


# ─────────────────────────────────────────────
# OPÇÃO 3 — APAGAR ALUNO
# ─────────────────────────────────────────────
elif opcao == 3:
    print("\nOpção 3 selecionada - Apagar aluno\n")

    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(FILE_PATH):
        print("❌ Nenhum arquivo encontrado. Adicione alunos primeiro.")
    else:
        # Lê o arquivo Excel e carrega os dados em um DataFrame
        df = pd.read_excel(FILE_PATH)

        # Verifica se há alunos cadastrados
        if df.empty:
            print("❌ Nenhum aluno cadastrado.")
        else:
            # Exibe a lista de alunos com seus índices para o usuário escolher
            print(df.to_string(index=True))
            indice = int(input("\nDigite o índice do aluno que deseja apagar: "))

            # Valida se o índice informado existe na tabela
            if indice < 0 or indice >= len(df):
                print("❌ Índice inválido.")
            else:
                # Guarda o nome antes de remover (para exibir na confirmação)
                nome_removido = df.loc[indice, "nome"]

                # Remove a linha pelo índice e reinicia a numeração dos índices
                df = df.drop(index=indice).reset_index(drop=True)

                # Salva o DataFrame atualizado no arquivo Excel
                df.to_excel(FILE_PATH, index=False)
                print(f"\n✅ Aluno '{nome_removido}' removido com sucesso!")


# ─────────────────────────────────────────────
# OPÇÃO INVÁLIDA
# ─────────────────────────────────────────────
else:
    # Caso o usuário digite um número fora das opções disponíveis
    print("❌ Opção inválida. Escolha 1, 2 ou 3.")