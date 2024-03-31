import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ1303 {
    static boolean[][] visited;
    static int N;
    static int M;

    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String[] firstLine = br.readLine().split(" ");
        N = Integer.parseInt(firstLine[0]);
        M = Integer.parseInt(firstLine[1]);

        visited = new boolean[M][N];

        final char[][] matrix = new char[M][N];
        for (int i = 0; i < M; i++) {
            final char[] temp = br.readLine().toCharArray();
            matrix[i] = temp;
        }

        int white = 0;
        int blue = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    int depth;
                    if (matrix[i][j] == 'W') {
                        depth = dfs(i, j, 'W', matrix);
                        white += depth * depth;
                    } else {
                        depth = dfs(i, j, 'B', matrix);
                        blue += depth * depth;
                    }
                }
            }
        }
        System.out.println(white + " " + blue);
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static int dfs(final int x, final int y, final char target, final char[][] matrix) {
        visited[x][y] = true;
        int depth = 1;

        for (int i = 0; i < 4; i++) {
            final int nx = x + dx[i];
            final int ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < M && ny < N && !visited[nx][ny] && matrix[nx][ny] == target) {
                depth += dfs(nx, ny, target, matrix);
            }
        }

        return depth;
    }
}
