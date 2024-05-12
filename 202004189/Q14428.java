import java.io.*;
import java.util.*;

public class Q14428 {
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
                writer.append(result.idx).append("\n");
            }
        }


        // output
        System.out.println(writer);
    }

    public static Item segment(int nodeIdx, int start, int end){
        if(start==end){
            return segTree[nodeIdx] = new Item(start,src[start]);
        }

        int mid = (start+end)/2;
        return segTree[nodeIdx] =
                Item.min(segment(nodeIdx*2,start,mid),segment(nodeIdx*2+1,mid+1,end));
    }

    public static Item read(int nodeIdx, int start, int end, int targetStart, int targetEnd){
        if(targetEnd < start || targetStart > end){
            return new Item(0,Integer.MAX_VALUE);
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }
        int mid = (start+end)/2;
        return Item.min(read(nodeIdx*2,start,mid,targetStart,targetEnd),
                read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd));
    }

    public static Item update(int nodeIdx, int start, int end, int updatedIdx, int updateValue){
        if (!(updatedIdx < start || updatedIdx > end)) {
            if(start==end){
                return segTree[nodeIdx] = new Item(updatedIdx,updateValue);
            }

            int mid = (start+end)/2;
            return segTree[nodeIdx] =
                    Item.min(update(nodeIdx*2,start,mid,updatedIdx,updateValue),
                    update(nodeIdx*2+1,mid+1,end,updatedIdx,updateValue));
        }

        return segTree[nodeIdx];
    }
}

class Item{
    int idx;
    int value;
    Item(int i, int v){
        idx=i;
        value=v;
    }

    public static Item min(Item o1, Item o2){
        if(o1.value==o2.value){
            return o1.idx < o2.idx ? o1 : o2;
        }else{
            return o1.value < o2.value ? o1: o2;
        }
    }
}