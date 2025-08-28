// g++ main.cpp -o app `fltk-config --cxxflags --ldflags`
#include <FL/Fl.H>          // Core FLTK header (event loop, etc.)
#include <FL/Fl_Window.H>   // For creating a window
#include <FL/Fl_Input.H>    // For editable text input box
#include <FL/Fl_Button.H>   // For clickable buttons
#include <FL/Fl_Output.H>   // For read-only text display box

// Define a small struct (custom type) to hold both input and output widgets
// This makes it easy to pass them together into the button callback
struct Widgets {
    Fl_Input* input;   // Pointer to the input box (user types here)
    Fl_Output* output; // Pointer to the output box (shows result)
};

// Callback function for the button
// Runs when the button is clicked
void button_cb(Fl_Widget* w, void* data) {
    // Cast the generic "data" pointer back to our Widgets struct
    Widgets* widgets = (Widgets*)data;

    // Copy the text from the input box into the output box
    // input->value() gives us the current string
    // output->value(...) sets that string in the output box
    widgets->output->value(widgets->input->value());
}

int main(int argc, char** argv) {
    // Create the main window (400x200 pixels, with a title)
    Fl_Window* win = new Fl_Window(400, 200, "FLTK Input Example");

    // Create a text input box:
    // x=100, y=40, width=200, height=30, with label "Enter text:"
    Fl_Input* input = new Fl_Input(100, 40, 200, 30, "Enter text:");

    // Create a text output box (read-only):
    // x=100, y=90, width=200, height=30, with label "You typed:"
    Fl_Output* output = new Fl_Output(100, 90, 200, 30, "You typed:");

    // Create a button at x=150, y=140, width=100, height=30, with label "Submit"
    Fl_Button* button = new Fl_Button(150, 140, 100, 30, "Submit");

    // Package the input + output together into one struct
    Widgets* widgets = new Widgets{input, output};

    // Connect the button's click event to our callback function
    // When the button is clicked, button_cb() will be called,
    // and it will receive a pointer to our Widgets struct as "data"
    button->callback(button_cb, widgets);

    // Finish building the window (tell FLTK no more widgets will be added)
    win->end();

    // Show the window on the screen
    win->show(argc, argv);

    // Start the FLTK event loop (this keeps the window responsive)
    return Fl::run();
}
