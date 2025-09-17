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
// Struct to hold widgets for callbacks
struct Logins {
    string name;
    string password;
};
vector<Logins> admins = {{"Vienna","No"},{"Vincent","12345"},{"MinGW","superior"}};
vector<Logins> users  = {{"Alice","Password"},{"Bob","Prop"},{"Charlie","Char"},{"David","9025"},{"Eve","Peanut"},{"Clang","64"},{"G++","11"}};

struct Widgets {
    Fl_Input* input;
    Fl_Input* input2;
    Fl_Output* output;
    Fl_Choice* typeChoice; // optional for signup
};

// Function to add new users
void addUser(const string& newUser, const string& newType, const string& newPassword) {
    if (newType == "Admin") {
        admins.push_back({newUser, newPassword});
    } else {
        users.push_back({newUser, newPassword});
    }
}

// Button callback
void button_cb(Fl_Widget* w, void* data) {
    Widgets* widgets = (Widgets*)data;
    string name = widgets->input->value();
    string password = widgets->input2->value(); // <-- Add this line here

    // If dropdown is already visible → finalize signup
    if (widgets->typeChoice->visible()) { // If the box is visible
        string role = widgets->typeChoice->text(); // Get selected role
        string password = widgets->input2->value(); // Get password
        addUser(name, role, password); // Add new user

        string msg = "Signed up new " + role + ": " + name; // Confirmation message
        widgets->output->value(msg.c_str()); // Show message

        widgets->typeChoice->hide(); // hide again after signup
        return;
    }

    // Check admins
    for (auto& a : admins) {
        if (name == a.name && password == a.password) {
            string msg = "Welcome Admin " + a.name;
            widgets->output->value(msg.c_str());
            return;
        } else if (name == a.name) {
            widgets->output->value("Wrong password!");
            return;
        }
    }

    // Check users
    for (auto& u : users) {
        if (name == u.name && password == u.password) {
            string msg = "Welcome User " + u.name;
            widgets->output->value(msg.c_str());
            return;
        } else if (name == u.name) {
            widgets->output->value("Wrong password!");
            return;
        }
    }

    // Not found → show dropdown, ask for role
    widgets->typeChoice->show();
    widgets->output->value("New user, select a role, enter password then press Submit again.");
}



int main(int argc, char** argv) {
    Fl_Window* win = new Fl_Window(400, 250, "FLTK Signup Example");

    // Input field
    Fl_Input* input = new Fl_Input(120, 40, 200, 30, "Enter name:");
    Fl_Input* input2 = new Fl_Input(120, 80, 200, 20, "Enter password:");

    // Dropdown (choice)
    Fl_Choice* choice = new Fl_Choice(120, 100, 200, 30, "Role:");
    choice->add("Admin");
    choice->add("User");
    choice->value(1); // Default to "User"
    choice->hide(); // Hide initially

    // Output field
    Fl_Output* output = new Fl_Output(120, 140, 200, 30, "Result:");

    // Button
    Fl_Button* button = new Fl_Button(150, 190, 100, 30, "Submit");

    // Pack widgets
    Widgets* widgets = new Widgets{input, input2, output, choice};
    button->callback(button_cb, widgets);

    win->end();
    win->show(argc, argv); // Show window

    return Fl::run();
}
