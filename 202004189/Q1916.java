import java.util.*;
import java.io.*;

public class Q1916 {
    static ArrayList<ArrayList<Edge>> graph =
            new ArrayList<>();
    static int[] costInfo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int vertex = Integer.parseInt(br.readLine());
        int edge = Integer.parseInt(br.readLine());

        costInfo = new int[vertex+1];

        for(int i=0;i<=vertex;i++){
            graph.add(new ArrayList<>());
            costInfo[i]=999999999;
        }

        for(int i=0;i<edge;i++){
            StringTokenizer s=new StringTokenizer(br.readLine()," ");

            int from = Integer.parseInt(s.nextToken());
            int end = Integer.parseInt(s.nextToken());
            int cost = Integer.parseInt(s.nextToken());

            graph.get(from).add(new Edge(end,cost));
        }

        StringTokenizer ss=new StringTokenizer(br.readLine()," ");

        int start = Integer.parseInt(ss.nextToken());
        int end = Integer.parseInt(ss.nextToken());


        System.out.println(search(start,end));
    }

    public static int search(int start, int end){
        PriorityQueue<Edge> q = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);

        q.offer(new Edge(start,0));

        while(!q.isEmpty()) {
            Edge currentNode = q.poll();

            if (currentNode.cost > costInfo[currentNode.toNode]) continue; // distance보다 작다면 무시한다.

            for (int i = 0; i < graph.get(currentNode.toNode).size(); i++) {
                Edge targetNode = graph.get(currentNode.toNode).get(i);
                if (costInfo[targetNode.toNode] > targetNode.cost + currentNode.cost) {
                    // 현재 저장된 distance의 값(target까지 가는 최소비용) > target까지 가는 비용+현재 노드로 오기까지의 비용
                    costInfo[targetNode.toNode] = targetNode.cost + currentNode.cost;
                    q.offer(new Edge(targetNode.toNode, targetNode.cost + currentNode.cost));
                }
            }
        }

        return costInfo[end];
    }
}

class Edge{
    int toNode;
    int cost;

    Edge(int e, int c){
        toNode=e;
        cost=c;
    }
}
