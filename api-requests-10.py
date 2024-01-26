import requests

def get_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    data = response.json()
    return data

def main():
    pokemon_name = "pikachu"  # Puedes cambiar esto por el nombre de cualquier Pokémon
    data = get_pokemon_data(pokemon_name)
    print(data)

if __name__ == "__main__":
    main()
