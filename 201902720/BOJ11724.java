import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

public class BOJ11724 {
    static List<Integer> visited = new ArrayList<>();

    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String[] splits = br.readLine().split(" ");
        final int N = Integer.parseInt(splits[0]);
        final int M = Integer.parseInt(splits[1]);

        final Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < M; i++) {
            final String[] temps = br.readLine().split(" ");
            final int start = Integer.parseInt(temps[0]);
            final int end = Integer.parseInt(temps[1]);
            graph.get(start);
            if (graph.containsKey(start)) {
                final List<Integer> values = graph.get(start);
                values.add(end);
            } else {
                final List<Integer> values = new ArrayList<>();
                values.add(end);
                graph.put(start, values);
            }
            if (graph.containsKey(end)) {
                final List<Integer> values = graph.get(end);
                values.add(start);
            } else {
                final List<Integer> values = new ArrayList<>();
                values.add(start);
                graph.put(end, values);
            }
        }

        final Set<List<Integer>> routes = new HashSet<>();
        for (int i = 1; i <= N; i++) {
            final List<Integer> visited = dfs(graph, i);
            Collections.sort(visited);
            routes.add(visited);
        }
        System.out.println(routes.size());
    }

    static List<Integer> dfs(final Map<Integer, List<Integer>> graph, final int startNode) {
        final Stack<Integer> stack = new Stack<>();

        stack.push(startNode);

        while (!stack.isEmpty()) {
            final Integer node = stack.pop();
            if (visited.contains(node)) {
                continue;
            }
            visited.add(node);
            final List<Integer> neighbors = graph.get(node);
            if (neighbors != null) {
                for (final Integer neighbor : neighbors) {
                    stack.push(neighbor);
                }
            }
        }
        return visited;
    }
}
