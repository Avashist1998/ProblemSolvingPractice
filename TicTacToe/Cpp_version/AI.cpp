#include "AI.h"
#include "TicTacToe.h"
#include <iostream>
#include <vector>

using namespace std;
AI::AI() {

}
int AI::pickSpot(TicTacToe game) {
    vector<int> choices;
    for (int i = 0; i < 9; ++i) {
        if (game.board[i] == '-') {
            choices.push_back(i + 1);
        }

    }
    return choices[rand() % choices.size()];
}

