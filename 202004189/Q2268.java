import java.io.*;
import java.util.*;

public class Q2268 {
    static long[] segTree;
    static long[] src;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer s=new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(s.nextToken());
        int M = Integer.parseInt(s.nextToken());

        // data init
        StringBuilder writer = new StringBuilder();
        segTree = new long[N*4+1];
        src  = new long[N+1];

        // logic
//        segment(1,1,N);

        for(int i=0;i<M;i++){
            StringTokenizer ss=new StringTokenizer(br.readLine()," ");
            int a = Integer.parseInt(ss.nextToken());
            int b = Integer.parseInt(ss.nextToken());
            int k = Integer.parseInt(ss.nextToken());

            if(a==1){
                update(1,1,N,b,k);
            }else{
                long result = read(1,1,N,Math.min(b,k),Math.max(b,k));
                writer.append(result).append("\n");
            }
        }

        // output
        System.out.println(writer);
    }
    public static long segment(int nodeIdx,int start, int end) {
        if (start==end) {
            return segTree[nodeIdx] = src[start];
        }

        int mid = (start+end)/2;
        long left = segment(nodeIdx*2,start,mid);
        long right = segment(nodeIdx*2+1,mid+1,end);

        return segTree[nodeIdx] = (left + right);
    }

    public static long read(int nodeIdx, int start, int end,int targetStart, int targetEnd){
        if (targetEnd < start || targetStart > end) {
            return 0;
        }else if(start >=targetStart && end <= targetEnd) {
            return segTree[nodeIdx];
        }

        int mid = (start+end)/2;
        long left = read(nodeIdx*2,start,mid,targetStart,targetEnd);
        long right = read(nodeIdx*2+1,mid+1,end,targetStart,targetEnd);

        return (left + right);
    }

    public static long update(int nodeIdx, int start, int end, int updatedIdx, long updatedValue){
        if (updatedIdx >= start && updatedIdx <= end) {
            if(start==updatedIdx && end == updatedIdx){
                return segTree[nodeIdx] = updatedValue;
            }

            int mid = (start+end)/2;
            long left = update(nodeIdx*2,start,mid,updatedIdx,updatedValue);
            long right = update(nodeIdx*2+1,mid+1,end,updatedIdx,updatedValue);
            return segTree[nodeIdx] = (left + right);
        }

        return segTree[nodeIdx];
    }
}