import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] a = line.split(" ");
        for(int i = 0; i<8;i++){
//            System.out.println(a[i]);
            if(a[i].equals("0")||a[i].equals("1")){
                continue;
            }else{
                System.out.print("F");
                System.exit(0);
            }
        }
        System.out.print("S");
    }
}