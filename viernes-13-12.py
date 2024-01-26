import calendar


def friday_13():
    # Define una lista para almacenar las fechas de los viernes 13
    fechas = []
    year = int(input("Ingrese el año: "))

    # Itera sobre cada del año
    for mes in range(1, 13):
        # Usa la función 'weekday' para obtener el día de la semana de 13 de ese mes
        # 'weekday' devuelve 0 para lunes, 1 para martes, ..., 4 para viernes, etc.
        if calendar.weekday(year, mes, 13) == 4:
            # Si es viernes, agrega la fecha a la lista
            fechas.append(f"Viernes 13-{mes}-{year}")

        elif calendar.weekday(year, mes, 13) == 1:
            # Si es martes, agrega la fecha a la lista
            fechas.append(f"Martes 13-{mes}-{year}")

    # Imprime todas las fechas de los viernes 13
    for fecha in fechas:
        print(fecha)


if __name__ == "__main__":
    friday_13()
