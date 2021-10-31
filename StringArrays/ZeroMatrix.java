import java.util.*;
public class ZeroMatrix{
    public static void zeroFill(int[][] arr, int index, boolean col){
        int nrow = arr.length;
        int ncol = arr[0].length;
        if (col)
        { 
            for(int i = 0; i < nrow; ++i){
                for (int j = 0; j < ncol; ++j){
                    if (j == index) arr[i][j] = 0;
                }
            }   
        }
        else{
            for(int i = 0; i < nrow; ++i){
                for (int j = 0; j < ncol; ++j){
                    if (i == index) arr[i][j] = 0;
                }
            }   
        }
    }
    public static void zeroMatrix(int[][] arr ){
        int row = arr.length;
        int col = arr[0].length;
        boolean rows[] = new boolean[row];
        boolean cols[] = new boolean[col];
        Arrays.fill(rows,false);
        Arrays.fill(cols,false);
        for( int i =0; i<row; ++i){
            for (int j = 0; j<col; ++j){
                if (arr[i][j]== 0){rows[i]= true; cols[j]= true;}
            }
        }
        for (int i = 0; i<row; ++i){
            if (rows[i]) zeroFill(arr, i, false);
        }
        for (int j = 0; j < col; ++j){
            if (cols[j]) zeroFill(arr, j, true);
        }
    }
    static void printMatrix(final int arr[][]) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++)
                System.out.print(arr[i][j] + " ");
            System.out.println("");
        }
    }
    public static void main(String[] args) {
        int arr[][] = { { 1, 2, 3, 4 }, 
        { 5, 6, 7, 8 }, 
        { 9, 10, 0, 12 }, 
        { 13, 14, 15, 16 } };
        System.out.println("The original array :");
        printMatrix(arr);
        zeroMatrix(arr);
        System.out.println("The new arry :");
        printMatrix(arr);

        
    }

}

