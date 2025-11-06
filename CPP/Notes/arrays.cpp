// Arrays
/*
How are for loops constructed in C++
    for (initialization; condition; increment) {
        // code to be executed
    }
When do you need to use curly brackets in C++
    Curly brackets are used to define the beginning and end of a block of code, such as in functions, loops, and conditionals.
How do you compare items in arrays
    You can compare items in arrays using relational operators (==, !=, <, >, <=, >=).
How do you use an array as an argument in a function
    You can pass an array to a function by specifying the array name without brackets. You may also need to pass the size of the array as an additional argument.
What is type_t
    type_t is not a standard C++ type. It might be a placeholder for a specific type in a given context or library. In standard C++, you would typically use built-in types like int, float, char, etc.
Why would we use type_t
    Since type_t is not a standard C++ type, its usage would depend on the specific context or library. Generally, using typedefs or type aliases can help improve code readability and maintainability.
How do you search an array
    You can search an array using a loop to iterate through the elements and check for a specific value. Alternatively, you can use algorithms from the <algorithm> header, such as std::find.
How do you sort an array
    You can sort an array using algorithms from the <algorithm> header, such as std::sort.
How do you make a multi-dimensional array
    You can create a multi-dimensional array by defining an array with multiple sets of brackets. For example, int matrix[3][4] creates a 2D array with 3 rows and 4 columns.
*/
#include <iostream>
using namespace std;

string days[7] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};

int main() {
    cout << "Days of the week:" << endl;
    for (int i = 0; i < 7; i++) {
        cout << days[i] << " ";
    }
    cout << endl;
    return 0;
}