#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/fl_ask.H>  // For fl_message
#include <cstdlib>
#include <ctime>
#include <random>
#include <iostream>
#include <cmath>
#include "battle.h"

// Helper functions (can be static or in an anonymous namespace)
void lightAttackCallback(Fl_Widget* w, void* data) {
    auto tuple = static_cast<std::tuple<BattleStats*, BattleStats*, Fl_Window*>*>(data);
    auto& playerStats   = *std::get<0>(*tuple);
    auto& opponentStats = *std::get<1>(*tuple);
    auto main_win       = std::get<2>(*tuple);
    auto battle_win     = w->window();

    if (playerStats.energy < 2) {
        fl_message("Not enough energy for Light Attack!");
        enemyTurn(playerStats, opponentStats, battle_win, main_win);
        return;
    }

    int damage = static_cast<int>(std::ceil(0.65 * playerStats.damage));
    playerStats.energy -= 2;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0,100);

    if (dist(gen) < opponentStats.dodge) {
        fl_message("Opponent dodged your light attack!\n Energy: %d", playerStats.energy);
    } else {
        opponentStats.health -= damage;
        fl_message("Light Attack dealt %d!\nOpponent health: %d\nYour energy: %d", damage, opponentStats.health, playerStats.energy);
    }

    if (opponentStats.health <= 0) {
        opponentStats.health = 0;
        fl_message("You win!");
        battle_win->hide();
        main_win->show();
        return;
    }

    enemyTurn(playerStats, opponentStats, battle_win, main_win);
}
void attackCallback(Fl_Widget* w, void* data) {
    auto tuple = static_cast<std::tuple<BattleStats*, BattleStats*, Fl_Window*>*>(data);
    auto& playerStats   = *std::get<0>(*tuple);
    auto& opponentStats = *std::get<1>(*tuple);
    auto main_win       = std::get<2>(*tuple);
    auto battle_win     = w->window();

    int damage = playerStats.damage;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0,100);

    if (dist(gen) < opponentStats.dodge) {
        fl_message("Opponent dodged your regular attack!\n Energy: %d", playerStats.energy);
    } else {
        opponentStats.health -= damage;
        fl_message("Regular attack dealt %d!\nOpponent health: %d\nYour energy: %d", damage, opponentStats.health, playerStats.energy);
    }

    if (opponentStats.health <= 0) {
        opponentStats.health = 0;
        fl_message("You win!");
        battle_win->hide();
        main_win->show();
        return;
    }

    enemyTurn(playerStats, opponentStats, battle_win, main_win);
}

// Heavy Attack
void heavyAttackCallback(Fl_Widget* w, void* data) {
    auto tuple = static_cast<std::tuple<BattleStats*, BattleStats*, Fl_Window*>*>(data);
    auto& playerStats   = *std::get<0>(*tuple);
    auto& opponentStats = *std::get<1>(*tuple);
    auto main_win       = std::get<2>(*tuple);
    auto battle_win     = w->window();

    if (playerStats.energy < 7) {
        fl_message("Not enough energy for Heavy Attack!");
        enemyTurn(playerStats, opponentStats, battle_win, main_win);
        return;
    }

    int damage = static_cast<int>(1.25 * playerStats.damage);
    playerStats.energy -= 7;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0,100);

    if (dist(gen) < opponentStats.dodge) {
        fl_message("Opponent dodged your heavy attack!\n Energy: %d", playerStats.energy);
    } else {
        opponentStats.health -= damage;
        fl_message("Light Attack dealt %d!\nOpponent health: %d\nYour energy: %d", damage, opponentStats.health, playerStats.energy);
    }
    if (opponentStats.health <= 0) {
        opponentStats.health = 0;
        fl_message("You win!");
        battle_win->hide();
        main_win->show();
        return;
    }

    enemyTurn(playerStats, opponentStats, battle_win, main_win);
}

// Heal
void healCallback(Fl_Widget* w, void* data) {
    auto tuple = static_cast<std::tuple<BattleStats*, BattleStats*, Fl_Window*>*>(data);
    auto& playerStats   = *std::get<0>(*tuple);
    auto& opponentStats = *std::get<1>(*tuple);
    auto main_win       = std::get<2>(*tuple);
    auto battle_win     = w->window();

    int healAmount = 5;
    playerStats.health += healAmount;
    fl_message("You healed for %d!\nYour health: %d", healAmount, playerStats.health);

    enemyTurn(playerStats, opponentStats, battle_win, main_win);
}

// Rest
void restCallback(Fl_Widget* w, void* data) {
    auto tuple = static_cast<std::tuple<BattleStats*, BattleStats*, Fl_Window*>*>(data);
    auto& playerStats   = *std::get<0>(*tuple);
    auto& opponentStats = *std::get<1>(*tuple);
    auto main_win       = std::get<2>(*tuple);
    auto battle_win     = w->window();

    int energyGain = 5;
    playerStats.energy += energyGain;
    fl_message("You rested and regained %d energy!\nYour energy: %d", energyGain, playerStats.energy);

    enemyTurn(playerStats, opponentStats, battle_win, main_win);
}

// Enemy AI logic
void enemyTurn(BattleStats& playerStats, BattleStats& opponentStats,Fl_Window* battle_win, Fl_Window* main_win){

    // Random device for action choice
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> actionDist(0, 2);
    std::uniform_int_distribution<> dodgeDist(0, 100);
    std::uniform_int_distribution<> typeAttack(0, 2);

    Action enemyAction = static_cast<Action>(actionDist(gen));

    switch (enemyAction) {
        case ATTACK: {
            int dmg = opponentStats.damage;
            if (typeAttack(gen) == 0) {
                if (opponentStats.energy < 2) {
                    fl_message("Enemy does not have enough energy for Light Attack!");
                    break;
                }
                if (dodgeDist(gen) < playerStats.dodge) {
                    fl_message("You dodged the enemy's attack!");
                    break;
                }
                playerStats.health -= floor(0.65*dmg);
                opponentStats.energy -= 2;
                fl_message("Enemy attacked you for %d!\nYour health: %d",
                        dmg, playerStats.health);
                if (playerStats.health <= 0){
                    playerStats.health = 0;
                    fl_message("You lose!");
                    battle_win->hide();
                    main_win->show();
                    return;
                }

                break;

            } else if (typeAttack(gen) == 1) {
                if (opponentStats.energy < 5) {
                    fl_message("Enemy does not have enough energy for Regular Attack!");
                    break;
                }
                if (dodgeDist(gen) < playerStats.dodge) {
                    fl_message("You dodged the enemy's attack!");
                    break;
                }
                playerStats.health -= dmg;
                opponentStats.energy -= 5;
                fl_message("Enemy attacked you for %d!\nYour health: %d",
                        dmg, playerStats.health);
                if (playerStats.health <= 0){
                    playerStats.health = 0;
                    fl_message("You lose!");
                    battle_win->hide();
                    main_win->show();
                    return;
                }

                break;
            } else {
                if (opponentStats.energy < 7) {
                    fl_message("Enemy does not have enough energy for Regular Attack!");
                    break;
                }
                if (dodgeDist(gen) < playerStats.dodge) {
                    fl_message("You dodged the enemy's attack!");
                    break;
                }
                playerStats.health -= floor(1.25*dmg);
                opponentStats.energy -= 7;
                fl_message("Enemy attacked you for %d!\nYour health: %d",
                        dmg, playerStats.health);
                if (playerStats.health <= 0){
                    playerStats.health = 0;
                    fl_message("You lose!");
                    battle_win->hide();
                    main_win->show();
                    return;
                }

                break;
            }
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

    BattleStats playerStats {player.damage, player.dodge, player.health, player.energy};
    BattleStats opponentStats {opponent.damage, opponent.dodge, opponent.health, opponent.energy};

    // Bundle into tuple for callbacks
    auto tuple = new std::tuple<BattleStats*, BattleStats*, Fl_Window*>(&playerStats, &opponentStats, main_win);

    Fl_Button* attackLight = new Fl_Button(50, 50, 100, 30, "Light");
    attackLight->callback(lightAttackCallback, tuple);

    Fl_Button* attackRegular = new Fl_Button(50, 90, 100, 30, "Regular");
    attackRegular->callback(attackCallback, tuple);

    Fl_Button* attackHeavy = new Fl_Button(50, 130, 100, 30, "Heavy");
    attackHeavy->callback(heavyAttackCallback, tuple);

    Fl_Button* heal = new Fl_Button(50, 170, 100, 30, "Heal");
    heal->callback(healCallback, tuple);

    Fl_Button* rest = new Fl_Button(50, 210, 100, 30, "Rest");
    rest->callback(restCallback, tuple);


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