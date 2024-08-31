def calculate_parity(bits):
    """Calcula o bit de paridade par"""
    count = bits.count('1')
    return '0' if count % 2 == 0 else '1'

def add_parity_bit(data):
    """Adiciona um bit de paridade ao final da string binária"""
    parity_bit = calculate_parity(data)
    return data + parity_bit

def check_parity(data):
    """Verifica o bit de paridade"""
    bits, parity_bit = data[:-1], data[-1]
    return calculate_parity(bits) == parity_bit

def main_parity():
    data = '1010101'
    data_with_parity = add_parity_bit(data)
    print(f"Data with Parity Bit: {data_with_parity}")
    print(f"Parity Check: {check_parity(data_with_parity)}")
