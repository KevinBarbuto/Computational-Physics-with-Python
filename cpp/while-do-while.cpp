#include <iostream>
using namespace std;

int main()
{
    int index = 1;

    while(index <= 5) { // Standard "while" loop
        cout << index << endl;
        index++;
    }

    do { // "Do while" loop, executes code before checking conditions
        cout << index << endl;
        index++;
    } while(index <= 5);

    return 0;
}
