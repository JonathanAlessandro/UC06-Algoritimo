from typing import Final
print("Hello World")


# define uma const uma variavel imutavel
MAX_CONEXOES: Final = 10

idade= int(5)




while True:
    try:
        # Define o tipo do atributo que essa variavel espera da erro caso não seja o correto
        idade_input = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Erro somente numeros são validos")

# os ":" não definem o tipo da variavel apenas o que o codigo deve esperar de tipo
total: float = 100.0

check: bool 
# lista stimples
clientes: list = []

#lista gigante
telefones: tuple 

while True:
    # o "f" e format permite formatar o texto de forma que ele procure por variaveis ou outros elementos do codigo não trata apenas como texto
    resposta = input(f"Então você tem {idade_input} anos de idade certo? (s/n)")

    # if resposta in [...]: Usar uma lista de opções permitidas para o if estar correto.
    if resposta in ['s', 'sim']:
        continuar = True
        break
    elif resposta in ['n', 'nao', 'não']:
        continuar = False
        break
    else:
        # tratando o que o usuario fez de errado
        print("Entrada inválida! Por favor, digite 's' para sim ou 'n' para não.")
    
if continuar:
    print("Prosseguindo com a operação...")
else:
    print("Operação cancelada.")


"""
comentario em mais de uma linha
"""

