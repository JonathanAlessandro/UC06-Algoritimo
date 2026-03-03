nome = "Alisson"
idade = 1

#O parametro pode existir somente dentro da função e so avisa ao codigo o que esperar para rodar a função caso não receba da erro
def saudacao(i: str, c: int):
    
    print("Olá ", i, "você tem",c, "anos de idade")

#para chamar a função e obrigatorio passar os parametros caso haja 
saudacao(nome,idade)

def soma (a:int,b:int):
    return a+b

print(soma(123,456))

salario =[1990,2200,4000,1500,7000]
beneficio = 200
pag_final = []

#Dentro da função o que deve ser usado são os parametros da função
#caso queira acessar as variaveis globais diretamento basta não passar parametros 
def soma_salario(lista,benef):
    for pag in lista:
        resultado = pag+benef
        pag_final.append(resultado)

soma_salario(salario,beneficio)
print(pag_final)


# idade_usuario= int(input("Digite sua idade"))


# if idade_usuario >=18:
#     var1=int(input("Digite o primeiro valor: "))
#     var2=int(input("Digite o segundo valor: "))
#     resultado_soma = var1+var2
    
    
lista = [20,12,3,4,58,99]
palavra = "pala"
print(len(lista))
#soma lista
print(sum(lista))
#max maior valor
print(max(lista))
#min menor
print(min(lista))
#sorted() ordena os valores
print(sorted(lista))
#type() retorna o tipo de valor que foi posto na variavel
print(type(lista))
