def crc_remainder(data, polynomial, initial_remainder=0):
    """Calcula o CRC usando divisão polinomial"""
    data = list(data)  
    poly = list(polynomial)
    remainder = initial_remainder

    for bit in data:
        remainder = (remainder << 1) ^ (int(bit) if bit == '1' else 0)
        if remainder & (1 << (len(poly) - 1)):
            remainder ^= int(''.join(poly), 2)

    return bin(remainder)[2:].zfill(len(poly) - 1)

def main_crc():
    data = '1011001'
    polynomial = '1101'
    remainder = crc_remainder(data, polynomial)
    print(f"CRC Remainder: {remainder}")