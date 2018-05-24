<html>
  <body>
    <p>Is is working?</p>

    <?php

    try
    {
      $pdo = new PDO('mysql:host=localhost;dbname=dbRealivent.db;charset=utf8', 'root', '');
    }
    catch (Exception $e)
    {
      die('Erreur : ' . $e->getMessage());
    }

    $sql = 'SELECT * FROM User';
    $req = $pdo->query($sql);

    ?>

    <table class="table table-bordered">
     <caption>Membres de Realivents</caption>
    <tr>
        <th><p class="text-error">Prénom</p></th>
        <th><p class="text-error">Nom</p></th>
        <th><p class="text-error">Email</p></th>
        <th><p class="text-error">Mot de passe</p></th>
      <th><p class="text-error">Statut du compte</p></th>
      <th><p class="text-error">Profil</p></th>

        </tr>
    <tr>

      <? while($row = $req->fetch())
      {
        ?>
            <td><? echo $row['first_name']; ?></td>
            <td><? echo $row['last_name']; ?></td>

            <td><? echo $row['email']; ?></td>
            <td><? echo $row['password']; ?></td>
        <td><? if ($row['is_staff'] == "False") { echo 'Membre'; } if ($row['is_staff'] == "True") { echo '<p class="text-warning"><strong>Administrateur</strong></p>'; } ?></td>
        <td><? echo '<a class="btn btn-info" href="profil?user='.$row['first_name'].'">Voir le profil</a><br/>'; ?></td>




    </tr>
    <? }
    $req->closeCursor();
    ?>
    </table>
  </body>
</html>
