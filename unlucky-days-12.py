import calendar
import sys

def friday_13(year):
    # Define una lista para almacenar las fechas de los viernes 13 y martes 13
    fechas = []

    # Itera sobre cada mes del año
    for mes in range(1, 13):
        # Usa la función 'weekday' para obtener el día de la semana de 13 de ese mes
        # 'weekday' devuelve 0 para lunes, 1 para martes, ..., 4 para viernes, etc.
        dia_semana = calendar.weekday(year, mes, 13)
        if dia_semana == 4:
            # Si es viernes, agrega la fecha a la lista
            fechas.append(f"Viernes 13-{mes}-{year}")
        elif dia_semana == 1:
            # Si es martes, agrega la fecha a la lista
            fechas.append(f"Martes 13-{mes}-{year}")

    # Imprime todas las fechas de los viernes 13 y martes 13
    for fecha in fechas:
        print(fecha)

if __name__ == "__main__":
    # Usa el primer argumento de línea de comandos como el año
    year = int(sys.argv[1])
    friday_13(year)
