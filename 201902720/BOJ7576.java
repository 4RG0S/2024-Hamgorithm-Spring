import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ7576 {
    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String[] firstLine = br.readLine().split(" ");
        final int col = Integer.parseInt(firstLine[0]);
        final int row = Integer.parseInt(firstLine[1]);
        final int[][] matrix = new int[row][col];
        for (int i = 0; i < row; i++) {
            final int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            matrix[i] = temp;
        }

        int countZero = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                }
                if (matrix[i][j] == 0) {
                    countZero++;
                }
            }
        }
        if (countZero == 0) {
            System.out.println(0);
            return;
        }

        bfs(matrix, row, col);

        int day = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                day = Math.max(matrix[i][j], day);
            }
        }
        System.out.println(day - 1);
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static Queue<int[]> queue = new LinkedList<>();

    static void bfs(final int[][] matrix, final int row, final int col) {
        while (!queue.isEmpty()) {
            final int[] point = queue.poll();
            final int x = point[0];
            final int y = point[1];
            for (int i = 0; i < 4; i++) {
                final int nx = x + dx[i];
                final int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < row && ny < col) {
                    if (matrix[nx][ny] == 0) {
                        queue.offer(new int[]{nx, ny});
                        matrix[nx][ny] = matrix[x][y] + 1;
                    }
                }
            }
        }
    }
}
