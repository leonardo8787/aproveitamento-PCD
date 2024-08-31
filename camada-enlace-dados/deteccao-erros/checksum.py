def checksum(data):
    """Calcula o checksum simples de uma string binária"""
    sum = 0
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        sum += int(byte, 2)
    return bin(~sum & 0xFF)[2:].zfill(8)

def main_checksum():
    data = '10101100'  # Exemplo de string binária
    checksum_value = checksum(data)
    print(f"Checksum: {checksum_value}")