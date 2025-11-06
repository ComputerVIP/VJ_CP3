// VJ Strings, arrays, conditionals
#include <iostream>

using namespace std;

/*
What is Narrowing?
    Narrowing is when you convert a larger data type to a smaller data type
What is a basic way to generate random numbers in C++?
What is an array?
    List of variables of the same type
How do I create an array?
    datatype name[size] = {values};
How do you make strings in C?
    char str[] = "Hello";
How did C++ improve creating strings? 
    char str[6] = "Hello";
How do I search a string?
    str.find("substring");
How do I modify a string?
    str.replace(start_index, length, "new_substring");
What are some string methods? 
    .length(), .find(), .replace(), .substr()
*/

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