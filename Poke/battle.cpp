#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Box.H>
#include <sstream>
#include "battle.h"

int battle(Fl_Window* main_win, const Pokemon& selected) {
    Fl_Window* win = new Fl_Window(300, 200, "Battle");

    std::stringstream info;
    info << selected.name << "\nType: " << selected.type
         << "\nDamage: " << selected.damage
         << "\nDodge: " << selected.dodge
         << "\nHealth: " << selected.health;

    new Fl_Box(50, 30, 200, 100, info.str().c_str());

    Fl_Button* back = new Fl_Button(100, 150, 100, 30, "Back");
    back->callback([](Fl_Widget* w, void* data) {
        auto main_win = static_cast<Fl_Window*>(data);
        w->window()->hide();
        main_win->show();
    }, main_win);

    win->end();
    win->show();
    return Fl::run();
}
