#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Box.H>
#include <string>
#include "battle.h"

int battle(Fl_Window* main_win, const Pokemon& selected) {
    Fl_Window* win = new Fl_Window(300, 250, "Battle");

    int y = 20;  // vertical position for each label
    int x = 50;  // left margin

    // Name
    Fl_Box* nameBox = new Fl_Box(x, y, 200, 20, ("Name: " + selected.name).c_str());
    nameBox->align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE);
    y += 25;

    // Type
    Fl_Box* typeBox = new Fl_Box(x, y, 200, 20, ("Type: " + selected.type).c_str());
    typeBox->align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE);
    y += 25;

    // Damage
    Fl_Box* dmgBox = new Fl_Box(x, y, 200, 20, ("Damage: " + std::to_string(selected.damage)).c_str());
    dmgBox->align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE);
    y += 25;

    // Dodge
    Fl_Box* ddgBox = new Fl_Box(x, y, 200, 20, ("Dodge: " + std::to_string(selected.dodge)).c_str());
    ddgBox->align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE);
    y += 25;

    // Health
    Fl_Box* hpBox = new Fl_Box(x, y, 200, 20, ("Health: " + std::to_string(selected.health)).c_str());
    hpBox->align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE);
    y += 25;

    // Energy
    Fl_Box* enBox = new Fl_Box(x, y, 200, 20, ("Energy: " + std::to_string(selected.energy)).c_str());
    enBox->align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE);
    y += 35;

    // Back button
    Fl_Button* back = new Fl_Button(100, y, 100, 30, "Back");
    back->callback([](Fl_Widget* w, void* data) {
        auto main_win = static_cast<Fl_Window*>(data);
        w->window()->hide();
        main_win->show();
    }, main_win);

    win->end();
    win->show();
    return Fl::run();
}
