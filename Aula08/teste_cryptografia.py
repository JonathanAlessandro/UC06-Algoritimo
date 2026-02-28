semente_secreta = 987654321  # Esta é a CHAVE PRIVADA
A, C, M = 1103515245, 12345, 2**31

def gerar_key():
    global semente_secreta
    semente_secreta = (A * semente_secreta + C) % M
    return semente_secreta % 256  # Limitamos a 256 (tamanho de 1 byte/caractere), quanto maior o valor maior o numero de caracteres

def cifrar(texto):
    resultado = []
    for letra in texto:
        # Transforma letra em número, faz o XOR com o número aleatório e guarda
        codigo_original = ord(letra)
        codigo_cifrado = codigo_original ^ gerar_key()
        resultado.append(codigo_cifrado)
    return resultado

# --- TESTE ---
mensagem = "GITHUB é fera de mais "
print(f"Original: {mensagem}")

# Criptografando
codigos = cifrar(mensagem)
print(f"Cifrado (Lista de números): {codigos}")

# Para descriptografar, REINICIAMOS a semente com o MESMO valor
semente_secreta = 987654321 
original = "".join([chr(c ^ gerar_key()) for c in codigos])
print(f"Descriptografado: {original}")