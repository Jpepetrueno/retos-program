def dibuja_escalera(n):
    if n == 0:
        print("Sin escalera: ")
        print("__")
    elif n > 0:
        print("Escalera que sube: ")
        for i in range(n):
            print("  " * (n - i - 1) + "_|")
    else:
        print("Escalera que baja: ")
        for i in range(-n):
            print("  " * (i + 1) + "|_")


if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de peldaños de la escalera: "))
    dibuja_escalera(n)
