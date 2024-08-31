def hamming_encode(data):
    """Codifica os dados usando o código de Hamming (7,4)"""
    data_bits = list(data)
    parity_bits = [0] * 3

    parity_bits[0] = (int(data_bits[0]) + int(data_bits[1]) + int(data_bits[3])) % 2
    parity_bits[1] = (int(data_bits[0]) + int(data_bits[2]) + int(data_bits[3])) % 2
    parity_bits[2] = (int(data_bits[1]) + int(data_bits[2]) + int(data_bits[3])) % 2

    return ''.join(map(str, parity_bits + [int(bit) for bit in data_bits]))

def hamming_decode(encoded):
    """Decodifica os dados usando o código de Hamming (7,4)"""
    parity_bits = [int(encoded[0]), int(encoded[1]), int(encoded[2])]
    data_bits = [int(encoded[3]), int(encoded[4]), int(encoded[5]), int(encoded[6])]

    parity_check = [
        (data_bits[0] + data_bits[1] + data_bits[3]) % 2,
        (data_bits[0] + data_bits[2] + data_bits[3]) % 2,
        (data_bits[1] + data_bits[2] + data_bits[3]) % 2
    ]

    error_position = parity_check[0] * 1 + parity_check[1] * 2 + parity_check[2] * 4
    if error_position:
        print(f"Erro detectado na posição {error_position}")
        encoded = list(encoded)
        encoded[error_position - 1] = '1' if encoded[error_position - 1] == '0' else '0'
        print(f"Corrigido: {''.join(encoded)}")

    return ''.join(map(str, encoded[3:]))

def main_hamming():
    data = '1011'  # 4 bits de dados
    encoded = hamming_encode(data)
    print(f"Encoded with Hamming: {encoded}")
    decoded = hamming_decode(encoded)
    print(f"Decoded Data: {decoded}")
