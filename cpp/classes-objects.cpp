#include <iostream>
using namespace std;

class Book {
    public:
        string title;
        string author;
        int pages;

};


int main()
{

    Book book1;
    book1.title = "The Lord of the Rings";
    book1.author = "J.R.R. Tolkien";
    book1.pages = 1077;

    Book book2;
    book2.title = "The Handmaid's Tale";
    book2.author = "Margaret Atwood";
    book2.pages = 303;

    cout << book2.pages;


    return 0;
}
