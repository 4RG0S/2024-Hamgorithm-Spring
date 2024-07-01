import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Q11003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer s=new StringTokenizer(br.readLine()," ");
        StringTokenizer ss=new StringTokenizer(br.readLine()," ");

        int N = Integer.parseInt(s.nextToken());
        int L = Integer.parseInt(s.nextToken());

        // data init
        Deque<Item> dq = new LinkedList<>();
        StringBuilder writer = new StringBuilder();
        // logic
        // 1 3 2 5 4
        for(int i=0;i<N;i++){
            Item current = new Item(i,Integer.parseInt(ss.nextToken()));

            while(!dq.isEmpty() && i-dq.peekFirst().idx >=L){
                dq.pollFirst();
            }
            if(dq.isEmpty()) {
                dq.offerFirst(current);
            }else if(dq.peekFirst().value > current.value){
                dq.pollFirst();
                dq.offerFirst(current);
            }else if(dq.peekLast().value > current.value){
                while(!dq.isEmpty() && dq.peekLast().value >= current.value){
                    dq.pollLast();
                }
                dq.offerLast(current);
            }else{
                dq.offerLast(current);
            }

            writer.append(dq.peekFirst().value).append(" ");
        }

        // output
        System.out.println(writer);
    }
}

class Item{
    int idx;
    int value;

    Item(int l, int v){
        idx=l;
        value=v;
    }

    @Override
    public String toString(){
        return this.value+"("+this.idx+")";
    }
}
