<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Testing</title>
  </head>
  <body>
    
    <?php
    class Book {
        var $title;
        var $author;
        var $pages;
        
        function __construct($aTitle, $aAuthor, $aPages){
            $this->title = $aTitle;
            $this->author = $aAuthor;
            $this->pages = $aPages;
        }
    }
    
    $book1 = new Book("The Road", "Cormac McCarthy", 400);
    $book2 = new Book("Moby Dick", "Herman Melville", 500);
    
    echo $book1->title;
    
     ?>
    
  </body>
</html>
