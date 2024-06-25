import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String v1 = sc.nextLine();
        Boolean[] a = new Boolean[v1.length()];
        String v2 = sc.nextLine();
        Boolean[] b = new Boolean[v2.length()];
        
        for(int i = 0; i<v1.length(); i++){
        	char k = v1.charAt(i);
        	if(k=='1') {
        		a[i]=true;
        	}else {
        		a[i]=false;
        	}
        	
        	char t = v2.charAt(i);
        	if(t=='1') {
        		b[i]=true;
        	}else {
        		b[i]=false;
        	}
        }
        
        for(int i = 0; i<v1.length();i++) {
        	if(a[i]&b[i]==true) {
        		System.out.print("1");
        	}else {
        		System.out.print("0");
        	}
        }
        System.out.println();
        for(int i = 0; i<v1.length();i++) {
        	if(a[i]|b[i]==true) {
        		System.out.print("1");
        	}else {
        		System.out.print("0");
        	}
        }
        System.out.println();
        for(int i = 0; i<v1.length();i++) {
        	if(a[i]^b[i]==true) {
        		System.out.print("1");
        	}else {
        		System.out.print("0");
        	}
        }
        System.out.println();
        for(int i = 0; i<v1.length();i++) {
        	if(a[i]==true) {
        		System.out.print("0");
        	}else {
        		System.out.print("1");
        	}
        }
        System.out.println();
        for(int i = 0; i<v1.length();i++) {
        	if(b[i]==true) {
        		System.out.print("0");
        	}else {
        		System.out.print("1");
        	}
        }
        
        
    }
}