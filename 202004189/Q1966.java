import java.util.*;
import java.io.*;

public class Q1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringBuilder writer =new StringBuilder();

        for(int t=0;t<T;t++){
            StringTokenizer s=new StringTokenizer(br.readLine()," ");
            StringTokenizer ss=new StringTokenizer(br.readLine()," ");
            Queue<Doc> q = new LinkedList<>();

            int N=Integer.parseInt(s.nextToken());
            int targetIndex = Integer.parseInt(s.nextToken());
            int[] priority = new int[10];

            // init
            for(int i=0;i<N;i++){
                int prior = Integer.parseInt(ss.nextToken());
                Doc doc = new Doc(i,prior);
                priority[prior]++;
                q.offer(doc);
            }

            // solution
            int rank = 1;
            while(true){
                Doc currentDoc = q.poll();

                if (isPrior(priority, currentDoc.prior)){
                    if(currentDoc.idx==targetIndex){
                        writer.append(rank).append("\n");
                        break;
                    }
                    priority[currentDoc.prior]--;
                    rank++;
                }else{
                    q.offer(currentDoc); // 다시 넣는다.
                }
            }
        }
        System.out.print(writer);
    }

    public static boolean isPrior(int[] priority, int prior){
        for(int i=9;i>prior;i--){
            if(priority[i] > 0){
                return false;
            }
        }

        return true;
    }
}

class Doc{
    int idx;
    int prior;

    Doc(int i, int p){
        idx=i;
        prior=p;
    }
}