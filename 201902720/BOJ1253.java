import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ1253 {
    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        final int[] numbers = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(numbers);

        int answer = 0;
        for (int i = 0; i < N; i++) {
            final int target = numbers[i];
            int start = 0;
            int end = N - 1;

            while (start < end) {
                if (numbers[start] + numbers[end] > target) {
                    end--;
                } else if (numbers[start] + numbers[end] < target) {
                    start++;
                } else {
                    if (start == i) {
                        start++;
                    } else if (end == i) {
                        end--;
                    } else {
                        answer++;
                        break;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
