import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ5555 {
    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String toFind = br.readLine();
        final int N = Integer.parseInt(br.readLine());

        int answer = 0;
        for (int i = 0; i < N; i++) {
            String alpha = br.readLine();
            alpha = alpha + alpha;
            if (alpha.contains(toFind)) {
                answer++;
            }
        }
        System.out.println(answer);
    }
}
