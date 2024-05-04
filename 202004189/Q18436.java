import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Q18436 {
    static int[] src;
    static Item[] segTree;


    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        // input & data init
        int N= Integer.parseInt(br.readLine());
        StringTokenizer s = new StringTokenizer(br.readLine()," ");
        int M= Integer.parseInt(br.readLine());

        StringBuilder writer = new StringBuilder();

        src = new int[N+1];
        segTree = new Item[N*4+1];

        for(int i=1;i<N+1;i++){
            src[i]=Integer.parseInt(s.nextToken());
        }

        // logic
        segment(1,1,N);

        for(int i=0;i<M;i++){
            s =new StringTokenizer(br.readLine()," ");
            int cmd = Integer.parseInt(s.nextToken());
            int value1 = Integer.parseInt(s.nextToken());
            int value2 = Integer.parseInt(s.nextToken());

            if(cmd==1){
                update(1,1,N,value1,value2);
            }else{
                Item result = read(1,1,N,value1,value2);
                writer.append(cmd==2 ? result.even : result.odd).append("\n");
            }
        }


        // output
        System.out.println(writer);
    }

    public static Item segment(int nodeIdx, int start, int end){
        if(start==end){
            int odd = src[start] % 2==0 ? 0:1;
            int even = src[start] % 2==0 ? 1:0;
            return segTree[nodeIdx] = new Item(odd,even);
        }

        int mid = (start+end)/2;
        return segTree[nodeIdx] =
                Item.sum(segment(nodeIdx*2,start,mid),segment(nodeIdx*2+1,mid+1,end));
    }

    public static Item read(int nodeIdx, int start, int end, int targetStart, int targetEnd){
        if(targetEnd < start || targetStart > end){
            return new Item(0,0);
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }
        int mid = (start+end)/2;
        return Item.sum(read(nodeIdx*2,start,mid,targetStart,targetEnd),
                read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd));
    }

    public static Item update(int nodeIdx, int start, int end, int updatedIdx, int updateValue){
        if (!(updatedIdx < start || updatedIdx > end)) {
            if(start==end){
                int odd = updateValue % 2==0 ? 0:1;
                int even = updateValue % 2==0 ? 1:0;
                return segTree[nodeIdx] = new Item(odd,even);
            }

            int mid = (start+end)/2;
            return segTree[nodeIdx] =
                    Item.sum(update(nodeIdx*2,start,mid,updatedIdx,updateValue),
                    update(nodeIdx*2+1,mid+1,end,updatedIdx,updateValue));
        }

        return segTree[nodeIdx];
    }
}

class Item{
    int value;
    int odd;
    int even;
    Item(int o, int e){
        odd=o;
        even=e;
    }

    public static Item sum(Item o1, Item o2){
        return new Item(o1.odd+o2.odd,o1.even+ o2.even);
    }
}