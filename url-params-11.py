def get_params(url):
    partes = url.split('?')
    if len(partes) < 2:
        return "La url no tiene parámetros."

    parametros = partes[1].split('&')

    valores = {}

    for parametro in parametros:
        nombre, valor = parametro.split('=')
        
        valores[nombre] = valor

    return valores

url = 'https://retosdeprogramacion.com?year=2023&challenge=0'

print(get_params(url))
