// Vincent Johnson, Tic Tac Toe
// g++ main.cpp -o app `fltk-config --cxxflags --ldflags`

#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <random>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<string> spaces(9, " ");
vector<string> wins = {
    "0,1,2", "3,4,5", "6,7,8", // horizontals
    "0,3,6", "1,4,7", "2,5,8", // verticals
    "0,4,8", "2,4,6"           // diagonals
};

vector<string> turn = {"X"}; // X starts
vector<Fl_Button*> buttons;  // store button pointers

void button_cb(Fl_Widget* w, void* data) {
    int id = (intptr_t)data; // Get button index

    if (spaces[id] == " ") { // Only if empty
        spaces[id] = turn[0]; // Set space to X
        buttons[id]->label(turn[0].c_str()); // Update button label

        // Check for win
        for (const auto& win : wins) {
            int a = win[0] - '0';
            int b = win[2] - '0';
            int c = win[4] - '0';
            if (spaces[a] == turn[0] && spaces[b] == turn[0] && spaces[c] == turn[0]) {
                cout << "Player " << turn[0] << " wins!" << endl;
                return;
            }
        }

        // Switch turn
        turn[0] = (turn[0] == "X") ? "O" : "X";

        // Computer random move
        random_device rd; // Using the random device
        mt19937 gen(rd()); // Mersenne Twister RNG
        uniform_int_distribution<> dist(0, 8); // Number between 0 and 8

        int r = dist(gen); // Random number!
        while (spaces[r] != " ") { // Find empty space
            r = dist(gen);
        }

        spaces[r] = turn[0];
        buttons[r]->label(turn[0].c_str());

        // Check win again
        for (const auto& win : wins) {
            int a = win[0] - '0';
            int b = win[2] - '0';
            int c = win[4] - '0';
            if (spaces[a] == turn[0] && spaces[b] == turn[0] && spaces[c] == turn[0]) {
                cout << "Player " << turn[0] << " wins!" << endl;
                return;
            }
        }

        // Switch back to human
        turn[0] = (turn[0] == "X") ? "O" : "X";
    }
}

int main(int argc, char** argv) {
    Fl_Window* win = new Fl_Window(300, 300, "Tic Tac Toe");

    // Make a 3x3 grid
    int x = 50, y = 50, size = 60;
    for (int i = 0; i < 9; i++) {
        int row = i / 3;
        int col = i % 3;
        Fl_Button* b = new Fl_Button(x + col*70, y + row*70, size, size, " ");
        b->callback(button_cb, (void*)(intptr_t)i);
        buttons.push_back(b);
    }

    win->end();
    win->show(argc, argv);
    return Fl::run();
}
