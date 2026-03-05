def salvar_usuario(nome,idade):
    with open("aula10/cadastro.txt", "a") as adicionar_texto:
        adicionar_texto.write(f"{nome} - {idade} \n")

while True:
    cadastrar_usuario= input("Deseja cadastrar um usuario?[S/N]")
    if cadastrar_usuario in ["S","s","Sim","sim"]:
        nome_usuario = input("Digite o nome do usuario: ")
        idade_usuario = input("Digite a idade do usuario: ")
        salvar_usuario(nome_usuario,idade_usuario)
    elif cadastrar_usuario in ["N","n","Não","não"]:
        break
    else:
        print("comando invalido por favor digite novamente!")

with open("aula10/cadastro.txt","r") as leitura_texto:
    texto = leitura_texto.read()
    print(texto)

