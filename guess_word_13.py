import random
import os


def guess_word():
    with open("./animales.txt", "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f]
    word = random.choice(words)
    hidden_word = hide_word(word)
    attempts = 5

    print(f"La palabra a adivinar es: {hidden_word}")
    print(f"Tienes {attempts} intentos")

    while attempts > 0:
        entrada = input("Introduce una letra o una palabra: ")

        if len(entrada) == 1:
            if entrada in word:
                hidden_word = update_hidden_word(word, hidden_word, entrada)
                print(f"¡Bien hecho! La palabra ahora es: {hidden_word}")
            else:
                attempts -= 1
                print(
                    f"¡Lo siento! Esa letra no está en la palabra. Te quedan {attempts} intentos."
                )
        elif entrada == word:
            print("¡Felicidades! Has adivinado la palabra.")
            return
        else:
            attempts -= 1
            print(f"¡Lo siento! Esa no es la palabra. Te quedan {attempts} intentos.")

        if "_" not in hidden_word:
            print("¡Felicidades! Has adivinado todas las letras de la palabra.")
            return

    print("¡Lo siento! Has agotado todos tus intentos.")


def hide_word(word):
    hidden_word = list(word)
    for _ in range(int(len(word) * 0.6)):
        indice = random.randint(0, len(hidden_word) - 1)
        hidden_word[indice] = "_"
    return "".join(hidden_word)


def update_hidden_word(word, hidden_word, letra):
    return "".join(
        [letra if letra == l else hidden_word[i] for i, l in enumerate(word)]
    )


def clear():
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Unix/Linux/MacOS/BSD
        os.system("clear")


if __name__ == "__main__":
    clear()
    guess_word()
