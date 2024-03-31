import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class BOJ1764 {
    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String[] firstLine = br.readLine().split(" ");
        final int N = Integer.parseInt(firstLine[0]);
        final int M = Integer.parseInt(firstLine[1]);

        final Set<String> n = new HashSet<>();
        for (int i = 0; i < N; i++) {
            n.add(br.readLine());
        }

        final Set<String> m = new HashSet<>();
        for (int i = 0; i < M; i++) {
            m.add(br.readLine());
        }

        n.retainAll(m);
        final List<String> temp = new ArrayList<>(n);
        Collections.sort(temp);

        System.out.println(temp.size());
        for (final String person : temp) {
            System.out.println(person);
        }
    }
}
