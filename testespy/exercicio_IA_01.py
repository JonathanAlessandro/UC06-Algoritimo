# Entrada: Peça o valor do saque: valor = int(input("Quanto deseja sacar? R$ ")).

# Processamento:

# Use uma variável para controlar o total que ainda precisa ser pago.

# Use uma variável para a cedula_atual (começando por 50).

# Use um contador para saber quantas cédulas de cada valor estão sendo "entregues".

# Saída: Sempre que mudar de nota (ex: de 50 para 20), exiba o total de notas daquela denominação se ele for maior que zero.


# Entrada
valor = int(input("Quanto deseja sacar? R$ "))

# Processamento
total_restante = valor  # Controla o que falta pagar
cedula_atual = 50       # Começa pela maior nota
total_cedulas = 0       # Contador de notas de cada denominação

while True:
    if total_restante >= cedula_atual:
        # Se o valor restante permite tirar a nota atual
        total_restante -= cedula_atual
        total_cedulas += 1
    else:
        # Se não dá mais para tirar a nota atual, imprime o resultado (se houver)
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R$ {cedula_atual}")
        
        # Lógica de troca de nota
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        
        # Zera o contador para a nova nota
        total_cedulas = 0
        
        # Se o valor chegou a zero, para o loop
        if total_restante == 0:
            break