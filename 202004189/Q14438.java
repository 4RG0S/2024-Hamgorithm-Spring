import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Q14438 {
    static int[] src;
    static int[] segTree;


    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        // input & data init
        int N= Integer.parseInt(br.readLine());
        StringTokenizer s = new StringTokenizer(br.readLine()," ");
        int M= Integer.parseInt(br.readLine());

        StringBuilder writer = new StringBuilder();

        src = new int[N+1];
        segTree = new int[N*4+1];

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
                int result = read(1,1,N,value1,value2);
                writer.append(result).append("\n");
            }
        }


        // output
        System.out.println(writer);
    }

    public static int segment(int nodeIdx, int start, int end){
        if(start==end){
            return segTree[nodeIdx] = src[start];
        }

        int mid = (start+end)/2;
        return segTree[nodeIdx] =
                Math.min(segment(nodeIdx*2,start,mid),segment(nodeIdx*2+1,mid+1,end));
    }

    public static int read(int nodeIdx, int start, int end, int targetStart, int targetEnd){
        if(targetEnd < start || targetStart > end){
            return Integer.MAX_VALUE;
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }
        int mid = (start+end)/2;
        return Math.min(read(nodeIdx*2,start,mid,targetStart,targetEnd),
                read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd));
    }

    public static int update(int nodeIdx, int start, int end, int updatedIdx, int updateValue){
        if (!(updatedIdx < start || updatedIdx > end)) {
            if(start==end){
                return segTree[nodeIdx] = updateValue;
            }

            int mid = (start+end)/2;
            return segTree[nodeIdx] = Math.min(update(nodeIdx*2,start,mid,updatedIdx,updateValue),
                    update(nodeIdx*2+1,mid+1,end,updatedIdx,updateValue));
        }

        return segTree[nodeIdx];
    }
}