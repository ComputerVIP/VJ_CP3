// Vincent Johnson, High score
// g++ main.cpp -o app `fltk-config --cxxflags --ldflags` -mconsole

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Output.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Choice.H>
#include <FL/fl_ask.H>
#include <string>
#include <limits>
#include <ctime>

using namespace std;

struct Widgets {
    Fl_Input* input;
    Fl_Input* input2;
};

struct Thng {
    string name;
    int score;
    string thyme;
};
vector<Thng> things;


void shwowScores(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    stringstream ss;
    ss << "Scores:\n";
    for (const auto& t : things) {
        ss << t.name << ": " << t.score << " --- "<< t.thyme<< "\n";
    }
    fl_message(ss.str().c_str());
}

// Button callback
void button_cb(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    string name = widgets->input->value();
    string score = widgets->input2->value();
    for (const auto& t : things) {
        if (name == t.name) {
            fl_message("Name already exists!");
            return;
        }
    }
    if (name.empty() || score.empty()) {
        fl_message("Please enter both name and score.");
        return;
    }

    time_t now = time(0);             // current time as seconds since epoch
    tm *ltm = localtime(&now);        // convert to local time struct

    string tme = to_string(1900 + ltm->tm_year) + "-" +
                  to_string(1 + ltm->tm_mon) + "-" +
                  to_string(ltm->tm_mday) + " " +
                  to_string(ltm->tm_hour) + ":" +
                  to_string(ltm->tm_min) + ":" +
                  to_string(ltm->tm_sec);
    int scoreInt = stoi(score);
    things.push_back({name, scoreInt, tme});

    ofstream file;

    file.open("scores.csv");
    if (file.is_open()) {
        file << "Name,Score,Time\n";
        for (const auto& t : things) {
            file << t.name << "," << t.score << "," << t.thyme << "\n";
        }
        fl_message("Added %s with score %d", name.c_str(), scoreInt);
    }
    file.close();

}



int main(int argc, char** argv) {
    ifstream file;
    file.open("scores.csv");
    if (!file.is_open()) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    string line;
    getline(file, line); // Skip header line

    while (getline(file, line)) {
        stringstream ss(line);
        string name, scoreStr, thy;

        getline(ss, name, ',');
        getline(ss, scoreStr, ',');
        getline(ss, thy, ',');

        Thng t;
        t.name = name;
        t.score = stoi(scoreStr);
        t.thyme = thy;
        things.push_back(t);
    }
    file.close();


    Fl_Window* win = new Fl_Window(400, 300, "High Score Table");

    // Input field
    Fl_Input* input = new Fl_Input(120, 40, 200, 30, "Enter name:");
    Fl_Input* input2 = new Fl_Input(120, 80, 200, 30, "Enter score:");

    // Button
    Fl_Button* button = new Fl_Button(150, 190, 100, 30, "Submit");

    Fl_Button* show = new Fl_Button(150, 220, 100, 30, "Show scores");

    // Pack widgets
    Widgets* widgets = new Widgets{input, input2};
    button->callback(button_cb, widgets);
    show->callback(shwowScores, widgets);


    win->end();
    win->show(argc, argv); // Show window

    return Fl::run();
}