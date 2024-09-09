#include <iostream>

using namespace std;

int main()
{

    cout << "String 1" << endl;
    cout << "String 2\n";
    cout << endl; // Line break?
    cout << "\n"; // Line Break 2?

    string phrase = "Giraffe Academy";
    cout << phrase.length() << endl; // Find length of string
    phrase[0] = 'B'; // Change specific character of string
    cout << phrase << endl;
    cout << phrase[2] << endl; // Call specific character

    cout << phrase.find("Academy", 0) << endl; // Search for substr
    // Second parameter of "find" function defines search start pos

    cout << phrase.substr(8, 3); // Define substring


    return 0;
}
