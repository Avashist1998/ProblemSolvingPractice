#include<iostream>
#include<string>
#include "TicTacToe.h"

using namespace std;

TicTacToe::TicTacToe (char playerToken, char aiMarker) {
    this->userMarker = playerToken;
    this->aiMarker = aiMarker;
    this->winner = '-';
    this->currentMarker = userMarker;
    setBoard();
    
}
void TicTacToe::setBoard() {
    for(int i = 0; i<9; ++i) {
        board[i] = '-';
    }
}
bool TicTacToe::withinRange(int spot) {
    return ((spot > 0) && (spot <= 9)) ? true : false;
}
bool TicTacToe::isEmpty(int spot) {
    return (board[spot - 1] == '-') ? true : false;
}
bool TicTacToe::playTurn(int spot) {
    bool isValid = ((withinRange(spot)) && (isEmpty(spot)));
    if (isValid) {
        
        board[spot - 1] = currentMarker;
        this->currentMarker = (currentMarker == userMarker) ? aiMarker : userMarker;
    }
    return isValid;
}
void TicTacToe::BoardPrinter() {
    for (int i = 1; i < 10; ++i) {
        if (i%3 == 0) {
            cout << this->board[i-1] << endl;
            if (i< 9) cout << "==========" << endl;
        }
        else {
            cout << this->board[i-1] << "|";
        }
    }

}
void TicTacToe::printIndexBoard() {
    for (int i = 1; i < 10; ++i) {
        if (i%3 == 0) {
            cout << i << endl;
            if (i < 9) {
                cout << "==========" << endl;
            }
        }
        else {
            cout << i << " | ";
        }
    }
}
bool TicTacToe::midChecker() {
    bool check = false;
    if ((board[0] == board[4]) && (board[4] == board[8])) {
        check = true;
    }
    else if ((board[2] == board[4]) && (board[4] == board[6])) {
        check = true;
    }
    else if ((board[2] == board[4]) && (board[4] == board[7])) {
        check = true;
    }
    else if ((board[3] == board[4]) && (board[4] == board[5])) {
        check = true;
    }
    return check;
}
bool TicTacToe::topRightChecker() {
    bool check = false;
    if ((board[0] == board[1]) && (board[1] == board[2])) {
        check = true;
    }
    else if ((board[0] == board[3]) && (board[3] == board[6])) {
        check = true;
    }
    return check;
}
bool TicTacToe::bottomLeftChecker() {
    bool check = false;
    if ((board[2] == board[5]) && (board[5] == board[8])) {
        check = true;
    }
    else if ((board[6] == board[7]) && (board[7] == board[8])) {
        check = true;
    }
    return check;
}
bool TicTacToe::WinnerCheck() {
    bool mid = ((midChecker()) && (board[4] != '-'));
    bool topRight = ((topRightChecker()) && (board[0] != '-'));
    bool bottomLeft = ((bottomLeftChecker()) && (board[8] != '-'));
    if (mid) {
        this->winner = board[4];
    }
    else if (topRight) {
        this->winner = board[0];
    }
    else if (bottomLeft) {
        this->winner = board[8];
    }
    return ((mid) || (topRight) || (bottomLeft));
}
bool TicTacToe::boardChecker() {
    bool checker = true;
    for (int i = 0; i < 9; ++i) {
        if (board[i] == '-') {
            checker = false;
        }
    }
    return checker;
}
string TicTacToe::gameOver() {
    bool isThereAWinner = WinnerCheck();
    bool isTheBoardFull = boardChecker();
    if ((isTheBoardFull) && (!isThereAWinner)) {
        return "The Game is a Draw";
    }
    else if (isThereAWinner) {
        string YouareWinner = "We have a winner! The winner is ";
        string TheWinner(1, winner);
        YouareWinner = YouareWinner + TheWinner;
        return YouareWinner;
    }
    else {
        return "The game is not over";
    }
}