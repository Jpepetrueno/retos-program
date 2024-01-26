def tennis_match(points):
    score_map = {0: "Love", 1: "15", 2: "30", 3: "40"}
    p1_score = 0
    p2_score = 0

    for point in points:
        if point == "P1":
            p1_score += 1
        elif point == "P2":
            p2_score += 1

        if p1_score >= 3 and p2_score >= 3:
            if abs(p1_score - p2_score) >= 2:
                print("Ha ganado el " + point)
                return
            elif p1_score == p2_score:
                print("Deuce")
            else:
                print("Ventaja " + point)
        else:
            print(
                score_map.get(p1_score, "Game")
                + " - "
                + score_map.get(p2_score, "Game")
            )


points_match = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
tennis_match(points_match)
