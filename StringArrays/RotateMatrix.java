public class RotateMatrix {
    static void transpose(final int arr[][]) {
        final int N = arr.length;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < i + 1; ++j) {
                final int temp = arr[i][j];
                arr[i][j] = arr[j][i];
                arr[j][i] = temp;
            }
        }
    }

    static void flipColumns(final int arr[][]) {
        for (int j = 0; j < N; ++j) {
            for (int i = 0; i < N / 2; ++i) {
                final int temp = arr[i][j];
                arr[i][j] = arr[N - i][j];
                arr[N - i][j] = temp;
            }

        }

    }

    static int[][] rotateMatrix(final int[][] Matrix) throws Exception {
        final int row = Matrix.length;
        final int col = Matrix[0].length;
        if (row != col)
            throw new Exception("The Matrix is not a square");
        transpose(Matrix);
        flipColumns(Matrix);
        return Matrix;
    }

    static void printMatrix(final int arr[][]) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++)
                System.out.print(arr[i][j] + " ");
            System.out.println("");
        }
    }

    public static void main(final String[] args) {
        int arr[][] = { { 1, 2, 3, 4 }, 
                        { 5, 6, 7, 8 }, 
                        { 9, 10, 11, 12 }, 
                        { 13, 14, 15, 16 } };
        System.out.println("The original array :");
        printMatrix(arr);
        arr = rotateMatrix(arr);
        printMatrix(arr);
        
    }
}