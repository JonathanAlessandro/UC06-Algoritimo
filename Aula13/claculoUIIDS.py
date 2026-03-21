import time
import os
import binascii

def gerar_uuid7_manual():
    # 1. Obter o timestamp atual em milissegundos (48 bits)
    # 1 bilhão de milissegundos garantem que o ID seja ordenável por tempo
    timestamp_ms = int(time.time() * 1000)
    
    # 2. Gerar 10 bytes de aleatoriedade (80 bits restantes após o tempo)
    random_bytes = os.urandom(10)
    
    # 3. Organizar os bits conforme a regra do UUID v7:
    # [48 bits: Time] [4 bits: Ver] [12 bits: Rand] [2 bits: Var] [62 bits: Rand]
    
    # Transformamos o timestamp em bytes (6 bytes = 48 bits)
    uuid_bytes = bytearray(timestamp_ms.to_bytes(6, byteorder='big'))
    
    # Adicionamos a aleatoriedade
    uuid_bytes.extend(random_bytes)
    
    # 4. Ajustar os bits de Versão (Setar o 7 no local correto)
    # O byte 6 deve começar com '0111' (versão 7)
    uuid_bytes[6] = (uuid_bytes[6] & 0x0f) | 0x70
    
    # 5. Ajustar os bits de Variante (Setar '10' no local correto)
    # O byte 8 deve começar com '10' (variante RFC 4122)
    uuid_bytes[8] = (uuid_bytes[8] & 0x3f) | 0x80
    
    # Retornar a string formatada (hexadecimal com hifens)
    h = binascii.hexlify(uuid_bytes).decode()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"

# Teste
for _ in range(3):
    print(gerar_uuid7_manual())
    time.sleep(0.001) # Espera 1ms para o próximo ser diferente no tempo