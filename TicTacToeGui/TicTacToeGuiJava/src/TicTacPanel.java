//F5 to compile, F2 to run
//imports useful packages and toolkits
import java.util.*;
import javax.swing.*;
import java.awt.*; 
import java.awt.event.*; //very important
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;

//this green stuff is a comment 
public class TicTacPanel extends JPanel{
  
  //-----------------------------------
  //First,we create variables
  //-----------------------------------
  boolean player1; 
  int winner = -1;
  boolean AI = false;
  
  //in our 2d array named board
  //lets use "1" to represent x 
  //lets use "2" to represent o 
  
  //for example
 /*board when empty  |   board when its a tie  | board when X wins | board when O wins
  * [ ][ ][ ]        |     [1][2][1]           |   [1][2][2]       |    [2][1][1]  
  * [ ][ ][ ]        |     [1][2][2]           |   [ ][1][ ]       |    [ ][2][ ] 
  * [ ][ ][ ]        |     [2][1][2]           |   [ ][ ][1]       |    [ ][ ][2] 
  * */
   
  //2d representation of the game
  int[][]board = new int[3][3];
  int x;
  int y;
  
  //Win counter
  int player1wins=0 , player2wins =0;
  
  //Text
  JLabel turn = new JLabel("Player 1's Turn");
  /*JLabel p1wins = new JLabel("Player 1 Wins:" + player1wins); 
  JLabel p2wins = new JLabel("Player 2 Wins:" + player2wins);
  JLabel title = new JLabel("Tic-Tac-Toe");
  JLabel xy = new JLabel("x: y:"); */
  
  //Buttons
  JButton playAgainButton = new JButton("Play Again?"); 
  
  //Colors
  //Color colorname = new Color(red,green,blue);
  Color lightgreen = new Color(150,223,193);
  Color darkpurple = new Color(112,024,114);
  
  //----------------------------------------------------------
  //Constructor- initialize or give inital values to variables
  //----------------------------------------------------------
  public TicTacPanel(){
    setBackground(lightgreen);
    setPreferredSize(Toolkit.getDefaultToolkit().getScreenSize());
    //setPreferredSize(new Dimension(300,300));
    
    player1 = true;
    player1wins = 0;
    player2wins = 0;
    add(turn);
    
    if (this.AI == false){

    }

    //add label,texts, and buttons to our panel
    

    //add listeners - react to clicks and drags etc.
    addMouseListener(new XOListener()); 
    add(playAgainButton);
    
    //this button starts the game over
    playAgainButton.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
            reset();
            repaint();
         }          
      });
  }
  
  //paintComponent - this does the drawing and graphics
  public void paintComponent(Graphics page){
    
    super.paintComponent(page); //must have this line for the panel to update/call itself
    
    //add and scale an image file
    Image gametitle = Toolkit.getDefaultToolkit().getImage("title.png");
    page.drawImage(gametitle,330,0,600,300,this);
    
    //useful variables to scale and reposition the game
    int i=5;
    int j=5;
    int width=5;
    int height=300;
    int xpos=490;
    int ypos=218;
    
    if (this.AI == false){
      if(player1 == true){
        turn.setText("Player 1's turn");
      }else{
        turn.setText("Player 2's turn");
      }
    }
    else{
      if(player1 == true){
        turn.setText("Player 1's turn");
      }else{
        turn.setText("AI's turn");
      }
    }
    
    
    //create game board - 2-by-2 parallel lines - using drawRectangle
    page.setColor(darkpurple);
    //vertical lines
    page.fillRoundRect(xpos + 100,220,width,height,5,5);
    page.fillRoundRect(xpos + 200,220,width,height,5,5);
    //horizontal lines
    page.fillRoundRect(xpos,ypos + 100,height,width,5,5);
    page.fillRoundRect(xpos,ypos + 200, height,width,5,5);
    
    //convert data from array into actual visual game
    for(int x=0;x<board.length;x++){
      for(int y=0;y<board.length;y++){
        if(board[x][y]==1){   // "1" represents x 
          //draw X - using drawPolygon()
          page.setColor(Color.black);
          int [] m = {xpos + 20 + 100 * x,xpos + 30 + 100 * x,xpos + 50 + 100 * x,xpos + 70 + 100 * x,xpos + 80 + 100 * x,
          xpos + 60 + 100 * x,xpos + 80 + 100 * x,xpos + 70 + 100 * x,xpos + 50 + 100 * x,xpos + 30 + 100 * x,xpos + 20 + 100 * x,
          xpos + 40 + 100 * x,};
          int [] n = {245 + 100 * y,245 + 100 * y,265 + 100 * y,245 + 100 * y,245 + 100 * y,
          270 + 100 * y,295 + 100 * y,295 + 100 * y,275 + 100 * y,295 + 100 * y,295 + 100 * y,
          270 + 100 * y};
          page.fillPolygon(m, n, 12);
          
        }else if(board[x][y]==2){   // "2" represents o 
               
          //draw O - using drawOval()
          page.setColor(Color.black);
          page.fillOval(xpos + 20 + 100 * x,240 + 100 * y,60,50);
          page.setColor(lightgreen);
          page.fillOval(xpos + 25 + 100 * x,243 + 100 * y,50,40);
          page.setColor(Color.black);
          page.drawOval(xpos + 25 + 100 * x,243 + 100 * y,50,40);
        }
        }
      }
    
    //announce winner
    page.setFont(new Font("Courier New", Font.ITALIC, 40));
    page.setColor(Color.black);
    if(checkwin() == 1){
      page.drawString("CONGRATS PLAYER 1, YOU WIN!",330,600);
    }else if(checkwin() == 2){
       page.drawString("CONGRATS PLAYER 2, YOU WON!",330,600);
    }else if(checkDraw() == true){
      page.setFont(new Font("Monospaced", Font.BOLD, 40));
      page.drawString("ITS A DRAW",520,600);
    }
    
    //display player scores
    page.setFont(new Font("Serif", Font.PLAIN, 35));
     page.setColor(Color.black);
    //player1
    page.drawString("Player1",300,300);
    page.drawString("has " +  player1wins + " wins",275,400);
    page.drawString("Player2 ",900,300);
    page.drawString("has " +  player2wins + " wins",875,400);
    
    ///draws an extra X and O figure
    // draws O
     x=0;
     y=0;
     xpos=900;
     ypos=315;
     page.setColor(Color.black);
     page.fillOval(xpos + 20 + 100 * x,ypos-3 + 100 * y,60,50);
     page.setColor(lightgreen);
     page.fillOval(xpos + 25 + 100 * x,ypos + 100 * y,50,40);
     page.setColor(Color.black);
     page.drawOval(xpos + 25 + 100 * x,ypos + 100 * y,50,40);
     
     //draws X
     x=0;
     y=0;
     xpos=300;
     ypos=320;
     int [] m = {xpos + 20 + 100 * x,xpos + 30 + 100 * x,xpos + 50 + 100 * x,xpos + 70 + 100 * x,xpos + 80 + 100 * x,
          xpos + 60 + 100 * x,xpos + 80 + 100 * x,xpos + 70 + 100 * x,xpos + 50 + 100 * x,xpos + 30 + 100 * x,xpos + 20 + 100 * x,
          xpos + 40 + 100 * x,};
          int [] n = {ypos + 100 * y,ypos+ 100 * y,ypos+20 + 100 * y,ypos + 100 * y,ypos + 100 * y,
          ypos+25 + 100 * y,ypos+50 + 100 * y,ypos+50 + 100 * y,ypos+30 + 100 * y,ypos+50 + 100 * y,ypos+50 + 100 * y,
          ypos+25 + 100 * y};
     page.fillPolygon(m, n, 12);
  }
  
  //reset method
  public void reset(){
    //clears the game board - goes thorugh the array
    //sets everything to 0, player1 to true
    for(int i=0;i<board.length;i++){
      for(int j=0;j<board.length;j++){
        board[i][j]=0;
      }
    }
    winner =-1;
    player1 = true;
  }
  
  //checkdraw
  public boolean checkDraw(){
    boolean completed = true;
    for(int i=0;i<board.length;i++){
      for(int j=0;j<board.length;j++){
        if(board[i][j] == 0){
          completed = false;
        }
      }
    }
    if(completed == false){
      System.out.print("keep playing");
    }else if(completed == true){
       System.out.print("its a draw");
    }
      return completed;
  }
   
  //checkwin method
  public int checkwin(){
    //checks to see if any winner
    //check vertical
     //winner = -1;
     int m=-1;
    for(int i=0;i<board.length;i++){
      int a = board[i][0];
      int b = board[i][1];
      int c = board[i][2];
      if((a == b) && (b == c)){
        winner = a;
        //System.out.print("hor" +a);
      }
    }
 
    //check hotizontal
    for(int i=0;i<board.length;i++){
      int a = board[0][i];
      int b = board[1][i];
      int c = board[2][i];
      if((a == b) && (b == c)){
        winner = a;
      }
    }
    
    //check \ diagonal
      int a = board[0][0];
      int b = board[1][1];
      int c = board[2][2];
      if((a == b) && (b == c)){
        winner = a;
      }
      
     //check / diagonal
       a = board[0][2];
       b = board[1][1];
       c = board[2][0];
       if((a == b) && (b == c)){
         winner = a;  
       }
       return winner;
    }
 
  //mouse events
  private class XOListener implements MouseListener{
    
    //other mouse events
    public void mousePressed(MouseEvent event){}
    public void mouseReleased(MouseEvent event){}
    public void mouseEntered(MouseEvent event){}
    public void mouseExited(MouseEvent event){}
    
    //main mouse event
    public void mouseClicked(MouseEvent event){
      if(checkwin() > 0){ //if winner =-1, then no winner yet
      //wait for player to play again 
       //p1wins.setText("Player 1 Wins:" + player1wins);
       //p2wins.setText("Player 2 Wins:" + player2wins);
      }else{
        
        //get x and y mouse positon
        int a = event.getX();
        int b = event.getY();
        //xy.setText("X: " + a + "\tY: " + b);
        
      
        if((a<500) || (b<200)){   //out of bounds
          repaint();
        }else if((a>780) || (b>510)){ //out of bounds
          repaint();
        }else{if(a>500 && a<580){
          x=0;
        }else if(a>600 && a<680){
          x=1;
        }else if(a>700 && a<780){
          x=2;
        }
        if(b>225 && b<310){
          y=0;
        }else if(b>325 && b<410){
          y=1;
        }else if(b>425 && b<510){
          y=2;
        }
        if(board[x][y]== 1 || board[x][y]==2){  //space filled - must play somewhere else
              repaint();
        }else{
          if(player1 == true){ //x turn - draw an X
            board[x][y]= 1;
          }if(player1 == false){ //o turn - draw an O
            board[x][y]=2;
          }
        }
        }
        //anounce winner
        System.out.println(checkwin());
        if(checkwin() == 1){
          
          player1wins++;
        }else if(checkwin() == 2){
         player2wins++; 
        }else if(checkDraw() == true){
            //do nothing
        }else
          //switch whos turn it is
          if(player1 == true){ 
            turn.setText("Player 2'S TURN");
            player1=!player1;
          }else{
            turn.setText("Player 1'S TURN");
            player1=!player1;
          }
        //update the game
        repaint();
        //p1wins.setText("Player 1 Wins:" + player1wins);
        //p2wins.setText("Player 2 Wins:" + player2wins);
      }
    } 
  }
  public static void main(String[]args){
    
    JFrame frame = new JFrame("TicTacToe");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
    Dimension DimMax = Toolkit.getDefaultToolkit().getScreenSize();
    frame.setMaximumSize(DimMax);
    //frame.setPreferredSize(new Dimension(300,300));

    frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
    frame.getContentPane().add(new TicTacPanel());
    frame.pack();
    frame.setVisible(true);  
    
  }
}
  //AND WERE DONE!
  //CHECK FOR BUGS AND MISSING SEMI- COLONS and MISSPELLED WORDS