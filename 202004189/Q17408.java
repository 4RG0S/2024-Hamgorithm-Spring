import java.io.*;
import java.util.*;

public class Q17408 {
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
                writer.append(result.maxValue).append("\n");
            }
        }


        // output
        System.out.println(writer);
    }

    public static Item segment(int nodeIdx, int start, int end){
        if(start==end){
            return segTree[nodeIdx] = new Item(src[start],0);
        }

        int mid = (start+end)/2;
        return segTree[nodeIdx] =
                Item.maxChildren(segment(nodeIdx*2,start,mid),segment(nodeIdx*2+1,mid+1,end));
    }

    public static Item read(int nodeIdx, int start, int end, int targetStart, int targetEnd){
        if(targetEnd < start || targetStart > end){
            return new Item(0,0);
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }
        int mid = (start+end)/2;
        return Item.maxChildren(read(nodeIdx*2,start,mid,targetStart,targetEnd),
                read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd));
    }

    public static Item update(int nodeIdx, int start, int end, int updatedIdx, int updateValue){
        if (!(updatedIdx < start || updatedIdx > end)) {
            if(start==end){
                return segTree[nodeIdx] = new Item(updateValue,0);
            }

            int mid = (start+end)/2;
            return segTree[nodeIdx] = Item.maxChildren(update(nodeIdx*2,start,mid,updatedIdx,updateValue),
                    update(nodeIdx*2+1,mid+1,end,updatedIdx,updateValue));
        }

        return segTree[nodeIdx];
    }
}

class Item{
    int leftMax;
    int rightMax;

    int maxValue;
    Item(int l, int r){
        leftMax = l;
        rightMax = r;
        maxValue=leftMax+rightMax;
    }


    public static Item maxChildren(Item o1, Item o2){
        Item newItem= new Item(Math.max(o1.leftMax, o1.rightMax),Math.max(o2.leftMax, o2.rightMax));
        newItem.maxValue = Math.max(newItem.maxValue,Math.max(o1.maxValue, o2.maxValue));
        return newItem;
    }
}