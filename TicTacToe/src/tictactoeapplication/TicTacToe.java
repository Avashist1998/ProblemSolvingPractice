package tictactoeapplication;
// creating a tictactoe class
public class TicTacToe{
    
    protected char [] board;

    protected char userMarker;
    protected char aiMarker;
    protected char winner, currentMarker;
    public TicTacToe(char playerToken, char aiMarker){
        this.userMarker = playerToken;
        this.aiMarker = aiMarker;
        this.winner = '-';
        this.board = setBoard();
        this.currentMarker = userMarker;
    }
    public char[] setBoard(){
    // we are setting up the board because there are 9 space in the board
        char [] board = new char[9];
        for (int i = 0; i<9; i++){
            board[i] = '-';
        } 
        return board;
    }
    public boolean withinRange(int spot){
        if (spot <= 9 && spot > 0)
            return true;
        else 
            return false;
    }
    public boolean isEmpty(int spot){
        // checking if the spot is free
        return board[spot-1] == '-';
    }
    public boolean playTurn(int spot){
        boolean isValid = withinRange(spot) && isEmpty(spot);
        if (isValid){
            board[spot-1] = currentMarker;
            // updating the maker to reflect that the turn has been placed
            currentMarker = (currentMarker == userMarker) ? aiMarker : userMarker;
        }
        return isValid;
    }
    public void BoardPrinter(){
        // the function can be called any time to print the baord
        //  0 | 1 | 2
        // ===========
        //  3 | 4 | 5
        // ===========
        //  6 | 7 | 8
        // ===========
        int i = 1;
        for (char spot : board){
            if ( i%3 == 0){
                System.out.println(spot);
                if (i < 9)
                    System.out.println("===========");
            }     
            else{
                System.out.print(spot);
                System.out.print(" | ");
            }
            i++;
        }
    }
    public void printIndexBoard(){
        // help the user understand the board
        
        for (int i = 1; i < 10; i++){
            if ( i%3 == 0){
                System.out.println(i);
                if (i < 9)
                    System.out.println("===========");
            }     
            else{
                System.out.print(i);
                System.out.print(" | ");
            }
        }
    }
    public boolean midChecker(){
        boolean check = false;
        if (board[0]  == board[4] && board[4] == board[8]) {
            check = true;
        }
        else if (board[2]  == board[4] && board[4] == board[6]){
            check = true;
        }
        else if (board[2]  == board[4] && board[4] == board[7]){
            check = true;
        }
        else if (board[3]  == board[4] && board[4] == board[5]){
            check = true;
        }
        return check;
    }
    public boolean topRightChecker(){
        boolean check = false;
        if (board [0] == board[1] && board [1] == board[2]) {
            check = true;
        }
        else if (board [0] == board[3] && board [3] == board[6]) {
            check = true;
        }

        return check;
    }
    public boolean bottomLeftChecker(){
        boolean check = false;
        if (board [2] == board[5] && board [5] == board[8]) {
            check = true;
        }
        else if (board [6] == board[7] && board [7] == board[8]) {
            check = true;
        }
        return check;
    }
    
    public boolean WinnerChecker(){
        boolean mid = (midChecker() && board [4] != '-');
        boolean topRight = (topRightChecker() && board [0] != '-');
        boolean bottomLeft = (bottomLeftChecker() && board [8] != '-');
        if (mid)
            this.winner = board[4];
        else if (topRight)
            this.winner = board[0];
        else if (bottomLeft)
            this.winner = board[8];
        return mid || topRight || bottomLeft;
    }
    public boolean boardChecker(){
        boolean checker = true;
        for (char spot : board){
            if (spot == '-')
                checker = false;
        }
        return checker;
    }
    public String gameOver(){
        boolean isThereAWinner = WinnerChecker();
        boolean isTheBoardFull = boardChecker();
        if (isTheBoardFull && !isThereAWinner)
            return "The Game is a Draw";
        else if (isThereAWinner)
            return "We have a winner! The winner is "+ this.winner + "'s";
        else
            return "The game is not over";
    }
}