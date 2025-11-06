/*
#include <iostream>
using namespace std;

enum Operation { Multiply = 1, Divide, Add, Subtract };
int main() {
    cout << "Number 1, #2, type (1=*, 2=/, 3=+, 4=-, 0=exit): ";
    double num1, num2;
    int type;
    cin >> num1 >> num2 >> type;

    if (type == 0) {
        cout << "Goodbye!\n";
        return 1;  // <-- exit the whole program with code 1
    }

    if (type == Operation::Multiply) {
        cout << num1 * num2 << endl;
    } else if (type == Operation::Divide) {
        cout << num1 / num2 << endl;
    } else if (type == Operation::Add) {
        cout << num1 + num2 << endl;
    } else if (type == Operation::Subtract) {
        cout << num1 - num2 << endl;
    } else {
        cout << "Invalid operation" << endl;
    }
    return 0;
}
*/
#include <iostream>
using namespace std;enum Operation { Multiply = 1, Divide, Add, Subtract };int main() {cout << "Number 1, #2, type (1=*, 2=/, 3=+, 4=-, 0=exit): ";double num1, num2;int type;cin >> num1 >> num2 >> type;if (type == 0) {cout << "Goodbye!\n";return 1;}if (type == Operation::Multiply) {cout << num1 * num2 << endl;} else if (type == Operation::Divide) {cout << num1 / num2 << endl;} else if (type == Operation::Add) {cout << num1 + num2 << endl;} else if (type == Operation::Subtract) {cout << num1 - num2 << endl;} else {cout << "Invalid operation" << endl;}return 0;}