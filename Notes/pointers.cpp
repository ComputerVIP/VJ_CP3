// Vincent Johnson, Pointers
// g++ pointers.cpp -o pointers
#include <iostream>
#include <vector>
using namespace std;


int numbers[] = {1,2,3,4,5};

void pass_pointer(int* list, int size) {
    cout << list << endl;
}

int main() {
    int var = 20;   // actual variable declaration
    int *ip;        // pointer variable

    ip = &var;  // store address of var in pointer variable

    cout << "Value of var variable: ";
    cout << var << endl;

    // print the address stored in pointer variable
    cout << "Address stored in ip variable: ";
    cout << ip << endl;

    // access the value at the address available in pointer
    cout << "Value of *ip variable: ";
    cout << *ip << endl;

    // Constant pointers
    const int *ptr = &var; // pointer to a constant integer
    const int val = 30;
    ptr = &val; // OK: ptr can point to another address

    int *const cptr = &var; // constant pointer to a constant integer
    const int val2 = 40;
    *cptr = 7;

    const int *const cp = &var; // constant pointer to a constant integer
    *cptr = 10; // Error: cannot change the value pointed to by cp
    //cptr = &val2; Error: cannot change the address cp points to

    pass_pointer(numbers, size(numbers));

    return 0;
}
/*
What is a pointer?
    Variable that holds the address of another variable.
Why do we use pointers?
    To find the variable! Literally a phonebook. Literally me.
How do I create a pointer
    Use the asterisk * symbol in the declaration.
What is indirection or de-referencing?
    Accessing the value at the address stored in the pointer. Using *.
What are constant pointers? How are the different types used?
    Variable that cannot change the address it points to.
How do you pass a pointer into a function?
    type* name
Why would you pass a pointer to a function?
    To modify the original variable.
How do you compare pointers?
    Compare the addresses they hold.
What is dynamic memory allocation?
    Allocating memory at runtime using new and delete.
What is the Stack?
    Memory for local variables, function calls.
What is the Heap?
    Memory for dynamic allocation, larger and more flexible.
What are smart pointers?
    Objects that manage the lifetime of dynamically allocated memory.
*/