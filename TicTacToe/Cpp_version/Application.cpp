#include <iostream>
#include "TicTacToe.h"
#include "AI.h"

using namespace std;

int main()
{
    bool doYouWantToPlay = true;
    while (doYouWantToPlay == true)
    {
        cout << "Welcome to Tic Tac Toe! You are about to play against an AI" << endl;
        cout << "First you must pick what character you want to play as?" << endl;
        cout << "Second you must also pick the character of the AI" << endl;
        cout << endl;
        cout << "Enter a single character that will represent you on the board" << endl;
        char userToken;
        cin >> userToken;
        cout << "Enter a single character that will represent the ai on the board" << endl;
        char aiToken;
        cin >> aiToken;
        TicTacToe game(userToken, aiToken);
        AI ai;
        cout << endl;
        cout << "Now we can start the game. To play, enter a number and your token shall be put " << "in  its place.\nThe numbers go from 1-9, left to right, Let's see who will win this round." << endl;
        game.printIndexBoard();
        while (game.gameOver() == "The game is not over")
        {
            if (game.currentMarker == game.userMarker)
            {
                cout << "It's your turn! Enter a spot for your token" << endl;
                int spot;
                cin >> spot;
                while (!game.playTurn(spot))
                {
                    cout << "Try again. " << spot << " is invalid. This spot is already taken or out of range" << endl;
                    cin >> spot;
                }
            }
            else
            {
                cout << "It's my turn!" << endl;
                int aiSpot = ai.pickSpot(game);
                game.playTurn(aiSpot);
                cout << "I picked " << aiSpot << "!" << endl;
            }
            cout << endl;
            game.BoardPrinter();
        }
        cout << endl;
        cout << game.gameOver() << endl;
        cout << endl;
        cout << "Do you want to play again? Enter Y for yes and N for no." << endl;
        char response;
        cin >> response;
        doYouWantToPlay = ((response == 'Y') || (response == 'y')) ? true : false;
        cout << endl;
        cout << endl;
    }
}