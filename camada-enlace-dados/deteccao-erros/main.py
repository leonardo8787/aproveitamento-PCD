
from crc import main_crc
from checksum import main_checksum
from parity import main_parity
from hamming import main_hamming

def main():
    print("Executando CRC:")
    main_crc()
    print("\nExecutando Checksum:")
    main_checksum()
    print("\nExecutando Bits de Paridade:")
    main_parity()
    print("\nExecutando Código de Hamming:")
    main_hamming()

if __name__ == "__main__":
    main()
