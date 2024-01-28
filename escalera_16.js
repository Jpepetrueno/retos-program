function dibujarEscalera(n) {
    if (n == 0) {
        console.log("__");
        return;
    }

    let escalones = Math.abs(n);
    let escalera = "";

    for (let i = 0; i < escalones; i++) {
        let espacios = "  ".repeat(i);
        let escalon = "|_";
        escalera += espacios + escalon + "\n";
    }

    if (n < 0) {
        escalera = escalera.split("\n").reverse().join("\n");
    }

    console.log(escalera);
}

dibujarEscalera(-4);