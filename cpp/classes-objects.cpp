#include <iostream>
using namespace std;

class Book {
    public:
        string title;
        string author;
        int pages;

        Book(){
            title = "no title";
            author = "no author";
            pages = 0;
        }

        Book(string aTitle, string aAuthor, int aPages){
            title = aTitle;
            author = aAuthor;
            pages = aPages;
        }

};


int main()
{

    Book book1("The Lord of the Rings", "J. R. R. Tolkien", 1077);

    Book book2("The Handmaid's Tale", "Margaret Atwood", 303);

    Book book3;

    cout << book1.title;

    return 0;
}
