package assignment1;

public class MatrixTranspose {

    public static void main(String[] args) {
        int row = 4, column = 6;
        int[][] matrix = {{1,3,4,5,8,9},
                          {2,4,3,5,6,1},
                          {3,4,5,8,9,2},
                          {2,6,4,1,8,4}};

        // Display current matrix
        display(matrix);

        // Transpose the matrix
        int[][] transpose = new int[column][row];
        for(int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                transpose[j][i] = matrix[i][j];
            }
        }

        // Display transposed matrix
        display(transpose);
    }

    public static void display(int[][] matrix) {
        System.out.println("The matrix is: ");
        for(int[] row : matrix) {
            for (int column : row) {
                System.out.print(column + "    ");
            }
            System.out.println();
        }
    }
}