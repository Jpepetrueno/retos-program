<?php

// Incluimos la librería Simple HTML DOM Parser
require_once 'simple_html_dom.php';

// Definimos la URL de la página web del evento
$url = 'https://holamundo.day';

// Creamos un objeto DOM a partir de la URL
$html = file_get_html($url);

// Buscamos el elemento que contiene la agenda del día 8
$agenda = $html->find('div[id=day8]', 0);

// Si encontramos el elemento, lo recorremos y extraemos la hora y la información de cada evento
if ($agenda) {
    foreach ($agenda->find('div.event') as $event) {
        $time = $event->find('span.time', 0)->plaintext;
        $info = $event->find('span.info', 0)->plaintext;
        echo "$time | $info\n";
    }
} else {
    // Si no encontramos el elemento, mostramos un mensaje de error
    echo "No se ha encontrado la agenda del día 8\n";
}

?>