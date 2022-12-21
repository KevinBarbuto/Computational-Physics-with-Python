<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Testing</title>
  </head>
  <body>
    
    <form action="site.php" method="post">
      What was your grade?<br>
      <input type="text" name="grade">
      <input type="submit">
    </form>
    
    <?php
      
      if(isset($_POST["grade"])){
          $grade = $_POST["grade"];
          
          switch($grade){
              case "A":
                echo "You did great!";
                break;
              case "B":
                echo "You did well.";
                break;
              case "C":
                echo "You passed!";
                break;
              case "D":
                echo "lmao";
                break;
              case "F":
                echo "You failed. Better luck next time!";
                break;
              default:
                echo "Invalid grade";
          }
      }
      
     ?>
    
  </body>
</html>
