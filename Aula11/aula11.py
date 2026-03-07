#import importa biblioteca com o comando ctrl + click abre a biblioteca
#random usado para gerar numeros aleatorios
import random
import math
import datetime




numero = random.randint(1,2000)

print(numero)


#Sorteio de alunos

alunos = ["A","I","An","we","l","j"]

#choice escolhe de forma aleatoria 
sorteado = random.choice(alunos) 

print(sorteado)

numero = 16
raiz = math.sqrt(numero)
print(raiz)
potencia = math.pow(2,2)


agora = datetime.datetime.now()

print(agora.year)




#Exercicio 
# solicitar ao usuario um numero de 1 ate 5
# Gerar um numero aleatorio usando a biblioteca random.randint
#verificar se o usuario digitou o mesmo valor que o resultado da função randint


numero_usuario = int(input("digite o numero da sorte: "))
numero_sorte = random.randint(1,2000)


if numero_usuario == numero_sorte:
    print("parabens você tirou a sorte grande.")
else:
    print("que pena!")
