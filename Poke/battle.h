#pragma once
#include <FL/Fl_Window.H>
#include <iostream>
#include <string>

// Pokemon definition
struct Pokemon {
    std::string name;
    std::string type;
    int damage;
    int dodge;
    int health;
    int energy;
};

// Runtime stats for battles
struct BattleStats {
    std:: string type;
    int damage;
    int dodge;
    int health;
    int energy;
};

// Enemy/player action options
enum Action {
    ATTACK,
    HEAL,
    REST
};

// Main battle function
int battle(Fl_Window* main_win, const Pokemon& player, const Pokemon& opponent);

// Choice function
int choice(Fl_Window* main_win);

// Enemy turn function
void enemyTurn(BattleStats& playerStats, BattleStats& opponentStats,
               Fl_Window* battle_win, Fl_Window* main_win);

