<?php

//$bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', ''); //MySQL

$bdd = new SQLite3('mysqlitedb.db');

//$reponse = $bdd->query('Tapez votre requête SQL ici');

$nombre_events = $bdd->query('SELECT COUNT(*) FROM Event, User WHERE Event.participant');


for ($i = 1; $i <= $nombre_events; $i++)
{

    echo 'Ceci est la ligne n°' . $nombre_de_lignes;
    $event_name = $bdd->query('SELECT  FROM table');
    $event_date = $bdd->query('SELECT COUNT(*) FROM table');
    echo 'Nom de l\'événement : ' . $event_name;
    echo 'Date de l\'événement : ' . $event_date;

}

?>






<?php
/*
while ($nombre_events <= 100)
{
  echo 'Je ne dois pas regarder les mouches voler quand j\'apprends le PHP.<br />';
  $nombre_de_lignes++; // $nombre_de_lignes = $nombre_de_lignes + 1
}


*/
?>
