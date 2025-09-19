// VJ enumerators
#include <iostream>
using namespace std;

enum Options {
    List = 1,
    Add,
    Update
};

enum class Action {
    List = 1,
    Add,
    Update
};

int main() {
    /*
    What is enumeration?
        Literally a list of things
    How do you build enumeration?
        enum Name {item1, item2, item3};
    How do we display our enumerator? 
        Just use the name of the enumerator
    Why does it matter that enumerators are constants??
        Can't update it
    What is the default beginning enumerator? 
        0
    How do you give a different default value?
        enum Name {item1 = 1, item2, item3};
    What is a strongly typed enumerator?
        enum class Name {item1, item2, item3};
    How are strongly typed enumerators different from a normal one?
        Can't implicitly convert to int
    */

   cout <<
    "1. List\n"
    "2. Add\n"
    "3. Update\n"
    "Choose an option: ";
    int choice;
    cin >> choice;

    if (choice == static_cast<int>(Actoin::List)) {
        cout << "You chose list\n";
    } else if (choice == Options::Add) {
        cout << "You chose add\n";
    } else if (choice == Options::Update) {
        cout << "You chose update\n";
    } else {
        cout << "Invalid choice\n";
    }

    return 0;
}