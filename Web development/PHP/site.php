<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Testing</title>
  </head>
  <body>
    
    <?php
      
      function getMax($num1, $num2, $num3) {
          
          if ($num1 >= $num2 && $num1 >= $num3){
              return $num1;
          } elseif($num2 >= $num1 && $num2 >= $num3) {
              return $num2;
          } else {
              return $num3;
          }
      }
      
      echo getMax(3000, 3000, 400);
      
     ?>
    
  </body>
</html>
