<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Testing</title>
  </head>
  <body>
  
    <form action="site.php" method="get">
      Name: <br><input type="text" name="username">
      <br>
      Age: <br><input type="text" name="age">
      <br><input type="submit">
    </form>
    <br>
    <?php if( isset($_GET["username"]) && isset($_GET["age"]) ): ?>
      Your name is <?php echo $_GET["username"] ?>
      <br>
      Your age is <?php echo $_GET["age"] ?>
    <?php endif; ?>
  </body>
</html>
