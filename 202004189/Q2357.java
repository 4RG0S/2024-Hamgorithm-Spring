import java.io.*;
import java.util.*;

public class Q2357 {
    static int[] src;
    static Item[] segTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        // input & data init
        StringTokenizer s=new StringTokenizer(br.readLine()," ");
        int N= Integer.parseInt(s.nextToken());
        int M= Integer.parseInt(s.nextToken());

        StringBuilder writer = new StringBuilder();

        src = new int[N+1];
        segTree = new Item[N*4+1];

        for(int i=1;i<N+1;i++){
            src[i]=Integer.parseInt(br.readLine());
        }

        // logic
        segment(1,1,N);

        for(int i=0;i<M;i++){
            s =new StringTokenizer(br.readLine()," ");
            int start = Integer.parseInt(s.nextToken());
            int end = Integer.parseInt(s.nextToken());

            Item result = read(1,1,N,start,end);
            writer.append(result.min).append(" ").append(result.max).append("\n");
        }

        // output
        System.out.println(writer);
    }

    public static Item segment(int nodeIdx, int start, int end){
        if(start==end){
            return segTree[nodeIdx] = new Item(src[start],src[start]);
        }

        int mid = (start+end)/2;
        return segTree[nodeIdx] =
                Item.compare(segment(nodeIdx*2,start,mid),segment(nodeIdx*2+1,mid+1,end));
    }

    public static Item read(int nodeIdx, int start, int end, int targetStart, int targetEnd){
        if(targetEnd < start || targetStart > end){
            return new Item(2100000000,0);
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }
        int mid = (start+end)/2;
        return Item.compare(read(nodeIdx*2,start,mid,targetStart,targetEnd),
                read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd));
    }

    public static Item update(int nodeIdx, int start, int end, int updatedIdx, int updateValue){
        if (!(updatedIdx < start || updatedIdx > end)) {
            if(start==end){
                return segTree[nodeIdx] = new Item(updateValue,updateValue);
            }

            int mid = (start+end)/2;
            return segTree[nodeIdx] = Item.compare(update(nodeIdx*2,start,mid,updatedIdx,updateValue),
                    update(nodeIdx*2+1,mid+1,end,updatedIdx,updateValue));
        }

        return segTree[nodeIdx];
    }
}

class Item{
    int min;
    int max;
    Item(int l, int r){
        min = l;
        max = r;
    }

    public static Item compare(Item o1, Item o2){
        return new Item(Math.min(o1.min,o2.min), Math.max(o1.max,o2.max));
    }
}