# Entrada: Peça o valor do saque: valor = int(input("Quanto deseja sacar? R$ ")).

# Processamento:

# Use uma variável para controlar o total que ainda precisa ser pago.

# Use uma variável para a cedula_atual (começando por 50).

# Use um contador para saber quantas cédulas de cada valor estão sendo "entregues".

# Saída: Sempre que mudar de nota (ex: de 50 para 20), exiba o total de notas daquela denominação se ele for maior que zero.


saque = int(input("Digite o valor que deseja sacar: "))
notas = [100,50,20,10,5,1]
total = 0

while not total == saque:
    for n in notas:
        if n < saque:
            total+=n
        elif n > notas:
            break
        
print(total)