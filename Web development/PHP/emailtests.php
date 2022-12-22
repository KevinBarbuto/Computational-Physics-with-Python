<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Testing</title>
  </head>
  <body>
    
    <?php
      
      // Improper email
      $email = "kevinb(ar)but:::o@gm//ail.com";
      echo "$email <br><br>";
      
      // Sanitize email
      $email = filter_var($email, FILTER_SANITIZE_EMAIL);
      echo "$email <br><br>";
      
      // Validate email
      if(filter_var($email, FILTER_VALIDATE_EMAIL)){
          echo "This is a valid email. Good job.";
      } else {
          echo "This is not a valid email.";
      }
      
     ?>
    
  </body>
</html>
