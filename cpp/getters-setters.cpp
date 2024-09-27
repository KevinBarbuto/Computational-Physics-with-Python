#include <iostream>
using namespace std;

class Movie {
    private:
        string rating;
    public:
        string title;
        string director;

        Movie(string aTitle, string aDirector, string aRating){
            title = aTitle;
            director = aDirector;
            setRating(aRating);
        }

        void setRating(string aRating){
            if(aRating == "G" || aRating == "PG" || aRating == "PG-13" || aRating == "R" || aRating == "NR"){
                rating = aRating;
            } else {
                rating = "NR";
            }
        }

        string getRating(){
            return rating;
        }

};


int main()
{
    Movie titanic("Titanic", "James Cameron", "PG-13");

    // titanic.setRating("Dog");

    cout << titanic.getRating();

    return 0;
}
