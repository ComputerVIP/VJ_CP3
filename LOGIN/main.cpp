// Vincent Johnson, User login
// g++ main.cpp -o app `fltk-config --cxxflags --ldflags`        

#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Output.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Choice.H>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

// Store admins and users
vector<string> admins = {"Vienna", "Vincent", "Clang"};
vector<string> users  = {"Alice", "Bob", "Charlie"};

// Struct to hold widgets for callbacks
struct Widgets {
    Fl_Input* input;
    Fl_Output* output;
    Fl_Choice* typeChoice; // optional for signup
};

// Function to add new users
void addUser(const string& newUser, const string& newType) {
    if (newType == "Admin") {
        admins.push_back(newUser);
    } else {
        users.push_back(newUser);
    }
}

// Button callback
void button_cb(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    string name = widgets->input->value();

    // Check if name is an admin
    for (auto& a : admins) {
        if (name == a) {
            string msg = "Welcome Admin " + a;
            widgets->output->value(msg.c_str());
            return;
        }
    }

    // Check if name is a user
    for (auto& u : users) {
        if (name == u) {
            string msg = "Welcome User " + u;
            widgets->output->value(msg.c_str());
            return;
        }
    }

    // If not found, "sign them up" with dropdown choice
    int idx = widgets->typeChoice->value(); // 0=Admin, 1=User
    string role = widgets->typeChoice->menu()[idx].label();

    addUser(name, role);

    string msg = "Signed up new " + role + ": " + name;
    widgets->output->value(msg.c_str());
}

int main(int argc, char** argv) {
    Fl_Window* win = new Fl_Window(400, 250, "FLTK Signup Example");

    // Input field
    Fl_Input* input = new Fl_Input(120, 40, 200, 30, "Enter name:");

    // Dropdown (choice)
    Fl_Choice* choice = new Fl_Choice(120, 80, 200, 30, "Role:");
    choice->add("Admin");
    choice->add("User");
    choice->value(1); // Default to "User"

    // Output field
    Fl_Output* output = new Fl_Output(120, 120, 200, 30, "Result:");

    // Button
    Fl_Button* button = new Fl_Button(150, 170, 100, 30, "Submit");

    // Pack widgets
    Widgets* widgets = new Widgets{input, output, choice};
    button->callback(button_cb, widgets);

    win->end();
    win->show(argc, argv);

    return Fl::run();
}
