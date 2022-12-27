<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Testing</title>
  </head>
  <body>
    
    <?php
    
    class Chef {
        function makeChicken(){
            echo "The chef makes chicken.";
        }
        
        function makeSpecialDish(){
            echo "The chef makes toast.";
        }
    }
    
    class ItalianChef extends Chef{
        function makeSpecialDish(){
            echo "The chef makes pasta.";
        }
    }
    
    $chef = new Chef;
    echo $chef->makeChicken();
    echo $chef->makeSpecialDish();
    
    $ichef = new ItalianChef;
    echo $ichef->makeSpecialDish();
    
     ?>
    
  </body>
</html>
