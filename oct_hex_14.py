import argparse


def decimal_to_oct_hex(n):
    # Convertir a octal
    octal = ""
    temp = n
    while temp > 0:
        octal = str(temp % 8) + octal
        temp = temp // 8

    # Convertir a hexadecimal
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    temp = n
    while temp > 0:
        hexadecimal = hex_chars[temp % 16] + hexadecimal
        temp = temp // 16

    return octal, hexadecimal

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a decimal to octal and hexadecimal.')
    parser.add_argument('n', type=int, help='The decimal number to convert.')
    args = parser.parse_args()

    # Prueba la función
    octal, hexadecimal = decimal_to_oct_hex(args.n)
    print(f"El numero decimal {args.n} es {octal} en octal y {hexadecimal} en hexadecimal.")

