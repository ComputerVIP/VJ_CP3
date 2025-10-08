// Vincent Johnson, Movie
// g++ main.cpp -o app `fltk-config --cxxflags --ldflags` -mconsole

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Choice.H>
#include <FL/fl_ask.H>
#include <string>
#include <limits>
#include <cctype>
#include <algorithm>

using namespace std;

struct Widgets {
    Fl_Input* input;
    Fl_Button* button;
    Fl_Button* add;
    Fl_Choice* choice;
};

struct Thng {
    string name;
    string director;
    int year;
    string genre;
    string rating;
};
vector<Thng> things;

void add_cb(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    Thng t;
    t.name = fl_input("What's the name of the movie?") ?: "";
    string nme = t.name;
    for (const auto& item : things) {
        if (nme.find(item.name) != std::string::npos) {
            fl_message("A movie with that name already exists!");
            return;
        }
    }

    t.director = fl_input("What's the director of the movie?") ?: "";
    const char* year_str = fl_input("What year was the movie released?");
    t.year = year_str ? stoi(year_str) : 0;
    t.genre = fl_input("What's the genre of the movie?") ?: "";
    t.rating = fl_input("What's the age-rating of the movie?") ?: "";
    things.push_back(t);

    ofstream file;
    file.open("movies.csv", ios::app);
    if (file.is_open()) {
        file << t.name << "," << t.director << "," << t.year << "," << t.genre << "," << t.rating << "\n";
        fl_message("Movie added successfully!");
    } else{
        fl_message("Could not open the file to add movie!");
    }
    file.close();
    return;
    

}


// Button callback
void button_cb(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    std::string query = widgets->input->value();

    if (query.empty()) {
        fl_message("Search term cannot be empty!");
        return;
    }

    int choice_index = widgets->choice->value(); // 0 = Name, 1 = Director
    std::stringstream ss;
    ss << "Matching Movies:\n";
    bool found = false;

    for (const auto& item : things) {
        bool match = false;
        switch (choice_index) {
            case 0: // Name
                match = (item.name.find(query) != std::string::npos);
                break;
            case 1: // Director
                match = (item.director.find(query) != std::string::npos);
                break;
            case 2: { // Year
                std::string year_str = std::to_string(item.year);
                match = (year_str.find(query) != std::string::npos);
                break;
            }
            case 3: // Genre
                match = (item.genre.find(query) != std::string::npos);
                break;
            case 4: // Rating
                match = (item.rating.find(query) != std::string::npos);
                break;
        }

        if (match) {
            ss << item.name << ": " << item.director << ": "
               << item.year << ": " << item.genre << ": " << item.rating << "\n";
            found = true;
        }
    }

    if (found) {
        fl_message(ss.str().c_str());
    } else {
        fl_message("No matching movies found.");
    }
}






int main(int argc, char** argv) {
    ifstream file;
    file.open("movies.csv");
    if (!file.is_open()) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    string line;
    getline(file, line); // Skip header line

    while (getline(file, line)) {
        stringstream ss(line);
        string name, director, year, genre, rating;

        getline(ss, name, ',');
        getline(ss, director, ',');
        getline(ss, year, ',');
        getline(ss, genre, ',');
        getline(ss, rating, ',');

        Thng t;
        t.name = name;
        t.director = director;
        t.year = stoi(year);
        t.genre = genre;
        t.rating = rating;
        things.push_back(t);
    }
    file.close();


    Fl_Window* win = new Fl_Window(400, 300, "Movie Database");

    Fl_Choice* choice = new Fl_Choice(120, 80, 200, 30, "Search by:");
    choice->add("Name");
    choice->add("Director");
    choice->add("Year");
    choice->add("Genre");
    choice->add("Rating");

    // Input field
    Fl_Input* input = new Fl_Input(120, 40, 200, 30, "Keyword to Search:");

    // Button
    Fl_Button* button = new Fl_Button(150, 190, 100, 30, "Search");

    Fl_Button* add = new Fl_Button(150, 220, 100, 30, "Add Movie");

    // Pack widgets
    Widgets* widgets = new Widgets{input, button, add, choice};
    button->callback(button_cb, widgets);
    add->callback(add_cb, widgets);


    win->end();
    win->show(argc, argv); // Show window

    return Fl::run();
}