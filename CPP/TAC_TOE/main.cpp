// Vincent Johnson, Tic Tac Toe
// g++ main.cpp -o app `fltk-config --cxxflags --ldflags`
// /p/Johnson_Vincent/VJ_CP3/TAC_TOE

#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <random>
#include <vector>

#include <string>
#include <iostream>
#include <FL/fl_ask.H> // For fl_message

using namespace std;

vector<string> spaces(9, " "); // 9 empty spaces
bool gameOver = false; // Boolean to tell if game is over
vector<vector<int>> wins = {
    {0,1,2}, {3,4,5}, {6,7,8}, // horizontals
    {0,3,6}, {1,4,7}, {2,5,8}, // verticals
    {0,4,8}, {2,4,6}           // diagonals
};


string turn = "X"; // X starts
string turnout = "O"; // O is computer
vector<Fl_Button*> buttons;  // store button pointers

void reset_game();

void button_cb(Fl_Widget* w, void* data) {
    if (gameOver) return; // Do nothing if game is over
    int id = (intptr_t)data; // Get button index

    if (spaces[id] == " ") { // Only if empty
        spaces[id] = turn; // Set space to X
        buttons[id]->label(turn.c_str()); // Update button label

        // Check for win (fix index usage)
        for (const auto& win : wins) {
            int a = win[0], b = win[1], c = win[2]; // Take win conditions
            if (spaces[a] == turn && spaces[b] == turn && spaces[c] == turn) { // If conditions are met
                gameOver = true;
                fl_message("Player %s wins!", turn.c_str());
                return;
            }
        }

        // Check for draw
        bool draw = true;
        for (const auto& s : spaces) {
            if (s == " ") {
                draw = false;
                break;
            }
        }
        if (draw) {
            gameOver = true;
            fl_message("It's a draw!");
            return;
        }

        turn = "O"; // Switch turn to computer

        // Computer random move only if there are empty spaces left
        bool moveMade = false;
        for (const auto& s : spaces) {
            if (s == " ") {
                moveMade = true;
                break;
            }
        }
        if (!moveMade) return; // Board full, no computer move

        random_device rd; // Using the random device
        mt19937 gen(rd()); // Mersenne Twister RNG
        uniform_int_distribution<> dist(0, 8); // Number between 0 and 8

        int r = dist(gen); // Random number!
        while (spaces[r] != " ") { // Find empty space
            r = dist(gen);
        }

        spaces[r] = turnout;
        buttons[r]->label(turnout.c_str());

        // Check win again for computer
        for (const auto& win : wins) {
            int a = win[0], b = win[1], c = win[2];
            if (spaces[a] == turn && spaces[b] == turn && spaces[c] == turn) {
                gameOver = true;
                fl_message("Player %s wins!", turn.c_str());
                return;
            }
        }
        // Check for draw after computer move
        draw = true;
        for (const auto& s : spaces) {
            if (s == " ") {
                draw = false;
                break;
            }
        }
        if (draw) {
            gameOver = true;
            fl_message("It's a draw!");
            return;
        }
        turn = "X"; // Switch back to human
    }
}


Fl_Button* resetBtn = nullptr;

void reset_game() {
    for (int i = 0; i < 9; ++i) {
        spaces[i] = " ";
        buttons[i]->label(" ");
    }
    turn = "X";
    gameOver = false;
}

int main(int argc, char** argv) {
    Fl_Window* win = new Fl_Window(300, 380, "Tic Tac Toe");

    // Make a 3x3 grid
    int x = 50, y = 50, size = 60;
    for (int i = 0; i < 9; i++) {
        int row = i / 3;
        int col = i % 3;
        Fl_Button* b = new Fl_Button(x + col*70, y + row*70, size, size, " ");
        b->callback(button_cb, (void*)(intptr_t)i);
        buttons.push_back(b);
    }

    // Add reset button
    resetBtn = new Fl_Button(100, 280, 100, 40, "Reset");
    resetBtn->callback([](Fl_Widget*, void*) { reset_game(); });

    win->end();
    win->show(argc, argv);
    return Fl::run();
}
