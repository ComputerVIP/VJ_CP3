// Arrays

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