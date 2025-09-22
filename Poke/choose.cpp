#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Box.H>
#include <fstream>
#include <sstream>
#include <vector>
#include "battle.h"

std::vector<Pokemon> load_pokemon() {
    std::vector<Pokemon> list;
    std::ifstream file("pokee.csv");
    std::string line;
    std::getline(file, line); // skip header
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        Pokemon p;
        std::string dmg, ddg, hp, en;
        std::getline(ss, p.name, ',');
        std::getline(ss, p.type, ',');
        std::getline(ss, dmg, ',');
        std::getline(ss, ddg, ',');
        std::getline(ss, hp, ',');
        std::getline(ss, en, ',');
        
        auto trim = [](std::string s) {
            s.erase(0, s.find_first_not_of(" \t\r\n"));
            s.erase(s.find_last_not_of(" \t\r\n") + 1);
            return s;
        };

        p.damage = std::stoi(trim(dmg));
        p.dodge  = std::stoi(trim(ddg));
        p.health = std::stoi(trim(hp));
        p.energy = std::stoi(trim(en));

        list.push_back(p);
    }
    return list;
}

int choice(Fl_Window* main_win) {
    main_win->hide();

    Fl_Window* win = new Fl_Window(300, 200, "Choose Pokemon");
    std::vector<Pokemon> pokes = load_pokemon();

    int y = 20;
    for (auto& p : pokes) {
        Fl_Button* b = new Fl_Button(50, y, 200, 30, p.name.c_str());
        b->callback([](Fl_Widget* w, void* data) {
            auto pack = static_cast<std::pair<Fl_Window*,Pokemon>*>(data);
            w->window()->hide();
            battle(pack->first, pack->second);
            delete pack;
        }, new std::pair<Fl_Window*,Pokemon>(main_win, p));
        y += 40;
    }

    win->end();
    win->show();
    return Fl::run();
}

