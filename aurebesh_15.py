import argparse

def espanol_a_aurebesh(texto):
    # Diccionario de mapeo de español a Aurebesh
    aurebesh_dict = {
        'a': 'Aurek', 'b': 'Besh', 'c': 'Cresh', 'd': 'Dorn',
        'e': 'Enth', 'f': 'Forn', 'g': 'Grek', 'h': 'Herf',
        'i': 'Isk', 'j': 'Jenth', 'k': 'Krill', 'l': 'Leth',
        'm': 'Mern', 'n': 'Nern', 'o': 'Osk', 'p': 'Peth',
        'q': 'Qek', 'r': 'Resh', 's': 'Senth', 't': 'Trill',
        'u': 'Usk', 'v': 'Vev', 'w': 'Wesk', 'x': 'Xesh',
        'y': 'Yirt', 'z': 'Zerek', ' ': ' ', '.': 'Enko',
        ',': 'Trill', '?': 'Thesh', '!': 'Dorn', '0': 'Nen',
        '1': 'Enth', '2': 'Yirt', '3': 'Enko', '4': 'Forn',
        '5': 'Dorn', '6': 'Resh', '7': 'Osk', '8': 'Cresh',
        '9': 'Thesh'
    }

    # Transformar el texto a Aurebesh
    aurebesh_texto = ''
    for char in texto.lower():
        aurebesh_texto += aurebesh_dict.get(char, char) + ' '

    return aurebesh_texto

if __name__ == "__main__":
    texto = input("Por favor, introduce el texto que quieres convertir a Aurebesh: ")
    print(espanol_a_aurebesh(texto))
