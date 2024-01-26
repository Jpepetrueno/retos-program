def sorting_hat():
    questions = [
        {
            "question": "¿Qué valoras más en la vida?",
            "options": [
                "Valor y coraje",
                "Poder y ambición",
                "Lealtad y justicia",
                "Sabiduría e inteligencia",
            ],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
        {
            "question": "Si te encuentras con un obstáculo en tu camino, ¿qué haces?",
            "options": [
                "Lo enfrento sin dudar",
                "Busco una manera de usarlo en mi beneficio",
                "Ayudo a otros a superarlo",
                "Lo estudio para entenderlo mejor",
            ],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
        {
            "question": "¿Cómo te describirías a ti mismo?",
            "options": [
                "Valiente y audaz",
                "Astuto y ambicioso",
                "Trabajador y leal",
                "Inteligente y creativo",
            ],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
        {
            "question": "¿Qué es lo que más te gustaría aprender en Hogwarts?",
            "options": [
                "Defensa contra las artes oscuras",
                "Pociones y artes oscuras",
                "Herbología",
                "Encantamientos y astronomía",
            ],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
        {
            "question": "¿Cómo reaccionas ante la adversidad?",
            "options": [
                "Con valentía, enfrentándola de frente",
                "Con astucia, buscando la manera de salir beneficiado",
                "Con paciencia, trabajando duro para superarla",
                "Con sabiduría, buscando aprender de la experiencia",
            ],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
        {
            "question": "Si pudieras tener un superpoder, ¿cuál sería?",
            "options": ["Superfuerza", "Invisibilidad", "Curación", "Telepatía"],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
        {
            "question": "¿Qué tipo de líder serías?",
            "options": [
                "Uno que lidera con valentía en el frente",
                "Uno que lidera con astucia y estrategia",
                "Uno que lidera con justicia y equidad",
                "Uno que lidera con sabiduría e innovación",
            ],
            "weights": {
                "Gryffindor": 0,
                "Slytherin": 1,
                "Hufflepuff": 2,
                "Ravenclaw": 3,
            },
        },
    ]

    scores = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")
        answer = int(input("Elige una opción: ")) - 1
        for house, weight in question["weights"].items():
            if weight == answer:
                scores[house] += 1

    return max(scores, key=scores.get)


print(f"¡Bienvenido a {sorting_hat()}!")
