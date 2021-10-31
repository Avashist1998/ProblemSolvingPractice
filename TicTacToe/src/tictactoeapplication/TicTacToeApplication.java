package tictactoeapplication;
import java.util.Scanner;


public class TicTacToeApplication {

    public static void main(String[] args){
        Scanner myObj = new Scanner(System.in);
        boolean doYouWantToPlay = true;
        while (doYouWantToPlay){
            System.out.println("Welcome to Tic Tac Toe! You are about to play against an AI");
            System.out.println("First you must pick what character you want to play as?");
            System.out.println("Second you must alos pick the character of the AI");
            System.out.println();
            // settingup the user char
            System.out.println("Enter a single character that will represent you on the board");
            char userToken = myObj.next().charAt(0);
            // setting up the ai char
            System.out.println("Enter a single character that will represent the ai on the board");
            char aiToken = myObj.next().charAt(0);
            TicTacToe game = new TicTacToe(userToken, aiToken);
            AI ai = new AI();
            // set up the game 
            System.out.println();
            System.out.println("Now we can start the game. To play, enter a numver and your token shall be put " + "in  its place.\nThe numbers go from 1-9, left to right, We shall who will win this round.");
            game.printIndexBoard();
            //Let's start
            while(game.gameOver().equals("The game is not over")){
                if (game.currentMarker == game.userMarker){
                    System.out.println("It's your turn! Enter a spot for your token");
                    int spot = myObj.nextInt();
                    while(!game.playTurn(spot)){
                        System.out.print("Try again. " + spot + "is invalid. This spot is already taken or out of range");
                        spot = myObj.nextInt();
                    }
                }
                else{
                    System.out.println("It's my turn!");
                    int aiSpot = ai.pickSpot(game);
                    game.playTurn(aiSpot);
                    System.out.println("I picked " + aiSpot + "!");
                }
                System.out.println();
                game.BoardPrinter();
            }
            System.out.println();
            System.out.println(game.gameOver());
            System.out.println();
            System.out.println("Do you want to play again? Enter Y for yes and N for no.");
            char response = myObj.next().charAt(0);
            doYouWantToPlay = (response == 'Y' || response == 'y') ? true : false;
            System.out.println();
            System.out.println();
        }
        myObj.close();

    }

}