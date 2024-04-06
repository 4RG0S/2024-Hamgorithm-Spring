import java.util.*;
import java.io.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        int X = Integer.parseInt(br.readLine());

        // data init
        PriorityQueue<Integer> pq = new PriorityQueue<>(Integer::compareTo);
        int total = 64;
        pq.offer(total);

        // logic
        while(!pq.isEmpty() && total > X){
            int half = pq.poll() / 2 ;
            pq.offer(half);

            if((total - half) < X){
                pq.offer(half);
            }else{
                total-=half;
            }
        }

        // result
        System.out.println(pq.size());
    }
}