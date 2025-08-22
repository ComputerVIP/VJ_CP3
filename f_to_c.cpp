#include <iostream>
using namespace std;

int main() {
    int n;

    cout << "Enter temperature in Fahrenheit: ";
    cin >> n;
    int c = (n - 32) * 5 / 9;
    cout << "Temperature in Celsius: " << c << "°C" << endl;

    return 0;
}