//g++ main.cpp battle.cpp choose.cpp -o app `fltk-config --cxxflags --ldflags` -mconsole
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include "battle.h"

int main() {
    Fl_Window* main_win = new Fl_Window(300, 200, "Main Menu");
    Fl_Button* play = new Fl_Button(100, 80, 100, 30, "Play");
    play->callback([](Fl_Widget* w, void* data) {
        choice(static_cast<Fl_Window*>(data));
    }, main_win);

    main_win->end();
    main_win->show();
    return Fl::run();
}
