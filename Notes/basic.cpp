// VJ Variables
#include <iostream>
using namespace std;

// int = 4bytes
// short = 2bytes
// long = 4bytes
// long long = 8bytes
// float = 4bytes
// double = 8bytes
// long double = 16bytes
// char = 1byte
// bool = 1byte
// string = 24bytes

int main() {
    int a = 10; // Integer variable
    float pi = 3.141592653589793264628f; // Floating-point variable, need f at end or becomes double
    const char c = 'C'; // Character variable
    bool d = true; // Boolean variable
    long num = 1234567890l; // Long integer variable, need l at end
    long long big_num = 1234567890123456789ll; // Long long integer variable, need ll at end

    std::cout << "Integer: " << a << std::endl;
    std::cout << "Float: " << pi << std::endl;
    std::cout << "Character: " << c << std::endl;
    std::cout << "Boolean: " << d << std::endl;
    std::cout << "Long: " << num << std::endl;
    std::cout << "Long Long: " << big_num << std::endl;

    cout << "Enter a number: ";
    int n;
    cin >> n;
    cout << "You entered: " << n << endl;
    return 0;
}

/*
How are static and dynamically typed variables different?
         You have to specify the type of variable
REMINDER: What is the difference between instantiating and declaring a variable?
        Declaring makes it with a value, instantiating makes space for it
What case type should be used for c++ variables?
    snake_case
What is the C++ standard library?
    What makes C++ better than C--
How do you access the standard library?
    #include <iostream>
How do you create an output in C++?
    cout
How do you create an input in C++?
    cin
What is the stream in C++?
    The flow of data
What is a constant?
    Values within program that should not be changed
Why do we write constants?
    To prevent accidental changes
*/