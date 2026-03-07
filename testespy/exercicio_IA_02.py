# Desafio: Analisador de Grupo
# Objetivo: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deve perguntar se o usuário quer ou não continuar.

# Requisitos de Processamento:

# Quantas pessoas têm mais de 18 anos.

# Quantos homens foram cadastrados.

# Quantas mulheres têm menos de 20 anos.

contador_idade_f =0
contador_idade_m= 0
contador_mulheres = 0
contador_homens = 0

while True:
    continuar = input("Deseja realizar um cadastro?[S/N]")
    
    if continuar in ["S","s","Sim","sim"] :
        nome_pessoa = input("Digite o nome da pessoa que deseja cadastrar: ")
        idade_pessoa = input("Digite a idade da pessoa: ")
        sexo_pessoa= input("Digite o sexo da pessoa: ")
        
        if sexo_pessoa in ["m","M","masculino","Masculino"]:
            contador_homens+=1
            if idade_pessoa >= 18:
                contador_idade_m+=1
        elif sexo_pessoa in ["f","F","feminino","Feminino"]:
            contador_mulheres+=1
            if idade_pessoa <20:
                contador_idade_f+=1

    elif continuar in ["N","n","não","Não","Nao","nao"]:
        break
    else:
        print("Não compreendi seu comando")
