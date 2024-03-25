import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

public class BOJ2606 {
    public static void main(final String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        final int M = Integer.parseInt(br.readLine());

        final Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < M; i++) {
            final String[] splits = br.readLine().split(" ");
            final int start = Integer.parseInt(splits[0]);
            final int end = Integer.parseInt(splits[1]);
            if (graph.containsKey(start)) {
                final List<Integer> values = graph.get(start);
                values.add(end);
            } else {
                List<Integer> tempList = new ArrayList<>();
                tempList.add(end);
                graph.put(start, tempList);
            }
            if (graph.containsKey(end)) {
                final List<Integer> values = graph.get(end);
                values.add(start);
            } else {
                List<Integer> tempList = new ArrayList<>();
                tempList.add(start);
                graph.put(end, tempList);
            }
        }

        final List<Integer> visited = dfs(graph, 1);
        System.out.println(visited.size() - 1);
    }

    static List<Integer> dfs(final Map<Integer, List<Integer>> graph, final int startNode) {
        List<Integer> visited = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(startNode);

        while (!stack.isEmpty()) {
            final int node = stack.pop();
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
