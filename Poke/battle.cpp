#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/fl_ask.H>  // For fl_message
#include <cstdlib>
#include <ctime>
#include <random>
#include <iostream>
#include "battle.h"

// Enemy AI logic
// Enemy AI logic
void enemyTurn(BattleStats& playerStats, BattleStats& opponentStats,Fl_Window* battle_win, Fl_Window* main_win) {
    // Random device for action choice
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> actionDist(0, 2);
    std::uniform_int_distribution<> dodgeDist(0, 100);

    Action enemyAction = static_cast<Action>(actionDist(gen));

    switch (enemyAction) {
        case ATTACK: {
            int dmg = opponentStats.damage;

            // Check if player dodges
            if (dodgeDist(gen) < playerStats.dodge) {
                fl_message("You dodged the enemy's attack!");
            } else {
                playerStats.health -= dmg;
                fl_message("Enemy attacked you for %d!\nYour health: %d",
                           dmg, playerStats.health);
                if (playerStats.health <= 0){
                    playerStats.health = 0;
                    fl_message("You lose!");
                    battle_win->hide();
                    main_win->show();
                    return;
                }

            }
            break;
        }

        case HEAL: {
            int healAmount = 5;
            opponentStats.health += healAmount;
            fl_message("Enemy healed for %d!\nOpponent health: %d",
                       healAmount, opponentStats.health);
            break;
        }
        case REST: {
            int restAmount = 5;
            opponentStats.energy += restAmount;
            fl_message("Enemy rested for %d!\nOpponent energy: %d",
                       restAmount, opponentStats.energy);
            break;
        }
    }
}


int battle(Fl_Window* main_win, const Pokemon& player, const Pokemon& opponent) {
    Fl_Window* win = new Fl_Window(400, 300, "Battle");

    // Initialize player and opponent stats
    BattleStats playerStats {player.damage, player.dodge, player.health, player.energy};
    BattleStats opponentStats {opponent.damage, opponent.dodge, opponent.health, opponent.energy};

    std::srand(std::time(nullptr));

    // Attack button
    Fl_Button* attack = new Fl_Button(50, 50, 100, 30, "Attack");
    attack->callback([](Fl_Widget* w, void* data) {
        auto both = static_cast<std::pair<BattleStats*, BattleStats*>*>(data);
        auto& playerStats   = *both->first;
        auto& opponentStats = *both->second;

        // Player attacks
        int damage = playerStats.damage;

        std:: random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dist(0,100);

        if (dist(gen) < opponentStats.dodge) {
            fl_message("Opponent dodged your attack!");
            // Then enemy takes a turn
            enemyTurn(playerStats, opponentStats, w->window(), main_win);
            return;
        } else {

        opponentStats.health -= damage;
        fl_message("You attacked for %d!\nOpponent health: %d",
                   damage, opponentStats.health);

        if (opponentStats.health < 0) {
            opponentStats.health = 0;
            fl_message("You win!");
            w->window()->hide();
            main_win->show();
            return;
        }

        // Then enemy takes a turn
        enemyTurn(playerStats, opponentStats, w->window(), main_win);

        }
    }, new std::pair<BattleStats*, BattleStats*>(&playerStats, &opponentStats));

    // Heal button
    Fl_Button* heal = new Fl_Button(50, 100, 100, 30, "Heal");
    heal->callback([](Fl_Widget* w, void* data) {
        auto both = static_cast<std::pair<BattleStats*, BattleStats*>*>(data);
        auto& playerStats   = *both->first;
        auto& opponentStats = *both->second;

        // Player heals
        int healAmount = 5;
        playerStats.health += healAmount;
        fl_message("You healed for %d!\nYour health: %d",
                   healAmount, playerStats.health);

        // Then enemy takes a turn
        enemyTurn(playerStats, opponentStats, w->window(), main_win);
    }, new std::pair<BattleStats*, BattleStats*>(&playerStats, &opponentStats));

    // Rest button
    Fl_Button* rest = new Fl_Button(50, 150, 100, 30, "Rest");
    rest->callback([](Fl_Widget* w, void* data) {
        auto both = static_cast<std::pair<BattleStats*, BattleStats*>*>(data);
        auto& playerStats   = *both->first;
        auto& opponentStats = *both->second;

        // Player rests to regain energy
        int energyGain = 5;
        playerStats.energy += energyGain;
        fl_message("You rested and regained %d energy!\nYour energy: %d",
                   energyGain, playerStats.energy);

        // Then enemy takes a turn
        enemyTurn(playerStats, opponentStats, w->window(), main_win);
    }, new std::pair<BattleStats*, BattleStats*>(&playerStats, &opponentStats));

    // Back button
    Fl_Button* back = new Fl_Button(200, 50, 100, 30, "Back");
    back->callback([](Fl_Widget* w, void* data) {
        auto main_win = static_cast<Fl_Window*>(data);
        w->window()->hide();
        main_win->show();
    }, main_win);

    win->end();
    win->show();
    return Fl::run();
}
