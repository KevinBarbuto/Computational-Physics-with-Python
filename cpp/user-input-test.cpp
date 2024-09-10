#include <iostream>
#include <cmath>

using namespace std;

int main()
{

    string name;
    cout << "Enter your name: ";
    getline(cin, name);

    cout << "Hello " << name << endl;

    int age;
    cout << "Enter your age: ";
    cin >> age;

    cout << "You are " << age << " years old";


    return 0;
}
