// Vincent Johnson - Changing Strings
// g++ chng_str.cpp -o chng_str
#include <iostream>
#include <string>
#include<vector>
using namespace std;
/*
How do I get a substring from within a string?
    substr()
How do I create an escape character in C++
    Use a backslash (\) before the character you want to escape.
How do I convert a string to another data type?
    Use functions like stoi(), stof(), stod() for converting strings to int, float, and double respectively.
What is a raw string and when would I use it?
    A raw string is a string literal that ignores escape sequences. File paths.
*/
int main() {
    string str1 = "Hello World";
    vector<vector<string>> vec = {{"Hello", "World"}, {"Goodbye", "World"}};
    cout << vec[0][0] << endl;
    auto index = str1.find(" ");
    string hi = str1.substr(0, index);
    string earth = str1.substr(index + 1);
    cout << hi << endl;
    cout << earth << endl;
    return 0;
}