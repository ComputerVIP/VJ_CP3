// VJ Strings, arrays, conditionals
#include <iostream>

using namespace std;

int main() {
    // Strings
    string str = "Hello, World!";
    cout << str << endl;

    // String concatenation
    string firstName = "John";
    string lastName = "Doe";
    string fullName = firstName + " " + lastName;
    cout << "Full Name: " << fullName << endl;

    // String length
    cout << "Length of Full Name: " << fullName.length() << endl;

    // Accessing characters in a string
    cout << "First character of Full Name: " << fullName[0] << endl;

    // Arrays
    int numbers[] = {1, 2, 3, 4, 5};
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);
    cout << "Array elements: ";
    for (int i = 0; i < arraySize; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;

    // Conditional statements
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age < 18) {
        cout << "You are a minor." << endl;
    } else if (age >= 18 && age < 65) {
        cout << "You are an adult." << endl;
    } else {
        cout << "You are a senior citizen." << endl;
    }

    return 0;
}