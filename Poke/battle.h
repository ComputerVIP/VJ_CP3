#pragma once
#include <FL/Fl_Window.H>
#include <string>

struct Pokemon {
    std::string name;
    std::string type;
    int damage;
    int dodge;
    int health;
    int energy;
};

int choice(Fl_Window* main_win);
int battle(Fl_Window* main_win, const Pokemon& selected);
