# nome = input("Digite seu nome: ")


# print(f"seu nome é: {nome}")


# numeros = int(input("Digite um numero: "))
# soma = numeros+10

# print(soma)


# calc_salario= float(input("Digite o seu salario: "))
# sum_salario = calc_salario * 3.5

# if sum_salario < 100000000000000000000000000000000000000000000000000:
#     print("Voce e pobre!")
# else:
#     print("Mentiroso!")


# idade= int(input("DIgite sua idade: "))

# if idade>=18:
#     print("velho!")
# else:
#     print("ainda vai ficar velho!")

# nome_aluno=input("nome do aluno")
# nota=int(input("nota do aluno: "))

# if nota >= 7:
#     print("Aluno aprovado")
# elif nota>= 5:
#     print(f"{nome_aluno}aluno aprovado pelo conselho!")
# else:
#     print(f"{nome_aluno} com a nota {nota} não foi suficiente e foi reprovado")


#   Se o usuario for menor de idade  então ele precisa ter autorização 
#   Se o usuario for maior de idade então ele precisa ter a altura minima


idade_usuario = int(input("Qual a sua idade?  "))
altura_usuario = float(input("Qual a sua altura?  "))
autorizacao = ""

if idade_usuario < 18:
    autorizacao = input("Você ainda não e maior de idade possui autorização? responda com (sim) ou (nao): ")
    permissao = "Voce está autorizado, aproveite nossos brinquedos" if autorizacao == "sim" or autorizacao == "s" and altura_usuario >= 1.5 else "voce nao esta autorizado!"
    print(permissao)
elif idade_usuario >=18 and altura_usuario >= 1.50:
    print("Aproveite nossos brinquedos")
else:
    print("desculpa mas não possui a altura necessaria para usar nossos brinquedos")


