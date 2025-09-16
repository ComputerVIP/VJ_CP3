#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Box.H>
#include "battle.h"

int my_function(Fl_Window* main_win) {
    // Example: Change the main window's label
    main_win->label("Main Window Edited!");

    // Open a new window as before
    Fl_Window* win = new Fl_Window(200, 100, "Battle Window");
    Fl_Box* box = new Fl_Box(20, 40, 160, 20, "Hi");
    win->end();
    win->show();
    return Fl::run();
}