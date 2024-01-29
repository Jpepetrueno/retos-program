const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Ingresa el texto que deseas analizar: ', function(texto) {
    let palabras = texto.split(' ');
    let totalPalabras = palabras.length;
    let totalOraciones = texto.split('.').length - 1;
    let totalLongitud = 0;
    let palabraMasLarga = '';
    let totalCaracteres = texto.length;

    for (let i = 0; i < totalPalabras; i++) {
        totalLongitud += palabras[i].length;
        if (palabras[i].length > palabraMasLarga.length) {
            palabraMasLarga = palabras[i];
        }
    }

    let longitudMedia = totalLongitud / totalPalabras;
    let longitudPalabraMasLarga = palabraMasLarga.length;

    console.log({
        totalPalabras: totalPalabras,
        longitudMedia: longitudMedia,
        totalOraciones: totalOraciones,
        palabraMasLarga: palabraMasLarga,
        longitudPalabraMasLarga: longitudPalabraMasLarga,
        totalCaracteres: totalCaracteres
    });

    rl.close();
});