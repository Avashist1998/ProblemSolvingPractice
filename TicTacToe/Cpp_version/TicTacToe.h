#ifndef TICTACTOE_H
#define TICTACTOE_H
#include <string>
using namespace std;

class TicTacToe {
    protected:
        char winner;
    public:
        protected: char board[9];
        protected: char currentMarker;
        protected: char userMarker;
        protected: char aiMarker;
        TicTacToe (char playerToken, char aiMarker);
        void setBoard();
        bool withinRange(int spot);
        bool isEmpty(int spot);
        bool playTurn(int spot);
        void BoardPrinter();
        void printIndexBoard();
        bool midChecker();
        bool topRightChecker();
        bool bottomLeftChecker();
        bool WinnerCheck();
        bool boardChecker();
        string gameOver();
};
#endif

