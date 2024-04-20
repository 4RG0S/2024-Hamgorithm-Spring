import java.util.*;
import java.io.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        String initSentence = br.readLine();
        int N= Integer.parseInt(br.readLine());

        // data init
        Editor editor = new Editor(initSentence);

        // logic
        for(int i=0;i<N;i++){
            StringTokenizer s=new StringTokenizer(br.readLine()," ");
            char cmd = s.nextToken().charAt(0);

            switch (cmd){
                case 'L':
                    editor.left();
                    break;
                case 'D':
                    editor.right();
                    break;
                case 'B':
                    editor.delete();
                    break;
                case 'P':
                    editor.append(s.nextToken().charAt(0));
            }
        }

        // result
        editor.printAll();

    }
}

class Editor{
    Stack<Character> leftStk = new Stack<>();
    Stack<Character> rightStk = new Stack<>();


    Editor(String initSentence){
        IntStream.range(0,initSentence.length())
                .forEach(i->leftStk.push(initSentence.charAt(i)));
    }

    public void left(){
        if(!leftStk.isEmpty()){
            rightStk.push(leftStk.pop());
        }
    }

    public void right(){
        if(!rightStk.isEmpty()){
            leftStk.push(rightStk.pop());
        }
    }

    public void delete(){
        if(!leftStk.isEmpty()){
            leftStk.pop();
        }
    }

    public void append(char c){
        leftStk.push(c);
    }

    public void printAll(){
        StringBuilder writer = new StringBuilder();
        while(!leftStk.isEmpty()){
            writer.append(leftStk.pop());
        }

        writer = writer.reverse();

        while(!rightStk.isEmpty()){
            writer.append(rightStk.pop());
        }

        System.out.println(writer);
    }
}