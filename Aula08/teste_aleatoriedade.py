import time  # Importa o módulo de tempo para usar o relógio do PC como semente

# --- CONFIGURAÇÃO DO GERADOR ---

# 1. Definimos a "Semente" (Seed)
# Usamos o tempo atual (segundos desde 1970) multiplicado por 1000 para ter milissegundos.
# Isso garante que, a cada vez que você rodar, o valor inicial seja diferente.
semente = int(time.time() * 1000)

# 2. Constantes Matemáticas (Padrão LCG - Linear Congruential Generator)
# Esses números são escolhidos por matemáticos para que o resultado pareça "caótico".
A = 1103515245   # Multiplicador: define como a semente será "embaralhada"
C = 12345        # Incremento: adiciona um valor para evitar que caia em zero
M = 2**31        # Módulo: o limite máximo que o cálculo interno pode atingir

# --- A FUNÇÃO DO SORTEIO ---

def meu_random():
    global semente  # Avisa que vamos atualizar a semente global a cada sorteio
    
    # PASSO 1: O Cálculo Matemático
    # Multiplicamos a semente, somamos o incremento e pegamos o resto da divisão pelo Módulo.
    # Isso gera um número novo e gigante que será a semente para o PRÓXIMO sorteio.
    semente = (A * semente + C) % M
    
    # PASSO 2: Ajuste de Escopo
    # O número em 'semente' é enorme. Usamos o % 2001 para que o resto da divisão
    # seja sempre um número entre 0 e 2000.
    resultado_final = semente % 2001
    
    return resultado_final

# --- TESTE DO CÓDIGO ---

print(f"Semente inicial baseada no relógio: {semente}")
print("-" * 30)

# Vamos gerar 5 números para ver se estão variando:
for i in range(1, 6):
    numero = meu_random()
    print(f"{i}º número sorteado: {numero}")
