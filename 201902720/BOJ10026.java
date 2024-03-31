import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ10026 {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] isChecked;

    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        final char[][] matrix = new char[N][N];
        for (int i = 0; i < N; i++) {
            final char[] temp = br.readLine().toCharArray();
            matrix[i] = temp;
        }

        isChecked = new boolean[N][N];
        int countNone = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!isChecked[i][j]) {
                    dfs(N, i, j, matrix[i][j], matrix);
                    countNone++;
                }
                if (matrix[i][j] == 'G') {
                    matrix[i][j] = 'R';
                }
            }
        }

        isChecked = new boolean[N][N];
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!isChecked[i][j]) {
                    dfs(N, i, j, matrix[i][j], matrix);
                    count++;
                }
            }
        }

        System.out.println(countNone + " " + count);
    }

    static void dfs(final int N, final int x, final int y, final char letter, final char[][] matrix) {
        if (isChecked[x][y]) {
            return;
        }
        isChecked[x][y] = true;

        for (int i = 0; i < 4; i++) {
            final int nx = x + dx[i];
            final int ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < N && ny < N && matrix[nx][ny] == letter) {
                dfs(N, nx, ny, letter, matrix);
            }
        }
    }
}
