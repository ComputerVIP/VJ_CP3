#include <iostream>
#include <string>

using namespace std;
// g++ structures.cpp -o struct
/*
What are structures?
    A structure is a data type that allows you to group different types of variables under one name.
How do you build a structure?
    struct
What can be held in a structure?
    Variables of different types
How do you access the information in a structure?
    name.variable = value;
How do you overload an operator
    bool operator==(const StructName &other) const {
        return (this->var1 == other.var1) && (this->var2 == other.var2);
    }
*/
struct Car {
    string make;
    string model;
    int year;
    float mileage;
};
int main() {
    Car camero;
    camero.make = "Chevrolet";
    camero.model = "Camero";
    camero.year = 2020;
    camero.mileage = 15000.5;
    cout << camero.make << " " << camero.model << " " << camero.year << " " << camero.mileage << endl;
    return 0;
}