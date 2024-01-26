<?php

function calculateWinner($games) {
    $rules = [
        "🗿" => ["✂️", "🦎"],
        "📄" => ["🗿", "🖖"],
        "✂️" => ["📄", "🦎"],
        "🦎" => ["📄", "🖖"],
        "🖖" => ["🗿", "✂️"]
    ];

    $score = ["Player 1" => 0, "Player 2" => 0];

    foreach ($games as $game) {
        if ($game[0] == $game[1]) {
            continue;
        }

        if (in_array($game[1], $rules[$game[0]])) {
            $score["Player 1"]++;
        } else {
            $score["Player 2"]++;
        }
    }

    if ($score["Player 1"] == $score["Player 2"]) {
        return "Tie";
    }

    return $score["Player 1"] > $score["Player 2"] ? "Player 1" : "Player 2";
}

$games = [["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]];
echo calculateWinner($games);

?>