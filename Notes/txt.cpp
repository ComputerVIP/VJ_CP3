#include <iostream>
#include <fstream>
#include <string>
#include <limits>
#include <iomanip>

using namespace std;
/*
What are the 3 main sources of data for a program
    Terminal, files, network
What are streams?
    Where or what you're getting the data from
What are the different streams we might need to include in a program? 
    iostream, fstream, sstream
What is the base class for all streams?
    ios
What is buffer?
    Temp storage for data being transferred
How do you clear the buffer?
    cin.ignore()
How do you handle invalid inputs from the terminal
What streams are for files specifically
How do you write to a text file?
What do stream manipulators let us do?
How do you write to a CSV?
How do you read a text file?
How do you read a CSV file?
What is a delimiter?
How do you read an entire CSV?
How do you turn items from a CSV into objects of a structure?
*/

/*
int main() {
    int num;
    cin << num;
    cin.ignore(numeric_limits<streamsize>::max()); // Clear the buffer

    cout << num << endl;

    while (true) {
        int mun;
        cin >> mun;
        if (cin.fail()){
            cin.clear(); // Clear the fail state
            cin.ignore(numeric_limits<streamsize>::max());
        } else break{
            cout << mun << endl;
        }
    }

    return 0;
}
    */

int main() {
    ofstream file;
    file.open("tep.txt");
    if (file.is_open()) {
        file << setw(20)<< "Hello, Gay Larson" << endl;
    }
    file.close();
    return 0;
}