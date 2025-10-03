// g++ binaries_l.cpp -o app -mconsole
#include <iostream>
#include <fstream>
#include <vector>
/*
istringstream - > Read
ostringstream - > Write
stringstream - > Read and Write
*/

using namespace std;
/*
What is a potential issue with converting values to strings without control?
    Random values
How can you control the way a value is converted to a string?
    Using stringstream
Why is it useful to create a reusable function for converting values to strings?
    To avoid rewriting code
What is parsing in the context of working with strings?
    Extracting specific information from a string
How do you extract specific information from a string in programming?
    Using stringstream and getline
When a title contains a space, which function should you use to read it properly?
    getline
Why might extra zeros be added to a string when converting a value without control?
    Default formatting
How does controlling the string conversion process benefit your program?
Give an example scenario where parsing a string would be necessary in a program.
Why are images, audio, and PDFs not readable by humans when stored in files?
What file extensions are commonly used to create binary files?
When writing to a binary file, what does the first parameter (reinterpret_cast<char*>(&numbers)) represent?
Why does the binary file only take 12 bytes while the array of integers might be larger?
How does reading individual numbers from a binary file differ from reading the entire list at once?
What is the main difference between sequential search and binary search?
In which type of data structure is binary search most efficient?
What is a key requirement for binary search to work correctly on a list?
How does sequential search find an item in a list?
Why is binary search generally faster than sequential search for large, sorted lists?
*/

struct Person {
    string name;
    int age;
    double height;
};
struct Movie {
    string title;
    int year;
};

Movie parseMovie(string str){
        stringstream stream;
        stream.str(str);

        Movie movie;
        getline(stream, movie.title, ',');
        stream >> movie.year;
        return movie;
    }

vector<Person> people;

int main(){
    auto movie = parseMovie("The Dark Knight,2008");
    

    double num = 123.456789;
    string str = to_string(num);
    cout << str << endl;
    fstream file;
    file.open("people.txt", ios::in | ios::out | ios::app);
    if (file.is_open()) {

        file.close();
    }

    people.push_back({"Alice", 30, 5.5});
    people.push_back({"Bob", 25, 6.0});

    ofstream outfile("people.bin", ios::binary);
    if (!outfile) {
        cerr << "Error creating binary file." << endl;
        return 1;
    }
    for (const auto& person : people) {
        size_t nameLen = person.name.size();
        outfile.write(reinterpret_cast<const char*>(&nameLen), sizeof(nameLen));
        outfile.write(person.name.c_str(), nameLen);
        outfile.write(reinterpret_cast<const char*>(&person.age), sizeof(person.age));
        outfile.write(reinterpret_cast<const char*>(&person.height), sizeof(person.height));
    }
    outfile.close();

    ifstream infile("people.bin", ios::binary);
    if (!infile) {
        cerr << "Error opening binary file." << endl;
        return 1;
    }
    while (infile.peek() != EOF) {
        Person person;
        size_t nameLen;
        infile.read(reinterpret_cast<char*>(&nameLen), sizeof(nameLen));
        person.name.resize(nameLen);
        infile.read(&person.name[0], nameLen);
        infile.read(reinterpret_cast<char*>(&person.age), sizeof(person.age));
        infile.read(reinterpret_cast<char*>(&person.height), sizeof(person.height)); // reinterpret variable type, then size?

        fstream file;
        file.open("people.txt", ios::in | ios::out | ios::app);
        if (file.is_open()) {
            cout << "Writing to text file" << endl;
            try{
                file << "Name: " << person.name << ", Age: " << person.age << ", Height: " << person.height << endl;
            }
            catch(...){
                cerr << "Error writing to text file." << endl;
            }
            
            
        }
    }
    file.close();
    infile.close();

    return 0;
}