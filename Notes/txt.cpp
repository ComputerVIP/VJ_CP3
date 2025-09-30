#include <iostream>
#include <fstream>
#include <sstream>
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
    if cin.fail()
What streams are for files specifically
    fstream, ifstream, ofstream
How do you write to a text file?
    ofstream file; file.open("file.txt"); file << "text"; file.close();
What do stream manipulators let us do?
    Format output
How do you write to a CSV?
    file << "item1,item2,item3\n";
How do you read a text file?
    getline(file, line)
How do you read a CSV file?
    getline(file, line, ',')
What is a delimiter?
    Character that separates items in a stream
How do you read an entire CSV?
     while loop with getline and a stringstream to parse each line by the delimiter
How do you turn items from a CSV into objects of a structure?
    Use a loop with getline and a stringstream to parse each line by the delimiter
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
        file << setw(20)<< "Hello, Nick Larson" << endl;
    }
    file.close();

    file.open("data.csv");
    if (file.is_open()) {
        file << "Name,Age,Height\n";
        file << "Vincent,16,5.7\n";
        file << "Johnson,16,5.9\n";
    }
    file.close();

    ifstream infile;
    infile.open("data.csv");
    if (infile.is_open()) {
        string line;
        getline(infile, line); // Skip header line
        while (getline(infile, line)) {
            stringstream ss(line);
            string name, age, height;
            getline(ss, name, ',');
            getline(ss, age, ',');
            getline(ss, height, ',');
            cout << "Name: " << name << ", Age: " << age << ", Height: " << height << endl;
        }
    }
    return 0;
}