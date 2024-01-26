def pseudo_random_generator(seed, a=1664525, c=1013904223, m=2**32):
    while True:
        seed = (a * seed + c) % m
        yield seed % 101  # Devuelve un número entre 0 y 100

# Crea el generador
generator = pseudo_random_generator(0)  # Puedes cambiar la semilla a cualquier número

# Genera algunos números pseudoaleatorios
for _ in range(10):
    print(next(generator))
