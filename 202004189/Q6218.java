import java.io.*;
import java.util.*;

public class Q6218 {
    static Item[] segTree;
    static int[] src;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer s=new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(s.nextToken());
        int M = Integer.parseInt(s.nextToken());

        // data init
        StringBuilder writer = new StringBuilder();
        segTree = new Item[N*4+1];
        src  = new int[N+1];

        for(int i=1;i<N+1;i++){
            src[i] = Integer.parseInt(br.readLine());
        }

        // logic
        segment(1,1,N);

        for(int i=0;i<M;i++){
            StringTokenizer ss=new StringTokenizer(br.readLine()," ");
            int a = Integer.parseInt(ss.nextToken());
            int b = Integer.parseInt(ss.nextToken());

            Item result = read(1,1,N,a,b);
            writer.append(result.calculate()).append("\n");
        }

        // output
        System.out.println(writer);
    }
    public static Item segment(int nodeIdx,int start, int end) {
        if (start==end) {
            return segTree[nodeIdx] = new Item(src[start], src[start]);
        }

        int mid = (start+end)/2;
        Item left = segment(nodeIdx*2,start,mid);
        Item right = segment(nodeIdx*2+1,mid+1,end);

        return segTree[nodeIdx] = Item.compare(left,right);
    }

    public static Item read(int nodeIdx, int start, int end,int targetStart, int targetEnd){
        if (targetEnd < start || targetStart > end) {
            return new Item(-1,Integer.MAX_VALUE);
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }

        int mid = (start+end)/2;
        Item left = read(nodeIdx*2,start,mid,targetStart,targetEnd);
        Item right = read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd);

        return Item.compare(left,right);
    }

//    public static long update(int nodeIdx, int start, int end, int updatedIdx, long updatedValue){
//        if (updatedIdx >= start && updatedIdx <= end) {
//            if(start==updatedIdx && end == updatedIdx){
//                return segTree[nodeIdx] = updatedValue;
//            }
//
//            int mid = (start+end)/2;
//            long left = update(nodeIdx*2,start,mid,updatedIdx,updatedValue);
//            long right = update(nodeIdx*2+1,mid+1,end,updatedIdx,updatedValue);
//            return segTree[nodeIdx] = (left + right);
//        }
//
//        return segTree[nodeIdx];
//    }
}

class Item{
    int max;
    int min;

    Item(int x,int n){
        max=x;
        min=n;
    }

    public static Item compare(Item o1, Item o2){
        return new Item(Math.max(o1.max,o2.max),Math.min(o1.min,o2.min));
    }

    public int calculate(){
        return max-min;
    }
}