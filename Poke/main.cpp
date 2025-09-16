//g++ main.cpp battle.cpp -o app `fltk-config --cxxflags --ldflags`
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include "battle.h"

// Callback function
void button_cb(Fl_Widget* w, void* data) {
    Fl_Window* main_win = (Fl_Window*)data;
    my_function(main_win); // Pass main window to battle
}

int main(int argc, char** argv) {
    Fl_Window* win = new Fl_Window(400, 250, "FLTK Signup Example");
    Fl_Button* button = new Fl_Button(150, 170, 100, 30, "Submit");
    button->callback(button_cb, win); // Pass win as data
    win->end();
    win->show(argc, argv);
    return Fl::run();
}