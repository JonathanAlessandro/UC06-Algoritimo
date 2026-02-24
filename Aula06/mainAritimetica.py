"""
sempre apresentar o resultado apos cada etapa finalizada blz
"""


# somar 3 numeros blz, depois vamos incrementar os 3 numeros, apos somar 3 numeros vamos subtrarir neh e melhor 15, apos isso
# multiplicar por 8
# em seguida dividir resultado por 100

for i in range(3):
    numeroI = int(input("Digite um numero"))


numero1= int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3= int(input("Digite mais um numero: "))

soma= numero1+numero2+numero3

print("os numeros digitados foram",numero1,numero2,numero3)

print("A soma dos numeros é: "+ str(soma))

print("Após reduzir 15 o valo restande é:",soma-15)

print("Após multiplicarmos por 8 o valor e:",soma*8)

print("Apos dividirmos tudo por 100 o resultado é:"+ str((soma*8)/100))
