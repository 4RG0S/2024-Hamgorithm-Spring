import java.io.*;
import java.util.*;

public class Q10868 {
    static int[] src;
    static int[] segTree;


    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        // input & data init
        StringTokenizer s=new StringTokenizer(br.readLine()," ");
        StringBuilder writer = new StringBuilder();
        int N= Integer.parseInt(s.nextToken());
        int M= Integer.parseInt(s.nextToken());

        src = new int[N+1];
        segTree = new int[N*4+1];

        for(int i=1;i<N+1;i++){
            src[i]=Integer.parseInt(br.readLine());
        }

        // logic
        segment(1,1,N);
        for(int i=0;i<M;i++){
            s =new StringTokenizer(br.readLine()," ");
            int start = Integer.parseInt(s.nextToken());
            int end = Integer.parseInt(s.nextToken());

            int result = read(1,1,N,start,end);
            writer.append(result).append("\n");
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
}